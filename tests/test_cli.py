from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from tach_cli.cli import app

runner = CliRunner()


def test_cli_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "timer" in result.output
    assert "clock" in result.output


def test_cli_timer_invalid() -> None:
    # Timer must be > 0
    result = runner.invoke(app, ["timer", "-M", "0", "-S", "0"])
    assert result.exit_code == 2
    assert "Timer must be > 0 seconds" in result.output


def test_cli_profile_not_found() -> None:
    result = runner.invoke(app, ["timer", "--profile", "nonexistent"])
    assert result.exit_code == 1
    assert "Profile 'nonexistent' not found" in result.output


@patch("tach_cli.cli.TachApp")
def test_cli_timer_run(mock_app: MagicMock) -> None:
    result = runner.invoke(app, ["timer", "-M", "10", "--kill"])
    assert result.exit_code == 0
    mock_app.assert_called_once()
    _, kwargs = mock_app.call_args
    assert kwargs["spec"].minutes == 10
    assert kwargs["spec"].kill is True


@patch("tach_cli.cli.TachApp")
def test_cli_clock_run(mock_app: MagicMock) -> None:
    result = runner.invoke(app, ["clock"])
    assert result.exit_code == 0
    mock_app.assert_called_once()
    assert mock_app.call_args[1]["clock_mode"] is True


@patch("tach_cli.cli.TachApp")
def test_cli_timer_profile_plus_flags(mock_app: MagicMock) -> None:
    # If profile AND flags provided, flags win/override
    # Config has no profiles by default in tests, so we need to mock load_config
    with patch("tach_cli.cli.load_config") as mock_load:
        from tach_cli.models import Config

        mock_load.return_value = Config(profiles={"fast": 60})
        result = runner.invoke(app, ["timer", "--profile", "fast", "-S", "10"])
        assert result.exit_code == 0
        mock_app.assert_called_once()
        assert (
            mock_app.call_args[1]["spec"].total_seconds == 10
        )  # Flag wins in current logic
