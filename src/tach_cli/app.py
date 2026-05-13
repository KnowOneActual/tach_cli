from __future__ import annotations

from datetime import datetime
from typing import Any, ClassVar

from rich.text import Text
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Digits, Footer, Header

from .config import load_config
from .models import Config, TimerSpec


class TachApp(App[None]):
    """The main Tach CLI application."""

    BINDINGS: ClassVar[Any] = [
        ("p", "toggle_pause", "Pause/Resume"),
        ("r", "reset", "Reset"),
        ("ctrl+r", "reload_config", "Reload Config"),
        ("q", "quit", "Quit"),
    ]

    CSS = """
    TachApp {
        align: center middle;
    }
    #timer {
        height: 1fr;
        width: 100%;
        content-align: center middle;
    }
    """

    remaining = reactive(0.0)
    is_paused = reactive(False)
    is_clock_mode = reactive(False)
    timer_display: Digits

    def __init__(
        self,
        spec: TimerSpec | None = None,
        clock_mode: bool = False,
        config: Config | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.spec = spec
        self.is_clock_mode = clock_mode
        self.config = config or Config()

        if spec:
            self.remaining = float(spec.total_seconds)
            self.initial_seconds = float(spec.total_seconds)

    def compose(self) -> ComposeResult:
        yield Header()
        # Using Digits for a segment-like look, which auto-scales horizontally.
        yield Digits(id="timer")
        yield Footer()

    def on_mount(self) -> None:
        """Start the update timer."""
        self.timer_display = self.query_one(Digits)
        self._apply_config()

        if not self.is_clock_mode:
            self._update_timer_display()

        self.set_interval(1 / 10, self.update_time)

    def _apply_config(self) -> None:
        """Apply the current configuration to the UI."""
        if self.config.general.bold:
            self.timer_display.styles.text_style = "bold"
        else:
            self.timer_display.styles.text_style = "none"

        # Apply alignment from config
        h_align = self.config.position.horizontal
        v_align = self.config.position.vertical

        # Textual uses 'middle' for vertical center alignment
        if v_align == "center":
            v_align = "middle"

        try:
            self.styles.align_horizontal = h_align  # type: ignore[assignment]
            self.styles.align_vertical = v_align  # type: ignore[assignment]
        except Exception:
            # Fallback to center middle if config is invalid
            self.styles.align_horizontal = "center"
            self.styles.align_vertical = "middle"

    def update_time(self) -> None:
        """Update the time display."""
        if self.is_clock_mode:
            now = datetime.now()
            self.timer_display.update(now.strftime("%H:%M:%S"))
            return

        if not self.is_paused:
            self.remaining -= 0.1
            if self.remaining <= 0 and self.spec and self.spec.kill:
                self.exit()

        self._update_timer_display()

    def _update_timer_display(self) -> None:
        """Update the timer display with colors and overtime logic."""
        abs_remaining = abs(int(self.remaining))
        hh, mm = divmod(abs_remaining, 3600)
        mm, ss = divmod(mm, 60)

        # Build string
        parts = []
        if hh > 0:
            parts.append(f"{hh:02d}")
        parts.append(f"{mm:02d}")
        parts.append(f"{ss:02d}")
        time_str = ":".join(parts)

        if self.remaining < 0:
            time_str = f"-{time_str}"

        # Determine color based on thresholds from config
        thresholds = self.config.thresholds
        color = "green"

        if self.remaining <= 0:
            # Overtime logic
            if self.remaining > -thresholds.soft_overrun:
                color = "magenta"  # Soft overrun
            else:
                color = "red"      # Hard overrun
        elif self.remaining <= thresholds.red:
            color = "red"
        elif self.remaining <= thresholds.yellow:
            color = "yellow"

        self.timer_display.update(time_str)
        self.timer_display.styles.color = color

    def action_toggle_pause(self) -> None:
        """Toggle the pause state."""
        if not self.is_clock_mode:
            self.is_paused = not self.is_paused

    def action_reset(self) -> None:
        """Reset the timer to its initial value."""
        if not self.is_clock_mode and self.spec:
            self.remaining = float(self.spec.total_seconds)
            self.is_paused = False

    def action_reload_config(self) -> None:
        """Reload the configuration and re-apply styles."""
        self.config = load_config()
        self._apply_config()
        if not self.is_clock_mode:
            self._update_timer_display()
        self.notify("Configuration reloaded")

    def action_quit(self) -> None:  # type: ignore[override]
        """Quit the application."""
        self.exit()
