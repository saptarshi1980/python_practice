# Validation performed

Updated for the requested Lesson 6A and shared requirements setup.

Validated with the existing project Python 3.12 environment; no packages were installed and
no virtual-environment configuration was changed. All lesson syntax targets Python 3.11+.

| Files | nbformat validation | Code compilation | Execution in order |
| --- | --- | --- | --- |
| 6A learner + solutions | Passed | Passed | Passed in separate fresh Jupyter kernels |
| 22 learner + solutions | Passed | Passed | Not run: NumPy absent |
| 23 learner + solutions | Passed | Passed | Not run: NumPy and pandas absent |
| 24 learner + solutions | Passed | Passed | Not run: NumPy, pandas, scikit-learn absent |
| 25 learner + solutions | Passed | Passed | Not run: NumPy and PyTorch absent |
| 26 learner + solutions | Passed | Passed, including top-level await | Not run: Pydantic and FastAPI absent; HTTPX available |
| 27 learner + solutions | Passed | Passed | Passed in separate fresh Jupyter kernels |

All new code cells compile, including unanswered scaffold cells. Lesson 6A has ten exercises;
each of Lessons 22-27 has five exercises. Each also has a chapter project, separated from the answer keys. Every answer key includes the
same worked setup followed by explained solutions and assertion checks. Exercise/task inputs and
expected values were reviewed against their answer keys. The validator independently checks small
numerical reference values for array totals, masks, accepted energy totals, regression and
classification metrics, derivative/optimizer-step arithmetic, and API formulas using the standard
library. These independent checks do **not** establish that unavailable third-party libraries ran.

Stage 27 execution covers all core examples, its answer key's five exercises and capstone,
lexical retrieval fixtures, zero-overlap abstention, invalid chunk size/overlap, malformed JSON,
unknown citations, invalid boolean fields, simulated timeouts, and per-case service failure counts.
The commented optional FastAPI integration was not executed. No real LLM, embedding provider,
network service, GPU, or live API was used or evaluated.

Known-value checks were corrected during validation. All shipped code cells now compile.
The API formula is clamped at zero so its output remains within the nonnegative response contract
even for the coldest valid temperature. Model-training metrics are deliberately reported at
runtime rather than claimed as measured results here; stochastic weights and metrics are not
hard-coded as exact expected outputs.

Original-file SHA-256 checks confirm all 21 original notebooks and .gitignore are unchanged. requirements.txt was subsequently
updated at the user's explicit request to consolidate dependencies; the existing entries were
retained and the six separate stage/aggregate requirements files were removed. A separate README prefix hash confirms its pre-existing bytes were preserved;
only the continuation was appended. No backups were used as replacements. Git was used only
for a local read-only status check; no GitHub access, remote creation, commit, or push occurred.

To rerun:

```powershell
.\.venv\Scripts\python.exe validate_ai_course.py --execute
```

After you install a stage's requirements yourself, this command executes that stage and its
solution notebook in separate fresh kernels using the calling interpreter. Execution happens
inside temporary working directories and outputs remain in memory. It never installs packages,
rewrites learner work, registers a kernel, or saves model/data artifacts in the repository.
The broad dependency ranges are API compatibility constraints, not a fully executed lockfile.


Lesson 6A validation covers every worked example, ten explained exercise solutions, and its
capstone in separate fresh kernels. Checks include first/all/absent searches, exact dictionary
pairs, set membership, representation round trips, strict zip failure, duplicate IDs, function
validation, independent defaults, ordering/ties, iterator exhaustion, dataclass state, generator
consumption, invalid/nonfinite pay, missing fields, unchanged source records, and a JSON round trip.
Only setup text was changed in Lessons 22-27 and their keys to reference requirements.txt;
their runnable code and learning content were preserved.


## Visualization chapter (23A)

Both 23_A_data_visualization.ipynb and its instructor answer key pass nbformat validation and
compilation of every code cell. The learner version includes six exercise scaffolds and a project;
its answer key includes matching implementations, data/figure assertions, and export checks.
The current environment lacks NumPy, pandas, scikit-learn, Matplotlib, Seaborn, and Plotly.
Neither new notebook was executed, rendered, or visually reviewed; their plotting, exercise,
and artifact-export assertions remain unexecuted until those dependencies are installed by the
learner. No installation was attempted, and no charts or exported artifacts were stored.

The public dataset's documented 150 samples, four numeric measurements, centimetre units,
and three balanced classes were checked against the official scikit-learn loader documentation.
Chart code and expected checks were reviewed against the exercise descriptions and official
library APIs. This review does not substitute for runtime or visual verification. The validator
now detects the 23A learner/solution pair separately from Lesson 23, and reports missing packages.
Existing notebooks, including their outputs and metadata, were verified unchanged by hashes.
