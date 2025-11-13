# CI Workshop Demo: Automated Testing Workflow

This repository is designed to demonstrate how **Continuous Integration (CI)** works in practice using **GitHub Actions** and Python.

The core purpose of this exercise is to observe the automated feedback loop: **RED Check (Failure)** and **GREEN Check (Success)**.

---

## 💻 Prerequisites (Run Locally)

To run the local tests and push the code, you must have Python and the necessary testing tools installed.

### 1. Install Python

Ensure you have **Python 3** installed on your system (version 3.8 or newer is recommended).

- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: Install via Homebrew: `brew install python3` or download from [python.org](https://www.python.org/downloads/)
- **Linux**: Usually pre-installed. If not, use your package manager (e.g., `sudo apt install python3` for Ubuntu/Debian)

### 2. Install Dependencies

You will need the `pytest` framework to execute the unit tests and `flake8` for code style checks.

#### Windows (Command Prompt or PowerShell)
```bash
pip install pytest flake8
```

#### macOS / Linux
```bash
pip3 install pytest flake8
```

#### Alternative: Using Python Module Installation (All Platforms)
```bash
python -m pip install pytest flake8
```
or
```bash
python3 -m pip install pytest flake8
```

> **Note**: If you encounter permission errors on macOS/Linux, you can either:
> - Add `--user` flag: `pip3 install --user pytest flake8`
> - Use a virtual environment (recommended for project isolation)

---

# CI Demo Steps: Bug to Fix

This process starts with the buggy code in your local `feature/discount-fix-attempt` branch and ends with a successful merge validation on GitHub.

## I. Trigger the Failure (RED Check)

The goal is to push the bug and observe the automated pipeline reject it.

**1. Verify Local Branch:** Ensure you are on the feature branch:
```bash
git checkout feature/discount-fix-attempt
```

**2. Confirm Bug Exists:** Run tests locally to see the expected failure message:
```bash
pytest
```

Expectation: 1 test fails (`test_discount_calculation_failure_demo`).

**3. Push and Open PR:** Push the current state of the code to GitHub and open a Pull Request against the `main` branch.
```bash
git push -u origin feature/discount-fix-attempt
```

(Go to GitHub and create the PR.)

**4. Observe Failure:** Monitor the "Checks" section of the PR.

Result: The GitHub Actions pipeline status turns RED (Failed), specifically due to the Unit Test failure. The merge is blocked.

## II. Fix the Code and Validate (GREEN Check)

The goal is to fix the bug locally and let the pipeline instantly verify the correction.

**1. Implement the Fix:** Open `app.py` and correct the logic error in the `calculate_discount` function:
```python
# Change the faulty line:
discount_amount = price * 0.01 

# To the correct line:
discount_amount = price * rate 
```

**2. Commit the Fix:** Save the file and commit the correction to the same branch:
```bash
git commit -am "Fix: Corrected discount calculation logic."
```

**3. Push and Rerun CI:** Push the correction to GitHub. This automatically triggers a new pipeline run.
```bash
git push
```

**4. Final Validation:** Return to the open PR on GitHub.

Result: The pipeline runs again and resolves to GREEN (Success). The code is now validated, and the merge is approved.