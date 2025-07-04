# Contributing to This Project

Thank you for considering contributing to this project! We welcome contributions from the community and are grateful for your support.

## Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub. When reporting an issue, please include:

- A clear and descriptive title
- A detailed description of the problem or suggestion
- Steps to reproduce the issue (if applicable)
- Any relevant logs, screenshots, or code snippets

## Submitting Pull Requests

We welcome pull requests! To submit a pull request:

1. Fork the repository and create your branch from `main`.
2. Make your changes in a new branch.
3. Ensure your code follows the coding standards outlined below.
4. Write or update tests as needed.
5. Ensure all tests pass.
6. Submit a pull request with a clear description of your changes.

## Coding Standards

- Follow PEP 8 style guidelines for Python code.
- Write clear, concise, and well-documented code.
- Use meaningful variable and function names.
- Include comments where necessary to explain complex logic.

## Community Guidelines

- Be respectful and inclusive in all interactions.
- Provide constructive feedback and be open to receiving it.
- Help others in the community when possible.
- Follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

Thank you for helping make this project better!

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

## Development setup

### Installing the `afcharts` package

#### Installing with `uv`

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

#### Installing with pip

If you don't want to use `uv`, the package can be installed in developer mode from the root directory of the repository with
```bash
pip install -e .[dev,test]
```
This assumes you already have a python virtual environment set up with your preferred tool (`conda`/`virtualenv`/`uv` etc.).

### Testing
To test your installation, run `pytest` to confirm all unit tests pass successfully in your environment
```bash
pytest
```

### Installing pre-commit hooks

Pre-commit hooks (configured in `.pre-commit-config.yaml`) run automated checks against your changes whenever you commit code. This will:
- Format your code according to agreed formatting guidelines.
- Check for common coding mistakes or deviations from best practices

To activate the pre-commit hooks run (you only have to do this once):

```bash
pre-commit install
```

You can test it on demand by running the following command:

```bash
pre-commit run --all-files
```

Now, whenever you try to make a commit, the pre-commit hooks will run to lint and format the staged files. 
If your files are formatted or auto-fixed, stage (`git add .`) the automated formatting corrections and try committing again. If there are linting errors you may
need to manually resolve these before committing again. In some *rare* circumstances you may need to make a commit that bypasses/fails the pre-commit hooks, in which case you can use:
```bash
git commit --no-verify -m 'feat(SCP-___): my commit message'
```

## Contributing

