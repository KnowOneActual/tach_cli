# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- **Time Nudge Keys** and **Vim-style keybindings** for adjusting the remaining time (+/- 30s, 2m, 5m).
- **Shell Completions** for Bash, Zsh, and Fish via Typer.
- **Post-show Session Summary** printed via the `--summary` flag on the `timer` command.
- **Config hot-reload** (`Ctrl+R`) to re-apply styles and reload TOML without restarting.
- **Soft overrun** visual state: the timer turns Magenta during the initial overtime window.
- Support for **TUI alignment** (horizontal/vertical) via the `[position]` config section.
- Async **TUI test suite** using `textual.pilot` and `pytest-asyncio`.
- **CLI test suite** using `typer.testing.CliRunner` and mocks.
- 100% test coverage for `cli.py` and `app.py` (excluding platform-specific `tomllib` fallbacks).

### Changed
- **Performance Optimization**: Cached `Digits` widget reference in `on_mount` to reduce lookup overhead.
- Refactored `cli.py` duration logic to ensure CLI flags act as explicit overrides for profiles.
- Updated `on_mount` to initialize the timer display immediately, preventing "white flicker".
- Mapped `center` vertical position to Textual's internal `middle` value for better UX.

### Security & Tooling
- Added `pytest-asyncio` to development dependencies.
- Renamed internal `display` attribute in `TachApp` to `timer_display` to avoid collision with base `App.display`.
- Ruff security rules added: `S` (bandit), `TRY`, `T20`, `FA`.
- `mypy` strict type checking wired into pre-commit + CI.
- CI matrix extended to Python 3.10–3.13 with pip caching.
- `pytest-cov` coverage reporting with Codecov upload.
- Dedicated CI `security` job: `bandit` SAST + `pip-audit` dependency scan.
- Pre-commit hardened: `detect-private-key`, `check-ast`, `check-json`, mypy.
- `pyproject.toml`: classifiers, project URLs, keywords, mypy + coverage config.
- `config.py`: bare `except Exception` replaced with targeted catch + structured logging.
- `app.py`: fixed mypy strict-mode violations (BINDINGS, kwargs, action_quit override).

---

## [0.0.0] — scaffolding

### Added
- `pyproject.toml` with Hatchling build backend, PEP 621 metadata, and basic Ruff config.
- `src/tach_cli/` package skeleton: `__init__.py`, `__main__.py`, and stub `cli.py` with `timer` and `clock` subcommands.
- `tests/` with smoke tests for imports and `TimerSpec` math.
- `docs/` directory: `usage.md`, `config.md`, `design.md`, `dev.md`.
- `examples/conf.toml` starter configuration.
- `.pre-commit-config.yaml` with Ruff (lint + format) and pre-commit-hooks.
- `.editorconfig` for consistent whitespace across editors.
- `.github/workflows/ci.yml` — CI matrix across Python 3.10, 3.11, 3.12.
- GitHub issue templates: bug report and feature request (with production-scope check).
- GitHub PR template.
- `CODE_OF_CONDUCT.md` and `SECURITY.md`.
- `CONTRIBUTING.md` rewritten to reflect subcommand CLI, Conventional Commits, and Keep a Changelog workflow.
- `README.md` updated with usage examples, status table, and updated stack.
- `roadmap.md` updated with subcommand CLI design, TOML config schema, `--kill` flag, and 4-phase development plan.
