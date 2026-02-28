from __future__ import annotations

from datetime import datetime
from typing import ClassVar

from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widgets import Digits, Footer, Header, Static

from .models import Config, TimerSpec


class TimeDisplay(Static):
    """A large auto-scaling time display."""

    DEFAULT_CSS = """
    TimeDisplay {
        content-align: center middle;
        text-style: bold;
        height: 1fr;
        width: 100%;
    }
    """

    value = reactive("")

    def render(self) -> Text:
        return Text(self.value)


class TachApp(App[None]):
    """The main Tach CLI application."""

    BINDINGS: ClassVar[list[Binding | tuple[str, str, str]]] = [
        ("p", "toggle_pause", "Pause/Resume"),
        ("r", "reset", "Reset"),
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

    def __init__(
        self,
        spec: TimerSpec | None = None,
        clock_mode: bool = False,
        config: Config | None = None,
        **kwargs,
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
        display = self.query_one(Digits)
        if self.config.general.bold:
            display.styles.text_style = "bold"

        self.set_interval(1 / 10, self.update_time)

    def update_time(self) -> None:
        """Update the time display."""
        if self.is_clock_mode:
            now = datetime.now()
            self.query_one(Digits).update(now.strftime("%H:%M:%S"))
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

        if self.remaining < 0 or self.remaining <= thresholds.red:
            color = "red"
        elif self.remaining <= thresholds.yellow:
            color = "yellow"

        display = self.query_one(Digits)
        display.update(time_str)
        display.styles.color = color

    def action_toggle_pause(self) -> None:
        """Toggle the pause state."""
        if not self.is_clock_mode:
            self.is_paused = not self.is_paused

    def action_reset(self) -> None:
        """Reset the timer to its initial value."""
        if not self.is_clock_mode and self.spec:
            self.remaining = float(self.spec.total_seconds)
            self.is_paused = False

    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()
