# {{ cookiecutter.target_name }} Role

{% if cookiecutter.test_badge %}![Tests Status](./.badges/tests-badge.svg){% endif %} {% if cookiecutter.coverage_badge %}![Coverage](./.badges/coverage-badge.svg){% endif %} {% if cookiecutter.lint_badge %}![Flake8](./.badges/flake8-badge.svg){ % endif %} {% if cookiecutter.status_badge %}![Status](https://img.shields.io/badge/Status-{{ cookiecutter.status }}){% endif %}

## Installation



```python
poetry add {{ cookiecutter.package_name }}

reflexsoar-agent --start
```
