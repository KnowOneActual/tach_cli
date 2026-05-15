# Tach CLI — Roadmap

## Project Description

A lightweight terminal application designed for live productions, events, and structured meetings. Tach provides a distraction-free timekeeping tool with a highly visible, auto-scaling display that toggles between a countdown timer and a standard clock.

---

## Design Philosophy

Built using Framestorming and Musk's 5-Step Process to solve the core problem of maintaining perfect pacing without breaking focus, while aggressively avoiding feature creep.

- **Question the Frame:** Simple visual communication. Color shifts (Green → Yellow → Red) replace competing alerts.
- **Delete the Unnecessary:** No complex menus, data logging, or OS-level window hacking. The terminal emulator handles transparency and borderless modes.
- **Simplify and Optimize:** Core logic is large text that counts down, changes color, and goes negative for overtime.

---

## Design Constraints & Non-Goals

Tach is intentionally opinionated. To keep the tool sharp for live production use, the following constraints apply:

- **Single primary timer view** — one main segment at a time. Future versions might preview "next segment," but Tach is not a full rundown editor.
- **Production control room first** — optimized for a solo operator or small crew in a control room; talent-facing displays are a later concern.
- **No networking in the MVP** — no OSC, HTTP, or multi-machine sync yet. Those are future integrations built on a solid local timing core.
- **No persistent analytics** — no history dashboards or metrics. At most, an optional post-show summary.
- **No visual noise** — no flashing by default, no animations that distract from content.

These constraints should be treated as guardrails when proposing new features.

---

## CLI Design

Tach uses a subcommand structure for clean, intuitive usage:

```
Usage: tach [COMMAND] [OPTIONS]

Commands:
  timer      Start a countdown timer (default: 5 minutes)
  clock      Display the current time of day
  help       Print help

Options (timer):
  -M, --minutes <MINUTES>  Add minutes to the timer
  -S, --seconds <SECONDS>  Add seconds to the timer
  -H, --hours <HOURS>      Add hours to the timer
      --kill               Exit automatically when the timer finishes
  -p, --profile <NAME>     Use a named profile from the config
  -h, --help               Print help
```

Time units auto-convert, so `tach timer -M 90` starts a 1h 30m timer.

---

## Core Features (MVP)

- Auto-scaling text that adjusts when the terminal is resized
- Subcommand CLI: `tach timer`, `tach clock`
- Flexible time input with `-M`, `-S`, `-H` flags and auto-conversion
- Text color shifts based on time remaining: Green → Yellow → Red
- Overtime counter — turns red and counts into negative numbers when time expires
- `--kill` flag to terminate automatically when the timer finishes
- Keyboard controls: pause, reset, and quit
- Named profiles via `--profile` flag
- TOML configuration file with platform-specific default paths

---

## Configuration

Tach uses a TOML configuration file for persistent settings, with CLI flags overriding on a per-run basis.

```toml
[general]
bold = true

[position]
horizontal = "center"
vertical = "center"

[thresholds]
yellow = 300   # 5 minutes — switch to yellow
red = 120      # 2 minutes — switch to red
soft_overrun = 120  # first 2 minutes of overtime are "soft" (pending UI)

[profiles]
standard = 1800   # 30 min
quick = 300       # 5 min
lightning = 120   # 2 min
```

Config hot-reload via `Ctrl+R` is planned.

---

## Development Roadmap

### Phase 1: Core Display & CLI — ✅ COMPLETED
Python project set up with Typer subcommand CLI. Timer and clock display via Textual. `-M`/`-S`/`-H` flags and `--kill` flag. Basic pause/reset controls.

### Phase 2: Visual Pacing & Overtime — ✅ COMPLETED
Color threshold logic (Green → Yellow → Red). Red overtime count-up. Auto-scaling text on window resize.

### Phase 3: Configuration — ✅ COMPLETED
TOML config file loading with CLI overrides. Multi-profile support via `--profile`.

### Phase 3.5: Security & Developer Workflow — ✅ COMPLETED
- Ruff security lint rules (`S`, `TRY`, `T20`, `FA`)
- `mypy` strict type checking wired into pre-commit and CI
- CI matrix extended to Python 3.10–3.13
- Coverage tracking with `pytest-cov` and Codecov
- Dedicated CI security scan job: `bandit` SAST + `pip-audit` dependency audit
- Pre-commit: `detect-private-key`, `check-ast`, `check-json` hooks
- Structured logging replacing bare `except Exception` in config loader
- `pyproject.toml` project metadata (classifiers, URLs, keywords)

### Phase 4: Hardening — ✅ COMPLETED
- Expand test coverage (currently 98%): added `tests/test_app.py` (Textual pilot), `tests/test_cli.py` (Typer CliRunner), and mocked error paths
- Implement `position` config support in TUI
- Implement config `Ctrl+R` hot-reload
- Implement `soft_overrun` visual distinction (Magenta)
- Cache `Digits` widget reference in `on_mount` for performance
- Clean up dead code in `cli.py` profile+flag interaction logic

### Phase 5: Advanced Controls — ✅ COMPLETED
- Time nudge keys (`+30s`, `+2m`, `+5m`)
- Vim-style keybindings for rapid home-row adjustments
- Shell completions for Bash, Zsh, and Fish
- Optional post-show session summary

### Phase 6: Polish & Release (Future)
- PyPI release workflow (build + publish on tag)
- Multi-OS CI matrix (macOS, Windows)
- Ratchet coverage gate from 0% → 50% → 70%
- `bandit` in pre-commit (currently CI-only)

### Phase 7: Integrations & Automation (Future)
Headless timing core with integration layer (OSC / HTTP) to drive external systems (audio cues, lighting, overlays). Only once the single-machine TUI is stable in real shows.

---

## Stack

| Component | Library | Why |
|---|---|---|
| Language | Python 3.10+ | Accessible, rapid iteration |
| UI Framework | [Textual](https://github.com/Textualize/textual) | Responsive TUI layouts and resizing |
| Styling | [Rich](https://github.com/Textualize/rich) | Color formatting and text styling |
| CLI | [Typer](https://typer.tiangolo.com/) | Subcommand structure, auto-generated help |
| Config | [TOML](https://toml.io/) | Human-readable, widely supported |
| Lint/Format | [Ruff](https://docs.astral.sh/ruff/) | Fast Python linter + formatter |
| Types | [mypy](https://mypy.readthedocs.io/) | Static type checking (strict mode) |
| Security | [bandit](https://bandit.readthedocs.io/) + [pip-audit](https://pypi.org/project/pip-audit/) | SAST + dependency scanning |
| Tests | [pytest](https://pytest.org/) + [pytest-cov](https://pytest-cov.readthedocs.io/) | Test runner + coverage |
