from src.watchdog.core.twitch import TwitchWatchDog
import pytest


def test_is_stream_live():
    """Test if the Twitch stream is live."""
    definitely_offline = "test_user"
    definitely_online = "asmr_marie"
    assert TwitchWatchDog(definitely_offline).is_stream_live() is False
    assert TwitchWatchDog(definitely_online).is_stream_live() is True


def test_get_stream_title():
    """Test if the Twitch stream title is retrieved correctly."""
    definitely_offline = "fert805"
    definitely_online = "asmr_marie"
    assert (
        TwitchWatchDog(definitely_offline).get_stream_title()
        == "Can't find stream title"
    )
    assert (
        TwitchWatchDog(definitely_online)
        .get_stream_title()
        .find("!fish !stats󠀀 !commands !triggerlist")
        != -1
    )



