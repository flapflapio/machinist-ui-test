# machinist-ui-test [![Build](https://github.com/flapflapio/machinist-ui-test/actions/workflows/test.yml/badge.svg)](https://github.com/flapflapio/machinist-ui-test/actions/workflows/test.yml)

Functional testing for the machinist-ui project

## QuickStart

1. Install [`poetry`](https://github.com/python-poetry/poetry), and then run:
   `poetry install`
2. Install [google chrome](https://www.google.com/intl/en_ca/chrome/)
3. Run tests with pytest: `poetry run pytest`

Check out the below section [Using Poetry](#using-poetry) on using poetry to
manage the virtual environment associated with your project. If you are using
vscode, remember that you need to point vscode to the virtual environment
associated installed by poetry (see below).

## Using Poetry

This project uses [poetry](https://github.com/python-poetry/poetry) for
dependency management. To operate a poetry environment:

```bash
# Install all dependencies
poetry install

# Open a poetry shell
poetry shell

# Open vscode
code .

# Then go to bottom left > configure python interpreter > select the one in your virtualenv
```
