# Release Guide

This document explains how to publish a new version of **afcharts** to PyPI.

## How the system works

Publishing is handled by a GitHub Actions workflow
(`.github/workflows/publish.yml`) triggered by GitHub Releases. The workflow
uses two types of release to route packages to the right registry:

| GitHub Release type | Publishes to | Purpose |
|---|---|---|
| **Pre-release** | TestPyPI | Test that the package builds, uploads, and installs correctly |
| **Full release** | PyPI | Publish the final, verified version for users to install |

The typical flow is:

1. Create a **pre-release** on the release branch → the workflow publishes
   to TestPyPI and automatically verifies the package can be installed and
   imported.
2. Once satisfied, squash-merge the release branch into `main`.
3. Create a **full release** from `main` → the workflow publishes to PyPI
   (after confirming a matching version exists on TestPyPI).

```
  Pre-release (release branch)       Full release (main)
        │                                    │
        ▼                                    ▼
  ┌───────────┐  ✅ verified          ┌─────────────┐
  │  TestPyPI │ ── squash merge ──►   │    PyPI     │
  └───────────┘    to main            └─────────────┘
    (automated                          (safety check
     install +                           confirms version
     import test)                        exists on TestPyPI)
```

### Safety checks

The workflow includes two safeguards to prevent broken or untested packages
reaching PyPI:

1. **Automated verification** — after publishing to TestPyPI, the workflow
   installs the package from TestPyPI and runs `import afcharts` to confirm
   it works.
2. **TestPyPI existence check** — before publishing to PyPI, the workflow
   queries the TestPyPI API to confirm a matching version was previously
   published there. If no match is found, the PyPI publish is blocked.

---

## Prerequisites

Before starting a release, ensure you have:

- **Write access** to the repository (to create branches, tags, and releases)
- **GitHub environments** configured:
  - `testpypi` — linked to the TestPyPI trusted publisher
  - `pypi` — linked to the PyPI trusted publisher
