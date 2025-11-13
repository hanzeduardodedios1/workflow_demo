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

## 🔴 Exercise 1: Introduce a Bug and Observe CI Failure (RED Check)

### 1. Open the Pull Request (PR) and Observe

1. Go to your repository on GitHub
2. Click the **"Compare & pull request"** banner
3. Click **"Create pull request"**
4. Go to the **Checks** tab on the PR page

**Expected Result**: The pipeline status will resolve to **RED (Failed)**, proving the bug was caught automatically.

---

## 🟢 Exercise 2: Fix the Bug and Pass CI (GREEN Check)

This exercise shows getting instant, automated approval after fixing the issue.

### 1. Fix the Code Locally

Open `app.py` in your editor and correct the bug in the `calculate_discount` function:

**Locate this line in `app.py`:**
```python
discount_amount = price * 0.01
```

**Change it to:**
```python
discount_amount = price * rate
```

### 2. Commit and Push the Fix

Commit the correction and push to the same open PR branch. This automatically triggers a pipeline rerun.
```bash
# Commit the fix
git commit -am "Fix: Corrected discount calculation logic."

# Push to update the open PR
git push
```

### 3. Final Validation

1. Return to the PR page on GitHub
2. Observe the pipeline rerun

**Expected Result**: The status will resolve to **GREEN (Success)**. The code is now validated and ready to merge.