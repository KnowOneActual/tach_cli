# Design

## Core principle

Tach is a **production-first** timer, not an ambient clock widget. It is built for live events, broadcasts, and structured meetings where pacing matters.

## Design decisions

- **Color shifts over competing alerts** — Green → Yellow → Red communicates urgency at a glance, no popups or sounds needed.
- **Overtime counter** — When time expires, the clock continues into negative numbers in red. This is the #1 differentiator vs. other terminal clocks.
- **Auto-scaling text** — The display fills the terminal window and adapts live on resize.
- **No menus or data logging** — The terminal emulator handles transparency and borders. Tach only manages time.

## What we deliberately removed

- Complex settings screens
- Notification system integrations
- Multi-display or multi-window management
- Logging / analytics

## Inspiration

- [clock-rs](https://github.com/Oughie/clock-rs) — subcommand CLI pattern, `--kill` flag, TOML config
- [tty-clock](https://github.com/xorg62/tty-clock) — minimal terminal clock lineage
- [Textual](https://github.com/Textualize/textual) — responsive TUI layout framework
