import os
from pathlib import Path

from tach_cli.config import _parse_config, load_config


def test_default_config():
    config = load_config(Path("/nonexistent/path"))
    assert config.general.bold is True
    assert config.thresholds.yellow == 300
    assert config.thresholds.red == 120
    assert config.profiles == {}


def test_parse_config():
    data = {
        "general": {"bold": False},
        "thresholds": {"yellow": 60, "red": 30},
        "profiles": {"test": 10},
    }
    config = _parse_config(data)
    assert config.general.bold is False
    assert config.thresholds.yellow == 60
    assert config.thresholds.red == 30
    assert config.profiles["test"] == 10


def test_env_override(tmp_path):
    conf_file = tmp_path / "test_conf.toml"
    conf_file.write_text("[profiles]\nenv_test = 42\n")

    os.environ["TACH_CONF"] = str(conf_file)
    try:
        config = load_config()
        assert config.profiles["env_test"] == 42
    finally:
        del os.environ["TACH_CONF"]
