# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Core **Textual TUI** implementation for `timer` and `clock` commands.
- Large, auto-scaling `Digits` display with segment-like aesthetics.
- Production pacing colors: Green → Yellow → Red shifts based on thresholds.
- Overtime counter that turns red and counts negative after zero.
- Keyboard controls: `P` (Pause), `R` (Reset), `Q` (Quit).
- **TOML Configuration** support with platform-specific default locations.
- Support for **Named Profiles** via `--profile` flag.
- `TACH_CONF` environment variable for configuration path override.
- New dependencies: `platformdirs` and `tomli`.
- Modular internal structure: `models.py`, `app.py`, `config.py`.
- Comprehensive configuration and logic tests.

### Changed
- CLI subcommands integrated with Textual app lifecycle.
- Timer defaults to 5 minutes when no arguments provided.
- `TC` (Type Checking) Ruff rule prefix updated from `TCH`.

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
