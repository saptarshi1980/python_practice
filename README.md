# Python Practice

Run these commands in PowerShell from the project folder.

## Notebook learning order

Each notebook includes runnable examples, explanations, practice cells, and expected results.
Run the notebooks in this order, and run each notebook's cells from top to bottom.

1. [Values, types, and variables](01_variables_types.ipynb)
2. [Operators, comparisons, and conditions](02_operators_and_conditions.ipynb)
3. [Strings](03_strings.ipynb)
4. [Lists and tuples](04_lists_and_tuples.ipynb)
5. [Loops and repetition](05_loops_and_repetition.ipynb)
6. [Dictionaries and sets](06_dictionaries_and_sets.ipynb)
7. [Functions and Scope](07_functions_and_scope.ipynb)
8. [Exceptions and Input Validation](08_exceptions_and_validation.ipynb)
9. [Comprehensions and Unpacking](09_comprehensions_and_unpacking.ipynb)
10. [Files, CSV, and JSON](10_files_csv_and_json.ipynb)
11. [Modules and Project Structure](11_modules_and_project_structure.ipynb)
12. [Dates, Decimal, and Rounding](12_dates_decimal_and_rounding.ipynb)
13. [Object-Oriented Programming](13_classes_and_composition.ipynb)
14. [Iterators and Generators](14_iterators_and_generators.ipynb)
15. [Sorting and Function Tools](15_sorting_and_function_tools.ipynb)
16. [Dataclasses and Type Hints](16_dataclasses_and_type_hints.ipynb)
17. [Testing, Debugging, and Logging](17_testing_and_logging.ipynb)
18. [Useful Standard Library Patterns](18_standard_library_patterns.ipynb)
19. [SQLite and Persistent Records](19_sqlite_and_persistence.ipynb)
20. [Capstone: A Validated Payroll Report](20_payroll_capstone.ipynb)
21. [MySQL with Python](21_mysql_with_python.ipynb)

The loops notebook was previously named `03_loops_and_repetition.ipynb`; use chapter 5 now.
Chapters 1-6 cover fundamentals; chapters 7-20 form an intermediate track. Each intermediate chapter includes worked examples, exercises, and a chapter project. Chapter 13 now includes properties, encapsulation, inheritance, overriding, polymorphism, abstract classes, and composition. Chapters 1-20 use the Python standard library and synthetic data. Chapter 21 adds optional MySQL integration. The final capstone combines validated inputs, Decimal salary calculations, reporting, and tests.

## MySQL lesson setup

Chapter 21 requires a separately running local MySQL server for its live lab. Install the
project dependencies, including the MySQL driver, in your activated virtual environment:

```powershell
python -m pip install -r requirements.txt
```

Chapter 21 uses the local MySQL account `root` with password `xyz123`, host `localhost`,
port `3306`, and database `python_practice`. Create the learning database as shown in the notebook.
MYSQL_HOST, MYSQL_PORT, and MYSQL_DATABASE can override the connection location.
Set RUN_MYSQL to True only after completing setup. The live lab uses temporary tables that
disappear on connection close. Offline examples run without a server; they do not test live SQL.

## Open the project folder

```powershell
cd D:\python_practice
```

## Check Python

```powershell
python --version
```

## Create a virtual environment

Run this once to create a virtual environment named `.venv`:

```powershell
python -m venv .venv
```

## Activate the virtual environment

Run this whenever you open a new terminal to work on the project:

```powershell
.\.venv\Scripts\Activate.ps1
```

Your terminal prompt should now start with `(.venv)`.

If PowerShell blocks the activation script, allow scripts for the current terminal session, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Verify the active Python

```powershell
python -c "import sys; print(sys.executable)"
```

The path should end in `.venv\Scripts\python.exe`.

## Install packages

With the virtual environment activated, install the project dependencies from `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

This includes Jupyter Notebook and `ipykernel` for running Python notebook cells.

For example, install `requests`:

```powershell
python -m pip install requests
```

## Run Jupyter Notebook

With the virtual environment activated and dependencies installed, launch Jupyter Notebook:

```powershell
python -m notebook
```

Open the local URL printed in the terminal if your browser does not open automatically. Create or open an `.ipynb` file and select the Python kernel to execute cells. To stop the server, press `Ctrl+C` in the terminal and confirm if prompted.

## Save installed packages

To save a snapshot of all installed package versions without overwriting the project's dependency list:

```powershell
python -m pip freeze > requirements-lock.txt
```

To install packages from an existing `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

## Run a Python file

Replace `your_file.py` with your script's filename:

```powershell
python your_file.py
```

## Deactivate the virtual environment

```powershell
deactivate
```

## AI and data continuation (Lessons 22?27)

Continue in this order after the existing course. Lessons 22?27 apply the Python foundations
already covered; they do not replace or renumber Lessons 1?21. Each notebook defines its own
inputs and can run from a fresh kernel. Lesson 21's live MySQL lab is not required for the new
lessons. All new examples use small fictional data and need no internet access at runtime.

22. [NumPy arrays](22_numpy_arrays.ipynb) ? shapes, dtypes, masks, broadcasting, and energy summaries.
23. [pandas data analysis](23_pandas_data_analysis.ipynb) ? cleaning, missingness, grouping, and validated joins.
24. [Classical ML](24_scikit_learn_classical_ml.ipynb) ? regression, classification, baselines, leakage, and Pipelines.
25. [PyTorch foundations](25_pytorch_deep_learning.ipynb) ? tensors, autograd, batches, training, evaluation, and weight persistence.
26. [Pydantic and FastAPI](26_pydantic_and_fastapi.ipynb) ? runtime validation, inference boundaries, dependency injection, endpoint tests, and async.
27. [GenAI applications](27_genai_applications.ipynb) ? chunking, lexical vectors, retrieval, a configurable mock client, validated JSON, RAG, and evaluation.

