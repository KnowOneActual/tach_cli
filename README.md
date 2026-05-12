# Tach CLI

> [!NOTE]
> Tach is still in active design and early development. Things may change quickly and break often. If you're trying it out, expect sharp edges and unstable behavior for now.

A lightweight terminal application designed to keep time during live productions, events, and structured meetings. Tach is a distraction-free countdown timer and clock built to help you manage pace without breaking focus.

## Quick Look

```bash
tach timer --minutes 30        # Start a 30-minute countdown
tach timer -M 1 -S 30          # Timer for 1 minute and 30 seconds
tach timer --profile quick     # Use a predefined profile from config
tach timer -M 45 --kill        # Exit automatically when time expires
tach clock                     # Display the current time of day
```

## What Makes Tach Different

Most terminal clocks are built for ambient display. Tach is built for **production pacing**:

- **Color-shifting countdown** — text shifts Green → Yellow → Red as time runs out
- **Overtime counter** — when the clock hits zero, it keeps going in red negative numbers
- **Auto-scaling text** — the display fills the terminal and resizes live
- **Production-first controls** — pause, reset, and quit via keyboard

## Status

| Feature | Status |
|---|---|
| Core timer display | ✅ |
| Clock mode | ✅ |
| Color threshold shifts | ✅ |
| Overtime counter | ✅ |
| Subcommand CLI | ✅ |
| TOML config file | ✅ |
| Named profiles | ✅ |
| Security lint rules | ✅ |
| mypy strict type checking | ✅ |
| CI coverage + security scan | ✅ |
| Position controls in TUI | 🔲 |
| Config hot-reload (Ctrl+R) | 🔲 |
| Soft overrun visual | 🔲 |
| Shell completions | 🔲 |
| Time nudge keys | 🔲 |

## Stack

| Component | Tool |
|---|---|
| Language | Python 3.10+ |
| TUI | [Textual](https://github.com/Textualize/textual) |
| Styling | [Rich](https://github.com/Textualize/rich) |
| CLI | [Typer](https://typer.tiangolo.com/) |
| Config | TOML |
| Lint/Format | [Ruff](https://docs.astral.sh/ruff/) |
| Types | [mypy](https://mypy.readthedocs.io/) (strict) |
| Security | bandit + pip-audit |
| Tests | pytest + pytest-cov |

## Contributing

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install

# Quality gates
ruff check .              # lint
ruff format --check .     # format
mypy src/                 # type check
pytest --cov              # tests + coverage
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines and the [roadmap](roadmap.md) for planned work.
