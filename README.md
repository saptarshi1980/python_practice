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

The loops notebook was previously named `03_loops_and_repetition.ipynb`; use chapter 5 now.
The next planned topic is functions; its notebook has not been created yet.

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
