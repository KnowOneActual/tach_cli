from __future__ import annotations

import typer

from .app import TachApp
from .config import load_config
from .models import TimerSpec

app = typer.Typer(add_completion=False, no_args_is_help=True)


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
) -> None:
    """Start a countdown timer using the Textual UI."""
    config = load_config()

    # Determine initial duration
    total_seconds = 0

    if profile:
        if profile in config.profiles:
            total_seconds = config.profiles[profile]
        else:
            typer.echo(f"Profile '{profile}' not found in configuration.")
            raise typer.Exit(code=1)
    else:
        # Default to 5 minutes if no minutes provided
        m = minutes if minutes is not None else 5
        total_seconds = hours * 3600 + m * 60 + seconds

    # If flags were provided AND profile was provided, flags win (or add?)
    # For now, let's keep it simple: if profile provided, flags are ignored
    # OR if profile provided, and any flag is NON-ZERO, flag wins.
    # Actually, let's just use the profile if provided, else use the flags.
    # But if profile is used, and user did `tach timer --profile quick -S 10`,
    # maybe they want `quick + 10s`?
    # Let's stick to: profile sets the base, flags override/add if non-zero.
    if profile and (hours > 0 or (minutes is not None and minutes > 0) or seconds > 0):
        # If any flag is provided, use them INSTEAD of profile?
        # Let's just follow: profile is a base, flags override.
        # But which flag? All of them.
        m = minutes if minutes is not None else 0
        total_seconds = hours * 3600 + m * 60 + seconds

    # Convert total_seconds back to H:M:S for TimerSpec
    hh, mm = divmod(total_seconds, 3600)
    mm, ss = divmod(mm, 60)

    spec = TimerSpec(hours=hh, minutes=mm, seconds=ss, kill=kill, profile=profile)

    if spec.total_seconds <= 0:
        typer.echo("Timer must be > 0 seconds.")
        raise typer.Exit(code=2)

    TachApp(spec=spec, config=config).run()
