import subprocess

dev_packages = [
    "flake8",
    "pytest",
    "pytest-loguru",
    "coverage",
    "bandit",
    "flynt",
    "safety",
    "pre-commit",
    "nox",
    "genbadge",
    "isort",
    "coverage[toml]",
    "mypy"
]

subprocess.run(["poetry", "add", "reflexsoar-agent"])
for package in dev_packages:
    subprocess.run(["poetry", "add", "--group", "dev", package])
