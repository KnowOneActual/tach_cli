# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Expanded Ruff lint rule set: `W`, `SIM`, `C4`, `N`, `PTH`, `RUF`, `TCH`, `TID`.
- `[tool.ruff.lint.per-file-ignores]` for test files (`S101`, `N802`).
- `[tool.ruff.lint.isort]` config: first-party package, combined-as imports.
- `[tool.ruff.lint.flake8-tidy-imports]` banning parent-relative imports.
- `[tool.ruff.lint.pep8-naming]` config for Textual/Typer classmethod conventions.
- `[tool.ruff.format]` expanded: `docstring-code-format`, `line-ending = lf`.
- `.pre-commit-config.yaml` expanded with `check-merge-conflict`, `check-added-large-files`, and `debug-statements` hooks.
- `docs/dev.md` updated with full Ruff rule reference table and notable ignores.

### Changed
- `B008` added to lint ignores (required by Typer's `Option`/`Argument` default pattern).
- `E501` moved to lint ignore (line length enforced by formatter only).

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
