# Tach CLI — Roadmap

## Project Description

A lightweight terminal application designed for live productions, events, and structured meetings. Tach provides a distraction-free timekeeping tool with a highly visible, auto-scaling display that toggles between a countdown timer and a standard clock.

---

## Design Philosophy

Built using Framestorming and Musk’s 5-Step Process to solve the core problem of maintaining perfect pacing without breaking focus, while aggressively avoiding feature creep.

- **Question the Frame:** Simple visual communication. Color shifts (Green → Yellow → Red) replace competing alerts.
- **Delete the Unnecessary:** No complex menus, data logging, or OS-level window hacking. The terminal emulator handles transparency and borderless modes.
- **Simplify and Optimize:** Core logic is large text that counts down, changes color, and goes negative for overtime.

---

## Design Constraints & Non-Goals

Tach is intentionally opinionated. To keep the tool sharp for live production use, the following constraints apply:

- **Single primary timer view** — one main segment at a time. Future versions might preview “next segment,” but Tach is not a full rundown editor.
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
  -h, --help               Print help
```

Time units auto-convert, so `tach timer -M 90` starts a 1h 30m timer.
A shell alias (`event 30`) can wrap the full command for quick launch.

---

## Core Features (MVP)

- Auto-scaling text that adjusts when the terminal is resized
- Subcommand CLI: `tach timer`, `tach clock`
- Flexible time input with `-M`, `-S`, `-H` flags and auto-conversion
- Text color shifts based on time remaining: Green → Yellow → Red
- Overtime counter — turns red and counts into negative numbers when time expires
- `--kill` flag to terminate automatically when the timer finishes
- Keyboard controls: pause, reset, and minute adjustments
- Quick launch via shell alias (e.g., `event 30`)

---

## Configuration

Tach will use a TOML configuration file for persistent settings, with CLI flags overriding on a per-run basis.

```toml
[general]
color = "green"
bold = true

[position]
horizontal = "center"
vertical = "center"

[thresholds]
yellow = 5   # Switch to yellow at 5 minutes remaining
red = 2      # Switch to red at 2 minutes remaining
soft_overrun = 2  # First 2 minutes of overtime are treated as “soft” overrun

[profiles]
standard = 30
quick = 5
lightning = 2
```

Config hot-reload will allow settings to update mid-session without restarting the app (`Ctrl+R`).

---

## Nice-to-Haves (Future Phases)

- Multi-profile loading via CLI flag (e.g., `tach timer --profile lightning`)
- Vim-style keybindings for rapid, home-row adjustments
- Global hotkeys to pause or adjust time even when the terminal is not focused
- Shell completions for Bash, Zsh, and Fish
- Time “nudge” keys for quickly adding or subtracting fixed amounts (e.g., `+30s`, `+2m`)
- Optional post-show “session summary” printed once when ending a run

---

## Future Considerations (Pending User Demand)

*Removed to keep the initial build lean, but can be revisited:*

- Subtle progress bar on the terminal edge
- Gentle flashing alerts at critical time milestones
- Built-in background transparency and borderless “true minimalist” mode
- Talent-facing “calm mode” palettes separate from control-room palettes
- OSC / API / headless control: a future integration layer so Tach’s timing core can drive external systems (e.g., audio cues, lighting, overlays) once the local TUI is battle-tested

---

## Development Roadmap

**Phase 1: Core Display & CLI**
Set up the Python project using Typer for the subcommand CLI. Build the timer and clock display with Textual. Accept `-M`/`-S`/`-H` flags and implement the `--kill` flag. Add basic pause and reset controls.

**Phase 2: Visual Pacing & Overtime**
Introduce color threshold logic (Green → Yellow → Red). Add the red overtime count-up, including `soft_overrun` handling. Ensure text auto-scales smoothly on window resize.

**Phase 3: Configuration**
Implement TOML config file loading with CLI overrides. Add `Ctrl+R` hot-reload. Build out multi-profile support and position controls.

**Phase 4: Advanced Controls (Optional)
**Implement time nudge keys, Vim-style keybindings, global hotkeys, and shell completion generation. Add optional post-show session summaries.

**Phase 5: Integrations & Automation (Future)**
Explore a headless timing core with an integration layer (OSC / simple HTTP / other protocols) that can trigger external systems. This phase only happens once the single-machine TUI is stable in real shows.

---

## Stack

| Component | Library | Why |
|---|---|---|
| Language | Python | Accessible, rapid iteration |
| UI Framework | [Textual](https://github.com/Textualize/textual) | Handles responsive TUI layouts and resizing |
| Styling | [Rich](https://github.com/Textualize/rich) | Color formatting and text styling |
| CLI | [Typer](https://typer.tiangolo.com/) | Subcommand structure, auto-generated help and completions |
| Config | [TOML](https://toml.io/) | Human-readable, widely supported |
