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
