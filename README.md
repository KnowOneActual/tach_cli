# Tach CLI

A lightweight terminal application designed to keep time during live productions, events, and structured meetings. Tach is a distraction-free countdown timer and clock built to help you manage pace without breaking focus.

> [!IMPORTANT]
> Tach is currently in active planning and early development. It is a personal project, so development may take time. There is also a chance it remains a concept and does not move forward — but the groundwork is being laid with real intent.

## Quick Look

```
tach timer --minutes 30        # Start a 30-minute countdown
tach timer -M 1 -S 30          # Timer for 1 minute and 30 seconds
tach timer --minutes 45 --kill # Exit automatically when time expires
tach clock                     # Display the current time of day
```

## What Makes Tach Different

Most terminal clocks are built for ambient display. Tach is built for **production pacing**:

- **Color-shifting countdown** — text shifts Green → Yellow → Red as time runs out
- **Overtime counter** — when the clock hits zero, it keeps going in red negative numbers
- **Auto-scaling text** — the display fills the terminal and resizes live
- **Production-first controls** — pause, reset, and time adjustments via keyboard

## Status

| Feature | Status |
|---|---|
| Core timer display | 🔲 Planned |
| Clock mode | 🔲 Planned |
| Color threshold shifts | 🔲 Planned |
| Overtime counter | 🔲 Planned |
| Subcommand CLI | 🔲 Planned |
| TOML config file | 🔲 Planned |
| Shell completions | 🔲 Planned |

## Stack

- **Language:** Python
- **UI Framework:** [Textual](https://github.com/Textualize/textual) — handles responsive terminal layouts and resizing
- **Styling:** [Rich](https://github.com/Textualize/rich) — handles color formatting and text styling
- **CLI:** [Typer](https://typer.tiangolo.com/) — subcommand structure and argument parsing

## Contributing

If you have suggestions, feature ideas, or thoughts on how to make this tool better, open an issue or start a discussion. All ideas are welcome.
