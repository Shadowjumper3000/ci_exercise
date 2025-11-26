# CI Exercise - GitHub Actions

This repository demonstrates how to build a Continuous Integration (CI) pipeline step by step using GitHub Actions.

**Each branch contains intentional bugs/issues that the CI step should catch!**

## Quick Summary

| Branch | CI Step | Bugs Introduced | Command to Check |
|--------|---------|-----------------|------------------|
| `main` | None | Clean starting point | - |
| `01-tests` | pytest | `multiply()` returns `a+b` instead of `a*b`; `is_palindrome()` broken | `pytest` |
| `02-code-format` | Black | Missing spaces: `a+b`, `a:float`, `s:str` | `black --check src tests` |
| `03-linting` | Flake8/MyPy | Unused imports (`os`, `sys`, `re`, `json`), unused variables, missing type hints | `flake8 src tests && mypy src` |
| `04-security` | Bandit | `eval()`, `subprocess(shell=True)`, hardcoded passwords, `pickle.loads()`, `mktemp()` | `bandit -r src` |
| `05-build` | python -m build | Missing comma in `setup.py`, bad import in `__init__.py` | `python -m build` |
| `06-complete` | Full pipeline | All bugs fixed - CI passes! | All checks pass |

### How Students Should Use This

1. `git checkout 01-tests` - Run `pytest` locally, see failures, fix the bugs
2. `git checkout 02-code-format` - Run `black --check src tests`, see issues, run `black src tests` to fix
3. `git checkout 03-linting` - Run `flake8 src tests` and `mypy src`, remove unused imports/variables
4. `git checkout 04-security` - Run `bandit -r src`, remove insecure code patterns
5. `git checkout 05-build` - Run `python -m build`, fix syntax errors
6. `git checkout 06-complete` - See the complete working pipeline

---

## Project Structure

```
ci_exercise/
├── src/
│   ├── __init__.py
│   ├── calculator.py      # Simple math operations
│   └── string_utils.py    # String manipulation utilities
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_string_utils.py
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── pyproject.toml         # Tool configurations
└── README.md
```

## Branches - Learning Path

Each branch builds upon the previous one, adding new CI capabilities. **Each branch contains bugs that the CI step will catch!**

| Branch | CI Step | Issues to Fix |
|--------|---------|---------------|
| `main` | No CI | Clean starting point |
| `01-tests` | Unit Tests | `multiply()` uses `+` instead of `*`; `is_palindrome()` has wrong comparison |
| `02-code-format` | Black | Missing spaces around operators and type hints |
| `03-linting` | Flake8 + MyPy | Unused imports, unused variables, missing type annotations |
| `04-security` | Bandit + Safety | `eval()`, `shell=True`, hardcoded passwords, `pickle.loads()`, `mktemp()` |
| `05-build` | Build Package | Syntax error in `setup.py`, bad import in `__init__.py` |
| `06-complete` | Full Pipeline | All issues fixed - CI passes! |

## How to Use This Exercise

### Option 1: Fix the bugs yourself (Recommended)

1. Check out a branch (e.g., `git checkout 01-tests`)
2. Run the CI checks locally to see the failures
3. Fix the issues in the code
4. Verify CI passes locally
5. Move to the next branch

### Option 2: Compare branches to see the fixes

```bash
# See what changed between branches
git diff 01-tests 02-code-format -- src/
```

### Commands to switch branches:

```bash
git checkout main           # Start here - clean code, no CI
git checkout 01-tests       # Has test failures to fix
git checkout 02-code-format # Has formatting issues to fix
git checkout 03-linting     # Has linting issues to fix
git checkout 04-security    # Has security issues to fix
git checkout 05-build       # Has build errors to fix
git checkout 06-complete    # All fixed - complete pipeline
```

## Issues in Each Branch

### `01-tests` - Test Failures

```python
# calculator.py - multiply() is broken
def multiply(a: float, b: float) -> float:
    return a + b  # BUG: Should be a * b

# string_utils.py - is_palindrome() is broken
def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == s  # BUG: Should compare to cleaned[::-1]
```

**Fix:** Change `a + b` to `a * b` and `cleaned == s` to `cleaned == cleaned[::-1]`

### `02-code-format` - Black Formatting Issues

```python
# Missing spaces around operators
def add(a: float,b: float) -> float:  # No space after comma
    return a+b  # No spaces around +
```

**Fix:** Run `black src tests` to auto-format

### `03-linting` - Flake8/MyPy Issues

```python
import os  # F401: unused import
import sys  # F401: unused import

def power(base, exponent):  # Missing type annotations
    unused_variable = 42  # F841: assigned but never used
    return base ** exponent
```

**Fix:** Remove unused imports/variables, add type hints

### `04-security` - Bandit Security Issues

```python
# B307: eval() can execute arbitrary code
return eval(expression)

# B602: shell=True allows command injection
subprocess.run(cmd, shell=True)

# B105: Hardcoded password
DATABASE_PASSWORD = "admin123"

# B301: pickle can execute arbitrary code
pickle.loads(data)

# B306: mktemp has race condition
tempfile.mktemp()
```

**Fix:** Remove all insecure functions and hardcoded secrets

### `05-build` - Build Errors

```python
# setup.py - Missing comma causes SyntaxError
setup(
    name="ci_exercise",
    version="1.0.0"  # Missing comma here!
    description="..."
)

# src/__init__.py - Bad import causes ImportError
from src.nonexistent_module import something
```

**Fix:** Add missing comma, remove bad import

## Local Development

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

### Running CI Checks Locally

```bash
# Tests
pytest --verbose

# Formatting
black --check --diff src tests

# Linting
flake8 src tests
mypy src

# Security
bandit -r src

# Build
python -m build
```

## CI Pipeline Stages Explained

### 1. Tests (`01-tests`)
- Runs unit tests with pytest
- Catches logic errors and bugs
- Generates coverage reports

### 2. Code Formatting (`02-code-format`)
- Checks code follows PEP 8 style using Black
- Ensures consistent, readable code

### 3. Linting (`03-linting`)
- Flake8: Catches unused imports, undefined variables, style issues
- MyPy: Static type checking

### 4. Security (`04-security`)
- Bandit: Finds dangerous functions (eval, exec, shell=True)
- Safety: Checks dependencies for known CVEs

### 5. Build (`05-build`)
- Creates wheel and source distribution
- Catches import errors and syntax issues

### 6. Complete Pipeline (`06-complete`)
- All stages combined
- Matrix testing (Python 3.9, 3.10, 3.11)
- Optimized job dependencies
- Concurrency control
