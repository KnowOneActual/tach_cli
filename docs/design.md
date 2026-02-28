# Design

## Core principle

Tach is a **production-first** timer, not an ambient clock widget. It is built for live events, broadcasts, and structured meetings where pacing matters.

The primary design frame is a **solo operator or small crew in a control room** running a live show. The operator is glancing at Tach while juggling switching, playback, graphics, and comms.

## Design decisions

- **Color shifts over competing alerts** — Green → Yellow → Red communicates urgency at a glance, no popups or sounds needed.
- **Overtime counter** — When time expires, the clock continues into negative numbers in red. This is the #1 differentiator vs. other terminal clocks.
- **Auto-scaling text** — The display fills the terminal window and adapts live on resize.
- **No menus or data logging** — The terminal emulator handles transparency and borders. Tach only manages time.

## Constraints & non-goals

- **One main segment at a time** — Tach may know about a list of segments, but shows a single primary timer. It is not a rundown editor.
- **Local-only in early versions** — No networking, OSC, or HTTP APIs in the MVP. All timing logic runs locally in a single terminal session.
- **Minimal persistence** — At most, optional one-shot post-show summaries. No long-term dashboards.
- **No talent-facing UX yet** — Initial focus is on the control room. Talent displays and “calm” modes come later.

## Future directions (informed by today’s pain points)

These are explicitly **later-phase** ideas that the core design should remain compatible with:

- **Profiles and pacing styles** — Named profiles (e.g., "talkshow", "panel") with different thresholds and overrun expectations.
- **Soft overrun semantics** — A configurable window where overtime is visually distinct but not yet “panic” mode.
- **Calm vs. control-room palettes** — Different color schemes for talent vs. operator views.
- **Time nudge keys and panic extensions** — Fast `+30s`, `+2m` adjustments and “extend segment” shortcuts.
- **Lightweight session summaries** — Simple textual recaps (planned vs. actual per segment, total overtime).
- **Headless core + OSC/API integration** — A future layer that exposes the timing state via OSC or a small API so Tach can drive lights, sound cues, overlays, or other systems.

## Inspiration

- [clock-rs](https://github.com/Oughie/clock-rs) — subcommand CLI pattern, `--kill` flag, TOML config
- [tty-clock](https://github.com/xorg62/tty-clock) — minimal terminal clock lineage
- [Textual](https://github.com/Textualize/textual) — responsive TUI layout framework
