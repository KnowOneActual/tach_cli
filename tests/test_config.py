import logging
import os
from pathlib import Path
from typing import Any

from tach_cli.config import _parse_config, load_config


def test_default_config() -> None:
    config = load_config(Path("/nonexistent/path"))
    assert config.general.bold is True
    assert config.thresholds.yellow == 300
    assert config.thresholds.red == 120
    assert config.profiles == {}


def test_parse_config() -> None:
    data: dict[str, Any] = {
        "general": {"bold": False},
        "thresholds": {"yellow": 60, "red": 30},
        "profiles": {"test": 10},
    }
    config = _parse_config(data)
    assert config.general.bold is False
    assert config.thresholds.yellow == 60
    assert config.thresholds.red == 30
    assert config.profiles["test"] == 10


def test_invalid_toml(tmp_path: Path) -> None:
    conf_file = tmp_path / "invalid.toml"
    conf_file.write_text("this is not toml")
    config = load_config(conf_file)
    assert config.general.bold is True  # Defaults


def test_missing_config_debug_log(caplog: Any) -> None:
    with caplog.at_level(logging.DEBUG):
        load_config(Path("/nonexistent/path/to/conf.toml"))
        assert "No config file found" in caplog.text


def test_env_override(tmp_path: Path) -> None:
    conf_file = tmp_path / "test_conf.toml"
    conf_file.write_text("[profiles]\nenv_test = 42\n")

    os.environ["TACH_CONF"] = str(conf_file)
    try:
        config = load_config()
        assert config.profiles["env_test"] == 42
    finally:
        del os.environ["TACH_CONF"]