- The version number you intend to release following
  [PEP 440](https://peps.python.org/pep-0440/) e.g. `1.2.0`. See [Version Numbering (py-pkgs.org)](https://py-pkgs.org/07-releasing-versioning#version-numbering) for a guide.

---

## Step-by-step release process

### 1. Create a release branch

Create a new branch from `dev` for the release:

```bash
git checkout dev
git pull origin dev
git checkout -b release/v1.2.0
```

### 2. Bump the version number

Update the `version` field in `pyproject.toml` to a **release candidate**
version (`1.2.0rc1`). This is needed because TestPyPI does not allow uploading the same
version twice — using RC versions lets you iterate if something goes wrong.

```toml
# pyproject.toml
[project]
version = "1.2.0rc1"
```

Commit and push:

```bash
git add pyproject.toml
git commit -m "build(release): bump version to 1.2.0rc1"
git push origin release/v1.2.0
```

### 3. Create a GitHub pre-release

1. Go to the repository on GitHub → **Releases** → **Draft a new release**
2. Click **Choose a tag** and type `v1.2.0rc1` (with "v" prefix) → select **Create new tag**
3. **Target**: the `release/v1.2.0` branch
4. **Title**: `afcharts 1.2.0rc1`
5. **Description**: Brief summary (e.g. "Release candidate for v1.2.0") and list of changes since previous release
6. ⚠️ **Check the "Set as a pre-release" box** ← this is critical ⚠️
7. Click **Publish release**

This triggers the workflow, which will:

- Build the package
- Publish `afcharts 1.2.0rc1` to TestPyPI
- Install it from TestPyPI and verify the import works

### 4. Check the workflow result

Go to the repository's **Actions** tab and find the workflow run triggered by
your pre-release. Check that all three jobs succeeded:

- ✅ `build-package`
- ✅ `Publish to TestPyPI`
- ✅ `Verify TestPyPI installation`

**If the verification failed**, see [Troubleshooting](#troubleshooting) below.

### 5. Check TestPyPI

Go to the [afcharts TestPyPI page](https://test.pypi.org/p/afcharts) and confirm that:
1. the new package version shows as a pre-release in 'Release history'
2. on clicking the pre-release version, the project description is accurate and the images are displayed correctly

### 6. Set the final version

Once you are satisfied with the RC, update `pyproject.toml` to the final
version:

```toml
[project]
version = "1.2.0"
```

Commit and push:

```bash
git add pyproject.toml
git commit -m "build(release): bump version to 1.2.0"
git push origin release/v1.2.0
```

### 7. Open pull requests

Open PRs from the release branch into **both** `main` and `dev`:

- `release/v1.2.0` → `main`
- `release/v1.2.0` → `dev`

Get them reviewed and **squash-merge** both.

### 8. Create a full release from main

1. Go to the repository on GitHub → **Releases** → **Draft a new release**
2. Click **Choose a tag** and type `v1.2.0` → select **Create new tag**
3. **Target**: `main`
4. **Title**: `afcharts 1.2.0`
5. **Description**: List of changes since previous release
6. Check **"Set as the latest release"**
7. **Do NOT** check "Set as a pre-release"
8. Click **Publish release**

This triggers the workflow, which will:

- Run the **safety check** (confirms a version matching `1.2.0` — including
  `1.2.0rc1`, `1.2.0rc2`, etc. — exists on TestPyPI)
- Build the package from the tagged commit on `main`
- Publish `afcharts 1.2.0` to **PyPI**

### 9. Verify the PyPI publication

After the workflow completes, confirm the package is live:

```bash
pip install afcharts==1.2.0
python -c "import afcharts; print('Success!')"
```

You can also check https://pypi.org/project/afcharts/ in your browser.

---

## Troubleshooting

### TestPyPI verification failed

The automated verification installs the package from TestPyPI and tries to
import it. Common reasons for failure:

| Problem | Solution |
|---|---|
| **Index propagation delay** | The workflow retries 3 times with 30-second waits. If it still fails, wait a few minutes and re-run the failed workflow from the Actions tab. |
| **Missing dependency on TestPyPI** | TestPyPI may not have all dependencies. The workflow uses `--extra-index-url https://pypi.org/simple/` to fall back to PyPI for dependencies, but if a dependency is misconfigured this can still fail. Check your `dependencies` in `pyproject.toml`. |
| **Import error** | The package built but cannot be imported — likely a packaging issue (e.g. missing `__init__.py`, incorrect package discovery). Fix the issue, bump the RC number, and create a new pre-release. |

### Safety check blocked the PyPI publish

The safety check queries TestPyPI for any version matching the base version
number (e.g. for `1.2.0`, it looks for `1.2.0`, `1.2.0rc1`, `1.2.0rc2`,
etc.). If it fails:

- Ensure you completed steps 3–5 (publishing an RC pre-release to TestPyPI)
  before creating the full release from `main`.
- Check https://test.pypi.org/project/afcharts/ to see which versions are
  available.

### I need to iterate on a failed RC

TestPyPI does not allow uploading the same version twice. To retry:

1. Bump the RC number in `pyproject.toml` (e.g. `1.2.0rc1` → `1.2.0rc2`)
2. Commit and push to the release branch
3. Create a new GitHub pre-release with the updated tag (e.g. `v1.2.0rc2`)

### I accidentally created a full release before verifying on TestPyPI

The safety check will block the PyPI publish if no matching version exists on
TestPyPI. To fix:

1. Delete the release (and its tag) from GitHub
2. Follow the process from step 2 (create an RC pre-release first)

---

## Quick reference

```
git checkout dev && git pull
git checkout -b release/v1.2.0
# Edit pyproject.toml: version = "1.2.0rc1"
git add pyproject.toml && git commit -m "build(release): bump version to 1.2.0rc1"
git push origin release/v1.2.0

# → Create GitHub pre-release (tag: v1.2.0rc1, target: release/v1.2.0)
# → Wait for workflow to pass
# → Fix & iterate with rc2, rc3... if needed

# Edit pyproject.toml: version = "1.2.0"
git add pyproject.toml && git commit -m "build(release): bump version to 1.2.0"
git push origin release/v1.2.0

# → Open PRs: release/v1.2.0 → main, release/v1.2.0 → dev
# → Squash-merge both PRs

# → Create full release from main (tag: v1.2.0, target: main)
# → Workflow publishes to PyPI
```
