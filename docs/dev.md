# Development

## Prerequisites

- Python 3.10+
- [pipx](https://pipx.pypa.io/) (optional, for isolated installs)

## Setup

```bash
git clone https://github.com/KnowOneActual/tach_cli
cd tach_cli
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
pre-commit install
```

## Run locally

```bash
tach --help
tach timer -M 5
tach clock
```

## Lint & format

```bash
ruff check .
ruff format .
```

## Tests

```bash
pytest
```

## Commit style

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add overtime counter display
fix: handle terminal resize on macOS
docs: update usage examples
refactor: extract threshold logic to own module
```

## Releasing

1. Bump `version` in `pyproject.toml` and `src/tach_cli/__init__.py`.
2. Update `CHANGELOG.md` — move `Unreleased` items to the new version block.
3. Commit: `chore: release vX.Y.Z`
4. Tag: `git tag vX.Y.Z && git push --tags`
