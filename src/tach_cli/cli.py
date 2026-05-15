from __future__ import annotations

import typer

from .app import TachApp
from .config import load_config
from .models import TimerSpec

app = typer.Typer(no_args_is_help=True)


@app.command()
def clock() -> None:
    """Display the current time using the Textual UI."""
    config = load_config()
    TachApp(clock_mode=True, config=config).run()


@app.command()
def timer(
    hours: int = typer.Option(0, "-H", "--hours", min=0, help="Hours for the timer."),
    minutes: int | None = typer.Option(
        None, "-M", "--minutes", min=0, help="Minutes for the timer."
    ),
    seconds: int = typer.Option(
        0, "-S", "--seconds", min=0, help="Seconds for the timer."
    ),
    kill: bool = typer.Option(False, "--kill", help="Exit when timer finishes."),
    profile: str | None = typer.Option(
        None, "--profile", "-p", help="Use a named profile from the config."
    ),
    summary: bool = typer.Option(
        False, "--summary", help="Print a session summary after exiting."
    ),
) -> None:
    """Start a countdown timer using the Textual UI."""
    config = load_config()

    # 1. Start with the base duration
    if profile:
        if profile in config.profiles:
            total_seconds = config.profiles[profile]
        else:
            typer.echo(f"Profile '{profile}' not found in configuration.")
            raise typer.Exit(code=1)
    else:
        # Default to 5 minutes if no profile or minutes provided
        m = minutes if minutes is not None else 5
        total_seconds = hours * 3600 + m * 60 + seconds

    # 2. If flags were provided alongside a profile, flags override the entire duration
    # This matches the user's likely intent: "use 'quick' but set it to 10s"
    if profile and (hours > 0 or minutes is not None or seconds > 0):
        m = minutes if minutes is not None else 0
        total_seconds = hours * 3600 + m * 60 + seconds

    # 3. Convert back to H:M:S for TimerSpec
    hh, mm = divmod(total_seconds, 3600)
    mm, ss = divmod(mm, 60)

    spec = TimerSpec(hours=hh, minutes=mm, seconds=ss, kill=kill, profile=profile)

    if spec.total_seconds <= 0:
        typer.echo("Timer must be > 0 seconds.")
        raise typer.Exit(code=2)

    app_instance = TachApp(spec=spec, config=config)
    app_instance.run()

    if summary:

        def fmt(s: int) -> str:
            h, m = divmod(s, 3600)
            m, sc = divmod(m, 60)
            if h > 0:
                return f"{h:02d}:{m:02d}:{sc:02d}"
            return f"{m:02d}:{sc:02d}"

        planned = spec.total_seconds
        actual = int(app_instance.elapsed_time)
        overtime = max(0, actual - planned)

        typer.echo("\n--- Session Summary ---")
        typer.echo(f"Planned:  {fmt(planned)}")
        typer.echo(f"Actual:   {fmt(actual)}")
        if overtime > 0:
            typer.echo(f"Overtime: {fmt(overtime)}")
        typer.echo("-----------------------\n")
