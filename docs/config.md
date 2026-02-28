# Configuration

Tach uses a TOML config file for persistent settings. CLI flags always override the config.

## Default location

| Platform | Path |
|----------|------|
| Linux    | `~/.config/tach/conf.toml` |
| macOS    | `~/Library/Application Support/tach/conf.toml` |

Override with the `TACH_CONF` environment variable.

## Example `conf.toml`

```toml
[general]
bold = true

[position]
horizontal = "center"
vertical = "center"

[thresholds]
yellow = 300        # switch to yellow at 5 min remaining
red = 120           # switch to red at 2 min remaining
soft_overrun = 120  # first 2 minutes of overtime are treated as “soft” overrun

[profiles]
standard = 1800
quick = 300
lightning = 120
```

See `examples/conf.toml` for a ready-to-use starter config.
