from watchdog.config import Settings


def test_config():
    """Should not raise an ValidationError"""
    settings = Settings()  # pyright: ignore
    assert isinstance(settings, Settings)
