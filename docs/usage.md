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
| `P` | Pause / unpause (timer mode only) |
| `R` | Reset to initial duration (timer mode only) |
| `Q` | Quit Tach |
