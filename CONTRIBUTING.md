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
9. If you are merging `dev` to `main`, you must increment the version number
by merging the automatically created `release-please` PR, which will also produce the change log for the new version release etc.
represent. The versioning scheme we use is [SemVer](http://semver.org/).

### Conventional commit PR titles

When you raise a pull request (PR), please ensure the PR title follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#specification) format (see [guidance gist](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#examples)).

By using conventional commits, commit logs are easier to read and the [`release-please`](https://github.com/googleapis/release-please) github action workflow can automate building of change logs and tagging and increasing of new version numbers.

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

### Major version number increments

A PR that introduces breaking changes (i.e. affects backwards compatibility) must be indicated by an `!` before the `:` in the subject line e.g. `feat(api)!: change func call signature`.
This will inform release-please to increment the *major* (e.g. `1.7` -> `2.0`) version number instead of the *minor* version number (e.g. `1.7` -> `1.8`) in the next release.
Breaking changes should be described in the squash commit footer section, if the commit description isn't sufficiently informative

---

## Basic folder structure

```plaintext
afcharts-py/
│
├── src/
│   └── afcharts/
│       ├── __init__.py
│       ├── theme_af.py
│       └── assets/
│           ├── af_colours.py
│           └── pio_template.py
│       └── cookbook/
│           ├── af_colours.py
│           └── pio_template.py
│
├── tests/
│   ├── conftest.py
│   └── test_module.py
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── pyproject.toml
└── .gitignore
```

### Explanation of Each Component

- **`src/afcharts/`**: Main package folder. All your code should go here. Using a `src` layout helps avoid import issues during development and testing.
  - `__init__.py`: Makes the directory a Python package.

- **`tests/`**: Contains unit tests.

- **`README.md`**: A markdown file describing your package, how to install and use it.

- **`pyproject.toml`**: The modern configuration file for building and packaging Python projects. It replaces `setup.py` and `setup.cfg`.

- **`.gitignore`**: Specifies files and directories to ignore in version control (e.g., `__pycache__/`, `.DS_Store`, etc.).

----

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
pip install -e .[dev,test]
```

This assumes you already have a python virtual environment set up with your preferred tool (`conda`/`virtualenv`/`uv` etc.).

### Testing

To test your installation, run `pytest` to confirm all unit tests pass successfully in your environment:

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
