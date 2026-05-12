from __future__ import annotations

import logging
import os
from pathlib import Path
import sys
from typing import Any

from platformdirs import user_config_dir

from .models import Config, General, Position, Thresholds

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

logger = logging.getLogger(__name__)


def load_config(config_path: Path | None = None) -> Config:
    """Load configuration from a TOML file."""
    if config_path is None:
        env_path = os.environ.get("TACH_CONF")
        if env_path:
            config_path = Path(env_path)
        else:
            config_dir = Path(user_config_dir("tach"))
            config_path = config_dir / "conf.toml"

    if not config_path.exists():
        logger.debug("No config file found at %s, using defaults.", config_path)
        return Config()

    try:
        with config_path.open("rb") as f:
            data = tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError) as e:
        logger.warning(
            "Failed to read config at %s: %s — using defaults.", config_path, e
        )
        return Config()

    return _parse_config(data)


def _parse_config(data: dict[str, Any]) -> Config:
    """Parse raw TOML data into a Config object."""
    general_data = data.get("general", {})
    position_data = data.get("position", {})
    thresholds_data = data.get("thresholds", {})
    profiles = data.get("profiles", {})

    general = General(
        bold=general_data.get("bold", True),
    )
    position = Position(
        horizontal=position_data.get("horizontal", "center"),
        vertical=position_data.get("vertical", "center"),
    )
    thresholds = Thresholds(
        yellow=thresholds_data.get("yellow", 300),
        red=thresholds_data.get("red", 120),
        soft_overrun=thresholds_data.get("soft_overrun", 120),
    )

    # Ensure profiles is a dict[str, int]
    parsed_profiles: dict[str, int] = {}
    for name, value in profiles.items():
        if isinstance(value, int):
            parsed_profiles[name] = value

    return Config(
        general=general,
        position=position,
        thresholds=thresholds,
        profiles=parsed_profiles,
    )
