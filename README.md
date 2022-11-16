# ReflexSOAR Agent Role Cookiecutter Template

> :warning: <b>WARNING</b><br>Pluggable Agent Roles is only supported with a yet unreleased ReflexSOAR Agent

## Usage

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) if not already installed

```
python3 -m pip install --user cookiecutter
```
**NOTE**: This cookiecutter repository uses Poetry for package installation and management.  You can install it using these [instructions](https://python-poetry.org/docs/#installation)

Generate the package project using the following command:

```
cookiecutter https://github.com/reflexsoar/reflexsoar-agent-role-cookiecutter.git
```

## Developing a Role

1. Determine what the Role should do
2. Define what fields to parse from the `config` parameter as Role specific configurations by setting `config_fields`
3. Add your primary code to the `main` function
4. Implement tests to ensure the role code works correctly
5. Package the role and distribute

## Testing & Code Quality

This template ships with several development environment options for testing, linting, security and type checking. These tools can be run in one of two ways:

- They can all be run independently by running `poetry run <module_name> <module_args>`.  Example `poetry run pylint .`
- You can run the provided `noxfile.py` using `poetry run nox -r` to run them all

### Tools

- flake8
- pytest
- pytest-loguru
- coverage
- coverage[toml]
- bandit
- flynt
- safety
- pre-commit
- nox
- genbadge
- isort
- mypy

## Pre-Commit Checks

This template ships with `pre-commit` installed so that code quality and testing checks pass before committing any code to the repository.  These can be skipped supplied the `--no-verify` flag on the `git commit` command, although it is not recommended.

### Pre-Commit Actions

- Linting/Security checking is performed using flake8 with bugbear and bandit
- Imports are sorted using isort
- Any tests in the test directory are checked to make sure they start with `test_`
- Repository is checked for any leaking private keys
- Trailing whitespaces are trimmed

## Publishing a Role

There are two options for publishing a role:

- Host the new role within your own github account and publish the backend package to PyPI
- Ask the ReflexSOAR project team to incorporate the role into the project as a core role