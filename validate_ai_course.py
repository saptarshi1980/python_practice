r"""Read-only validation; no installation and no changes to existing notebooks or environments.

Run with the project's interpreter to use its existing nbformat/nbclient installation:
    .\.venv\Scripts\python.exe validate_ai_course.py
Use --execute to run complete lessons whose dependencies are available in clean Jupyter kernels.
The optional commented API integration in Lesson 27 is intentionally excluded from core execution.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import importlib.util
import json
import math
import os
import sys
import tempfile

import nbformat

ROOT = Path(__file__).resolve().parent
DEPENDENCIES = {
    '06_A': [],
    '22': ['numpy'], '23': ['numpy', 'pandas'],
    '23_A': ['numpy', 'pandas', 'sklearn', 'matplotlib', 'seaborn', 'plotly'],
    '24': ['numpy', 'pandas', 'sklearn'], '25': ['numpy', 'torch'],
    '26': ['pydantic', 'fastapi', 'httpx'], '27': [],
}


def check_reference_values():
    """Independently check small numerical fixtures without replacing library execution."""
    readings = [[10, 12, 14], [20, 22, 24]]
    assert [sum(row) for row in readings] == [36, 66]
    assert [sum(row[i] for row in readings) for i in range(3)] == [30, 34, 38]
    assert [sum(value * rate for value, rate in zip(row, [2, 3, 4], strict=True))
            for row in readings] == [112, 202]
    assert sum([112, 202]) == 314
    assert [v for row in readings for v in row if 12 <= v < 23] == [12, 14, 20, 22]
    assert [sum(v*r for v, r in zip(row, [2, 3, 4], strict=True))
            for row in [[1, 2, 3], [4, 5, 6]]] == [20, 47]
    assert [value for value in [10., -1., math.nan, 20., math.inf, 0.]
            if math.isfinite(value) and value >= 0] == [10., 20., 0.]
    assert sum([10, 20, 30]) * 3 == 180  # Accepted pandas energy cost.
    errors = [abs(a-b) for a, b in zip([10, 20, 30], [12, 18, 33], strict=True)]
    assert math.isclose(sum(errors)/3, 7/3)
    assert math.isclose(math.sqrt(sum(e*e for e in errors)/3), math.sqrt(17/3))
    actual, predicted = [0, 0, 1, 1, 1], [0, 1, 1, 0, 1]
    matrix = [[sum(a == row and p == col for a, p in zip(actual, predicted, strict=True))
               for col in [0, 1]] for row in [0, 1]]
    assert matrix == [[1, 1], [1, 2]]
    assert sum([0., 2., 4.])/3 == 2
    assert 2*100+1 == 201
    assert (2*3-9)**2 == 9 and 2*(2*3-9)*3 == -18
    weight_after_step = 0 - 0.1 * (2 * (2*0-4) * 2)
    assert math.isclose(weight_after_step, 1.6)
    assert math.isclose((2*weight_after_step-4)**2, 0.64)
    assert max(0., 5+3*4+0.5*25) == 29.5
    assert max(0., 5+3*2+0.5*20) == 21
    assert [max(0., 5+3*h+0.5*25) for h in [0, 4]] == [17.5, 29.5]
    assert max(0., 5+3*0+0.5*(-20)) == 0
    print('Reference values: array totals/masks, energy cleaning totals, metrics, gradient/step arithmetic, API formula checked with standard-library fixtures.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true')
    args = parser.parse_args()
    check_reference_values()
    original_hashes = json.loads((ROOT / 'course_original_hashes.json').read_text())
    for name, expected in original_hashes.items():
        # The user explicitly requested dependency consolidation after the initial creation.
        # Keep the original manifest as historical evidence; preserve notebook checks.
        if name == 'requirements.txt':
            continue
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(f'Existing file changed since baseline: {name}')
    readme = (ROOT / 'README.md').read_bytes()
    marker = b'\n## AI and data continuation (Lessons 22'
    original_readme = readme[:readme.index(marker)]
    assert hashlib.sha256(original_readme).hexdigest() == (ROOT / 'course_readme_original.sha256').read_text().strip()
    print('Preservation: all 21 original notebooks and .gitignore unchanged; original README bytes preserved as prefix. requirements.txt intentionally consolidated at user request.')
    for stage, dependencies in DEPENDENCIES.items():
        # A bridge such as 23_A must not be included again under the base stage 23.
        paths = [path for folder in [ROOT, ROOT / 'instructor_solutions']
                 for path in sorted(folder.glob(f'{stage}_*.ipynb'))
                 if not (stage == '23' and path.name.startswith('23_A_'))]
        # Respect the learner's renamed bridge notebook without renaming it back.
        renamed_bridge = ROOT / '06_modern_function_based_on_dict_set.ipynb'
        if stage == '06_A' and len(paths) == 1 and renamed_bridge.exists():
            paths.insert(0, renamed_bridge)
        assert len(paths) == 2
        missing = [module for module in dependencies if importlib.util.find_spec(module) is None]
        for path in paths:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
            code_cells = [cell for cell in notebook.cells if cell.cell_type == 'code']
            for index, cell in enumerate(code_cells):
                compile(cell.source, f'{path.name}:code-{index}', 'exec', flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
            if path.parent == ROOT:
                assert sum('exercise' in cell.metadata.get('tags', []) for cell in code_cells) >= 6
            print(f'VALID {path.relative_to(ROOT)}: nbformat + {len(code_cells)} code cells compile')
            if missing:
                print('  NOT EXECUTED: missing ' + ', '.join(missing))
            elif args.execute:
                from nbclient import NotebookClient
                from jupyter_client import KernelManager
                # Override the process command so execution uses exactly this interpreter,
                # without installing a kernelspec or modifying the virtual environment.
                manager = KernelManager(kernel_name='python3')
                manager.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
                with tempfile.TemporaryDirectory(prefix='ai-course-check-') as workdir:
                    NotebookClient(notebook, km=manager, timeout=180,
                                   resources={'metadata': {'path': workdir}}).execute(
                                       cleanup_kc=True,
                                       env={**os.environ, 'IPYTHONDIR': str(Path(workdir) / '.ipython')})
                print('  EXECUTED: fresh kernel, all core cells passed; outputs not saved')
            else:
                print('  Execution available; pass --execute to run in a fresh kernel')


if __name__ == '__main__':
    main()
