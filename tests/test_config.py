from watchdog.config import Settings


def test_settings():
    """Test settings configuration."""
    settings = Settings()  # pyright: ignore
    # pydantic_settings will raise an error if the settings are not valid
    assert settings is not None
    assert settings.vk_write_to.index(1) >= 0  # Check if vk_write_to contains 1
