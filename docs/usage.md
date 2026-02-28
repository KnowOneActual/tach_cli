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
```

Time units auto-convert: `tach timer -M 90` starts a 1h 30m timer.

## Clock

```bash
tach clock   # display current time of day
```

## Keyboard controls

| Key | Action |
|-----|--------|
| `P` | Pause / unpause |
| `R` | Reset |
| `Q` / `Esc` / `Ctrl+C` | Quit |
