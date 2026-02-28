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

## Internal Architecture

- `src/tach_cli/models.py` — Dataclasses for `Config` and `TimerSpec`.
- `src/tach_cli/config.py` — Logic for loading and parsing TOML configuration.
- `src/tach_cli/app.py` — The Textual application and custom widgets.
- `src/tach_cli/cli.py` — Typer subcommands that instantiate and run the app.

## Run locally
...
```bash
tach --help
tach timer -M 5
tach clock
```

## Lint & format

```bash
# Check for lint issues
ruff check .

# Auto-fix lint issues
ruff check . --fix

# Format code
ruff format .

# Check formatting without writing changes (useful in CI)
ruff format --check .
```

### Rule sets enabled

| Code | Source | What it catches |
|------|--------|------------------|
| `E`/`W` | pycodestyle | Style errors and warnings |
| `F` | pyflakes | Undefined names, unused imports |
| `I` | isort | Import ordering |
| `UP` | pyupgrade | Outdated syntax patterns |
| `B` | bugbear | Likely bugs and design issues |
| `SIM` | simplify | Overly complex expressions |
| `C4` | comprehensions | Suboptimal list/dict/set comprehensions |
| `N` | pep8-naming | Naming convention violations |
| `PTH` | use-pathlib | `os.path` → `pathlib.Path` |
| `RUF` | Ruff-specific | Miscellaneous improvements |
| `TC` | type-checking | Type-only import placement |
| `TID` | tidy-imports | Bans parent-relative imports |

### Notable ignores

- `E501` — line length is enforced by the formatter, not the linter
- `B008` — Typer uses function calls (`typer.Option(...)`) as default arguments by design

## Tests

```bash
pytest
pytest -v          # verbose
pytest -x          # stop on first failure
```

## Commit style

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add overtime counter display
fix: terminal resize crash on macOS
docs: update usage examples
refactor: extract threshold logic to own module
chore: bump dependencies
```

## Releasing

1. Bump `version` in `pyproject.toml` and `src/tach_cli/__init__.py`.
2. Update `CHANGELOG.md` — move `Unreleased` items to the new version block.
3. Commit: `chore: release vX.Y.Z`
4. Tag: `git tag vX.Y.Z && git push --tags`
