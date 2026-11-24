# Jenkins CI/CD Pipeline Report

## Changes Made

- Added a Python virtual environment setup and dependency installation stage.
- Added Flake8 linting for `app.py` and the tests directory.
- Added pytest unit testing.
- Added a Coverage stage that erases prior data, executes tests under coverage, and produces a text and HTML report.
- Added a Security Scan stage that runs Bandit against `app.py` and the tests.
- Added a local deployment stage that copies `app.py` into a `deployment/` directory using `deploy.py`.
- Added cleanup of the Jenkins workspace after every build.

## Test and Scan Commands

- `flake8 app.py tests`
- `pytest`
- `coverage erase && coverage run -m pytest && coverage report -m`
- `bandit -r app.py tests`
- `python deploy.py`

## Jenkins Output

The pipeline stages are named Setup, Lint, Test, Coverage, Security Scan, and Deploy. Jenkins must configure the job to use `Jenkinsfile_Talia_Semaan` and trigger builds after the repository is pushed.

Local verification produced:

- 1 pytest test passed.
- Coverage: 82% across the application and test modules.
- Bandit: 0 security issues found.
- Deployment: `app.py` copied successfully into the local `deployment/` directory.
