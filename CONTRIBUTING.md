# Contributing to Tach CLI

Thanks for your interest! Tach is a lightweight terminal clock + countdown timer built for **live productions, events, and structured meetings**. The core goal is simple visual pacing — big readable time, threshold color shifts, overtime counter — with aggressive anti-feature-creep.

## Scope first

Before opening a PR, make sure the change fits:

- ✅ Countdown timer / clock display improvements
- ✅ Color threshold and overtime behavior
- ✅ Auto-scaling text and terminal resize handling
- ✅ Keyboard controls (pause, reset, adjust)
- ✅ TOML config and CLI flag improvements
- ❌ Complex menus or settings screens
- ❌ Data logging or analytics
- ❌ OS-level notification integrations

Not sure? Open an issue first.

## Getting started

```bash
git clone https://github.com/KnowOneActual/tach_cli
cd tach_cli
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

See [docs/dev.md](docs/dev.md) for full development setup.

## Workflow

1. Open or find an issue describing the change.
2. Fork the repo and create a branch: `git checkout -b feat/your-feature`.
3. Make your changes.
4. Run `ruff check .`, `ruff format .`, and `pytest` — all must pass.
5. Open a PR using the PR template.

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add overtime counter
fix: terminal resize crash on macOS
docs: update config examples
refactor: extract threshold logic
chore: bump dependencies
```

## Changelog

Add a line to the `Unreleased` section of `CHANGELOG.md` for every user-visible change. Use [Keep a Changelog](https://keepachangelog.com/) categories: `Added`, `Changed`, `Fixed`, `Removed`.

## Code style

- Python 3.10+
- Ruff for lint and format (config in `pyproject.toml`)
- Clarity over cleverness — this tool runs in high-stress live environments
