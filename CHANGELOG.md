# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- `pyproject.toml` with Hatchling build backend, PEP 621 metadata, and Ruff config.
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

### Changed
- `CONTRIBUTING.md` rewritten to reflect subcommand CLI, Conventional Commits, and Keep a Changelog workflow.
- `README.md` updated with usage examples, status table, and updated stack (added Typer).
- `roadmap.md` updated with subcommand CLI design, TOML config schema, `--kill` flag, and 4-phase development plan.