### Course dependencies: one requirements file

All course dependencies are listed in `requirements.txt`, grouped by purpose in comments.
The original Jupyter and MySQL dependencies are retained. No stage-specific requirements files
are needed. From the project terminal, with your chosen environment activated:

```powershell
python -m pip install -r requirements.txt
```

This installs Jupyter, the MySQL driver, NumPy, pandas, scikit-learn, PyTorch, Pydantic v2,
FastAPI, HTTPX, and Uvicorn. This is an installation command for you to run; no packages were
installed or virtual-environment settings changed while creating the lessons.

Lessons 1-20, the new 6A bridge, and Lesson 27's core examples use only the standard library
beyond Jupyter. Lesson 21's live lab additionally requires a local MySQL server, installed separately.
The new data/AI lessons use the packages grouped in the shared requirements file.
PyTorch is the largest dependency; a GPU and torchvision are not required. Version ranges
specify API compatibility families, not a fully executed lockfile. Keep a snapshot once your
environment is working.

Use the existing Jupyter launch instructions above (`python -m notebook`), open the desired file,
and run top to bottom with Shift+Enter. Check `import sys; print(sys.executable)` in a scratch cell
if a package appears installed but cannot be imported. Restart the kernel after changing packages.
Do not name local files numpy.py, pandas.py, torch.py, or fastapi.py.

### Practice before opening solutions

Predict each example's output, run it, change one value, and explain the difference. Complete the
five scaffolded exercises and chapter project in each lesson before opening the matching notebook
in [instructor_solutions](instructor_solutions/). The answer keys explain reasoning and include
assertions; they also define their own worked-example setup and run independently. Check values
in learner notebooks help diagnose your work without giving complete implementations.

For pair study, take turns explaining a transformation and reviewing the other's edge-case checks.
Restart and Run All before sharing your completed notebook. Save your own work deliberately;
model and data examples use temporary folders and do not leave large generated artifacts.

### Validation and scope

[Coverage notes](course_coverage_notes.md) record how the new sequence builds on the existing lessons.
[Validation notes](course_validation.md) distinguish executed cells from static checks.
Run `.\.venv\Scripts\python.exe validate_ai_course.py --execute` to validate the new notebooks,
compile every code cell (including notebook top-level await), verify the original-file hashes,
and execute dependency-ready lessons and solutions in fresh kernels. Missing packages are reported,
never installed. The validator uses the calling interpreter and writes no executed notebooks.
The original-file hashes are a creation-time preservation check; if you later edit earlier lessons
intentionally, expect that check to flag the change.

Lesson 26 tests run in-process without launching a web server. Its formula service has exact test
values and can later be replaced by a trained model; it is identified as a formula, not learned ML.
Lesson 27's mock client and word-count vectors run without secrets or model downloads. They teach
application structure and failure handling, not real LLM quality or semantic retrieval. External
provider integration is optional and requires your own provider choice and runtime configuration.


## Lesson 6A: searching, transformations, and reusable records

After [Lesson 6](06_dictionaries_and_sets.ipynb), open
[06_A_modern_function.ipynb](06_A_modern_function.ipynb). This self-contained standard-library
bridge covers searching lists/dictionaries/sets, converting representations, zip, enumerate,
unpacking, comprehensions, lambda, functions, OOP, dataclasses, type hints, iterators, and generators.
It introduces the vocabulary needed to try the examples now and links to the existing later
chapters for deeper practice. Continue to Lesson 7 afterward, or revisit 6A as a review after Lesson 16.
The existing Lesson 6 filename and contents are unchanged.

Complete its ten exercises and employee-directory capstone before opening
[instructor solutions](instructor_solutions/06_A_modern_function_solutions.ipynb).
Both new notebooks run independently and require no additional packages.


## Lesson 23A: visualization before machine learning

Recommended order: [23 pandas](23_pandas_data_analysis.ipynb) ?
[23_A_data_visualization.ipynb](23_A_data_visualization.ipynb) ?
[24 classical ML](24_scikit_learn_classical_ml.ipynb). Existing chapter numbers stay unchanged.

The visualization chapter teaches **Matplotlib**, **Seaborn**, and **Plotly**: choosing chart types,
counts and distributions, labelled scatter plots, subplots, correlation heatmaps, interactive hover,
zoom and facets, accessible encodings, and local PNG/SVG/HTML export. It includes six scaffolded
exercises, expected checks, interpretation questions, and a visual-report capstone. Attempt these
before opening [the instructor answer key](instructor_solutions/23_A_data_visualization_solutions.ipynb).

Data comes from scikit-learn's bundled [Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html):
150 flower measurements and three species, loaded locally with `load_iris(as_frame=True)`.
No Kaggle account, dataset URL request, network download, model training, or confidential data is
needed. This public dataset is an explicit exception to the fictional-data examples elsewhere.

The three visualization packages are now included in the single `requirements.txt`, alongside
NumPy, pandas, and scikit-learn. Use the same install command as the rest of the course:

```powershell
python -m pip install -r requirements.txt
```

No packages were installed during chapter creation. Plotly's compact `plotly_mimetype` output
requires a compatible notebook frontend. If it appears blank, follow the chapter's renderer
troubleshooting or export self-contained HTML with embedded JavaScript for offline viewing.
Static Plotly image export is optional and is not required; Matplotlib provides PNG/SVG.
All export examples use temporary folders; choose a deliberate output path to keep an artifact.
