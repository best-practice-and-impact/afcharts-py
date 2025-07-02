
# afcharts-py <img src="src/afcharts/assets/logo.svg" alt="afcharts logo" align="right" height="150"/>

afcharts-py is an Python package for creating accessible plots by the Government
Analysis Function. Currently, functions are available for styling
plotly plots.

The package has been developed using the [Government Analysis Function
Data Visualisation
guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).
afcharts-py should be used in conjunction with these guidance documents.

More information about the package and its functions can be found on the
[afcharts
website](https://best-practice-and-impact.github.io/afcharts/).

## Basic folder structure

```plaintext
afcharts-py/
│
├── src/
│   └── afcharts/
│       ├── __init__.py
│       ├── theme_af.py
│       └── assets
│           └── pio_template.py
│
├── tests/
│   ├── conftest.py
│   └── test_module.py
│
├── README.md
├── pyproject.toml
├── LICENSE
└── .gitignore
```

### Explanation of Each Component

- **`src/afcharts/`**: Main package folder. All your code should go here. Using a `src` layout helps avoid import issues during development and testing.
  - `__init__.py`: Makes the directory a Python package.

- **`tests/`**: Contains unit tests.

- **`README.md`**: A markdown file describing your package, how to install and use it.

- **`pyproject.toml`**: The modern configuration file for building and packaging Python projects. It replaces `setup.py` and `setup.cfg`.

- **`.gitignore`**: Specifies files and directories to ignore in version control (e.g., `__pycache__/`, `.DS_Store`, etc.).

## Installation

```bash
pip install afcharts-py
```

## Development only

### Create a Python virtual environment

### Installing with `uv`

[`uv`](https://docs.astral.sh/uv/) is a powerful python package and virtual environement management tool that can be used as a stand in replacement for `pip`. It can be installed with `python -m pip install uv`. Familiar `pip` commands can be run with `uv pip <pip command>` e.g. `uv pip install matplotlib`, `uv pip list`.

To create a virtual environment (in `./.venv`), install the recommended version of python and install the `afcharts` package and all it's dependencies run:

```bash
uv sync
```

Activate the virtual evironment on linux with

```bash
source .venv/bin/activate
```

or on Windows with

```bash
.venv\Scripts\activate
```

This should display `(afcharts)` at the start of your terminal prompt, showing the venv is active.

### To test the package locally and install dependencies

```bash
pip install -e .[dev,test]
```

### Testing

```bash
pytest
```

## Acknowledgments

The afcharts package is based on the
[afcharts](https://github.com/best-practice-and-impact/afcharts.git) package

## License

Unless stated otherwise, the codebase is released under [the MIT
License](LICENSE). This covers both the codebase and any sample code in
the documentation.

The documentation is [© Crown
copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
and available under the terms of the [Open Government
3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
licence.
