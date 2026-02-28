def test_imports():
    import tach_cli  # noqa: F401
    from tach_cli.cli import app  # noqa: F401


def test_timer_spec_total_seconds():
    from tach_cli.cli import TimerSpec

    spec = TimerSpec(hours=1, minutes=30, seconds=0)
    assert spec.total_seconds == 5400


def test_timer_spec_auto_convert():
    from tach_cli.cli import TimerSpec

    spec = TimerSpec(minutes=90)
    assert spec.total_seconds == 5400
