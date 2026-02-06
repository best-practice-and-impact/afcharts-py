# Contributing to This Project

Thank you for considering contributing to this project! We welcome contributions from the community and are grateful for your support.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners before making a change.

## Community Guidelines

- Be respectful and inclusive in all interactions.
- Provide constructive feedback and be open to receiving it.
- Help others in the community when possible.
- Follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

## Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub. When reporting an issue, please include:

- A clear and descriptive title
- A detailed description of the problem or suggestion
- Steps to reproduce the issue (if applicable)
- Any relevant logs, screenshots, or code snippets

## Code style

- We follow [Python style guide - The GDS Way](https://gds-way.digital.cabinet-office.gov.uk/manuals/programming-languages/python/python.html#python-style-guide)
- Use meaningful variable and function names.
- We name variables using few nouns in lowercase, e.g. `mapping_names`
or `increment`.
- We name functions using verbs in lowercase, e.g. `map_variables_to_names` or
`change_values`.
- Follow PEP 8 style guidelines for Python code.
- Write clear, concise, and well-documented code. Include comments where necessary to explain complex logic.
- We use the [Google](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
format for documenting features using docstrings.

## Submitting Pull Requests

We welcome pull requests! To submit a pull request:

1. Branch from the `dev` branch.
2. Update the README.md and other documentation with details of major changes
to the interface, this includes new environment variables, useful file
locations and container parameters.
3. Ensure your code follows the coding standards outlined below.
4. Write or update tests as needed.
5. Ensure all tests pass.
6. Ensure all pre-commit checks pass. See the instructions for installing and using pre-commit below
7. Once you are ready for review please open a pull/merge request to the
`dev` branch with a clear description of your changes and a title following the conventional-commit format (see below).
8. You may merge the Pull/Merge Request in once you have the sign-off of two
maintainers.

### Conventional commit PR titles

When you raise a pull request (PR), please ensure the PR title follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#specification) format (see [guidance gist](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#examples)).

The `PR Conventional Commit Semantic Title Check` github workflow check will fail at the bottom of your PR if the title doesn't meet the requirements.

Using conventional commit commit PR titles just involves structuring your title in the format:
`<type>(<optional scope>): <description>`
where:

- `<type>` is one of the specific phases given below describing the type of change
- `(<optional scope>)` provides additional contextual information about the area of the codebase affected. If omitted also leave out the brackets.
- `<description>` contains a concise description of the change (in the imperative, present tense: "change" not "changed" nor "changes").

#### Common change types

- Changes relevant to the API or UI:
  - `feat` Commits that add, adjust or remove a new feature to the codebase
  - `fix` Commits that fix a codebase bug of a preceded `feat` commit
  - `test` Commits that add missing tests or correct existing ones
  - `docs` Commits that exclusively affect documentation
  - `style` Commits that address code style (e.g., white-space, formatting, missing semi-colons) and do not affect application behaviour
  - `refactor` Commits that rewrite or restructure code without altering codebase behaviour
  - `build` Commits that affect build-related components such as build tools, dependencies, project version, CI/CD pipelines, ...
  - `chore` Miscellaneous commits e.g. modifying `.gitignore`, ...

## Basic folder structure

```plaintext
afcharts-py/
│
├── .github/                            # Github templates and workflows
│
├── docs/
│   └── images/                         # Image files
│
├── src/
│   └── afcharts/                       # Main package folder
│       ├── __init__.py
│       ├── pio_template.py             # Plotly template
│       ├── afcharts.mplstyle           # Matplotlib stylesheet
│       └── cookbook/
│           ├── _quarto.yml
│           └── index.qmd
│           └── getting-started.qmd
|
├── tests/                              # Unit tests
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── pyproject.toml
└── .gitignore
└── .pre-commit-config.yaml
```


## Development setup

### Installing the `afcharts` package

#### Installing with `uv`

[`uv`](https://docs.astral.sh/uv/) is a powerful python package and virtual environement management tool that can be used as a stand in replacement for `pip`. It can be installed with `python -m pip install uv`. Familiar `pip` commands can be run with `uv pip <pip command>` e.g. `uv pip install matplotlib`, `uv pip list`.

To create a virtual environment (in `./.venv`), install the recommended version of python and install the `afcharts` package and all it's dependencies run:

```bash
uv sync
```

Activate the virtual environment on linux with

```bash
source .venv/bin/activate
```

or on Windows with

```bash
.venv\Scripts\activate
```

This should display `(afcharts)` at the start of your terminal prompt, showing the venv is active.

`afcharts` will be installed in editable mode (like `pip install -e .`) so that changes to the code will take effect without reinstalling the package.

#### Installing with pip

If you don't want to use `uv`, the package can be installed in developer (editable) mode from the root directory of the repository with:

```bash
pip install -e . --group test --group dev
```

This assumes you already have a python virtual environment set up with your preferred tool (`conda`/`virtualenv`/`uv` etc.).

### Testing

To test your installation, run `pytest` to confirm all unit tests pass successfully in your environment:

```bash
pytest
```

See [docs/pytest_intro.md](docs/pytest_intro.md) for guidance on adding unit tests with `pytest`.

### Reproduce the cookbook locally

<details>
You can now reproduce the book (requires quarto to be installed):

```bash
quarto preview ./src/afcharts/cookbook/
```

</details>

### Installing pre-commit hooks

<details>
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

</details>

### Ruff

<details>
Github actions automatically formats code using ruff.

If you are using 'VS Code' IDE ensure that you change your formater in order to reduce style conflicts.

```plain
# Open the preferences
'Ctrl+,'

Search for 'Default Formatter' and change it to 'ruff'
```

</details>
