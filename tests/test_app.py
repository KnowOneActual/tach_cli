import pytest
from unittest.mock import patch
from textual.widgets import Digits
from textual.color import Color
from tach_cli.app import TachApp
from tach_cli.models import TimerSpec, Config, Thresholds, General

@pytest.mark.asyncio
async def test_app_timer_color_shifts():
    config = Config(
        thresholds=Thresholds(yellow=10, red=5, soft_overrun=5)
    )
    spec = TimerSpec(minutes=0, seconds=15)
    app = TachApp(spec=spec, config=config)
    
    async with app.run_test() as pilot:
        digits = app.query_one(Digits)
        
        # 15s -> Green
        assert digits.styles.color == Color.parse("green")
        
        # Manually set remaining for testing thresholds
        app.remaining = 9.0
        app._update_timer_display()
        assert digits.styles.color == Color.parse("yellow")
        
        app.remaining = 4.0
        app._update_timer_display()
        assert digits.styles.color == Color.parse("red")
        
        app.remaining = -1.0
        app._update_timer_display()
        assert digits.styles.color == Color.parse("magenta")
        
        app.remaining = -6.0
        app._update_timer_display()
        assert digits.styles.color == Color.parse("red")

@pytest.mark.asyncio
async def test_app_pause_reset():
    spec = TimerSpec(minutes=0, seconds=10)
    app = TachApp(spec=spec)
    
    async with app.run_test() as pilot:
        assert app.remaining == 10.0
        assert not app.is_paused
        
        await pilot.press("p")
        assert app.is_paused
        
        app.remaining = 5.0
        await pilot.press("r")
        assert app.remaining == 10.0
        assert not app.is_paused

@pytest.mark.asyncio
async def test_app_clock_mode():
    app = TachApp(clock_mode=True)
    async with app.run_test() as pilot:
        assert app.is_clock_mode
        # Wait for on_mount to finish (pilot.run_test handles this usually)
        digits = app.query_one(Digits)
        app.update_time()
        # Should be formatted as HH:MM:SS
        assert ":" in str(digits.value)

@pytest.mark.asyncio
async def test_app_kill_flag():
    spec = TimerSpec(minutes=0, seconds=1, kill=True)
    app = TachApp(spec=spec)
    with patch.object(app, "exit") as mock_exit:
        async with app.run_test():
            app.remaining = 0.0
            app.update_time()
            mock_exit.assert_called_once()

@pytest.mark.asyncio
async def test_app_timer_hours_formatting():
    spec = TimerSpec(hours=1, minutes=0, seconds=0)
    app = TachApp(spec=spec)
    async with app.run_test() as pilot:
        digits = app.query_one(Digits)
        app._update_timer_display()
        assert str(digits.value) == "01:00:00"

@pytest.mark.asyncio
async def test_app_reload_config():
    app = TachApp()
    async with app.run_test() as pilot:
        # Mock load_config to return a specific config
        with patch("tach_cli.app.load_config") as mock_load:
            mock_load.return_value = Config(general=General(bold=False))
            await pilot.press("ctrl+r")
            assert app.config.general.bold is False
            # In Textual, setting text_style to "none" results in an empty Style()
            assert not app.timer_display.styles.text_style.bold

@pytest.mark.asyncio
async def test_app_action_quit():
    app = TachApp()
    with patch.object(app, "exit") as mock_exit:
        async with app.run_test() as pilot:
            await pilot.press("q")
            mock_exit.assert_called_once()
