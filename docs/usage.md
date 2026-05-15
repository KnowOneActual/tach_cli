# Usage

## Commands

```
tach [COMMAND] [OPTIONS]

Commands:
  timer      Start a countdown timer
  clock      Display the current time
  help       Print help
```

## Timer examples

```bash
tach timer                       # 5-minute default
tach timer -M 30                 # 30-minute countdown
tach timer -H 1 -M 30            # 1 hour 30 minutes
tach timer -M 45 --kill          # exit automatically when timer ends
tach timer --profile quick       # use duration from 'quick' profile in config
tach timer -M 15 --summary       # print a post-show summary after exiting
```

Time units auto-convert: `tach timer -M 90` starts a 1h 30m timer.
CLI flags override profile durations: `tach timer --profile quick -S 10` will start a 10s timer, overriding the 'quick' profile.

## Clock

```bash
tach clock   # display current time of day (H:M:S)
```

## Keyboard controls

| Key | Action |
|-----|--------|
| `p` | Pause / unpause (timer mode only) |
| `r` | Reset to initial duration (timer mode only) |
| `q` | Quit Tach |
| `ctrl+r` | Reload configuration |
| `k`, `Up` | Nudge time +30s |
| `j`, `Down` | Nudge time -30s |
| `l`, `Right` | Nudge time +2m |
| `h`, `Left` | Nudge time -2m |
| `L` | Nudge time +5m |
| `H` | Nudge time -5m |

## Shell Completions

Tach supports shell completions for Bash, Zsh, and Fish.

To enable completions, run the following command and follow the instructions:

```bash
tach --install-completion
```

For more details on shell completions with Typer, refer to the [Typer documentation](https://typer.tiangolo.com/tutorial/options/completion/).
