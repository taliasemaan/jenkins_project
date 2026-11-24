# Jenkins CI/CD Pipeline Report

## Changes Made

- Added a Python virtual environment setup and dependency installation stage.
- Added Flake8 linting for `app.py` and the tests directory.
- Added pytest unit testing.
- Added a Coverage stage that erases prior data, executes tests under coverage, and produces a text and HTML report.
- Added a Security Scan stage that runs Bandit against `app.py` and the tests.
- Added a local deployment stage that copies `app.py` into a `deployment/` directory using `deploy.py`.

## Test and Scan Commands

- `python -m flake8 app.py tests`
- `python -m pytest`
- `python -m coverage erase`
- `python -m coverage run -m pytest`
- `python -m coverage report -m`
- `python -m bandit -r app.py tests`
- `python deploy.py`

## Jenkins Output

The Jenkins job `Python-CI-CD` checked out commit `f6a30dd` from the `main` branch and completed with `Finished: SUCCESS`.

All six pipeline stages passed: Setup, Lint, Test, Coverage, Security Scan, and Deploy.

- Tests: 1 passed.
- Total coverage: 82% (`app.py`: 75%; `tests/test_app.py`: 86%).
- Bandit: no issues identified.
- Deployment: `app.py` copied to the Jenkins workspace's `deployment/` directory.
