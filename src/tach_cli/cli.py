from __future__ import annotations

from dataclasses import dataclass
import time

import typer

app = typer.Typer(add_completion=False, no_args_is_help=True)


@dataclass(frozen=True)
class TimerSpec:
    hours: int = 0
    minutes: int = 5
    seconds: int = 0
    kill: bool = False

    @property
    def total_seconds(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds


@app.command()
def clock() -> None:
    """Display the current time (placeholder; Textual UI comes next)."""
    typer.echo(time.strftime("%H:%M:%S"))


@app.command()
def timer(
    hours: int = typer.Option(0, "-H", "--hours", min=0, help="Add hours."),
    minutes: int = typer.Option(5, "-M", "--minutes", min=0, help="Add minutes."),
    seconds: int = typer.Option(0, "-S", "--seconds", min=0, help="Add seconds."),
    kill: bool = typer.Option(False, "--kill", help="Exit when timer finishes."),
) -> None:
    """Start a timer (placeholder; pacing colors/overtime comes next)."""
    spec = TimerSpec(hours=hours, minutes=minutes, seconds=seconds, kill=kill)
    remaining = spec.total_seconds
    if remaining <= 0:
        typer.echo("Timer must be > 0 seconds.")
        raise typer.Exit(code=2)

    while remaining >= 0:
        mm, ss = divmod(remaining, 60)
        hh, mm = divmod(mm, 60)
        typer.echo(f"{hh:02d}:{mm:02d}:{ss:02d}", nl=False)
        typer.echo("\r", nl=False)
        time.sleep(1)
        remaining -= 1

    typer.echo("")
    typer.echo("TIME!")
    if spec.kill:
        raise typer.Exit(code=0)
