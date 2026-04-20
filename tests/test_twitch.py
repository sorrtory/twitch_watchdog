import pytest

from src.watchdog.core.twitch import TwitchWatchDog

DEFINITELY_OFFLINE = "test_user"
DEFINITELY_ONLINE = "asmr_marie"
DEFINITELY_NOT_EXIST = "ggwplanayajksakjsdjnadsjnsdajhndsa"
DEFINITELY_BANNED = "zxcursed"
DEFINITELY_EXISTS = "asmr_marie"


@pytest.mark.anyio
async def test_is_stream_live():
    """Test if the Twitch stream is live."""
    assert await TwitchWatchDog(DEFINITELY_OFFLINE).is_stream_live() is False
    assert await TwitchWatchDog(DEFINITELY_ONLINE).is_stream_live() is True
    assert await TwitchWatchDog(DEFINITELY_NOT_EXIST).is_stream_live() is False


@pytest.mark.anyio
async def test_get_stream_title():
    """Test if the Twitch stream title is retrieved correctly."""
    assert (
        await TwitchWatchDog(DEFINITELY_OFFLINE).get_description()
        == "my own new channel"
    )
    assert (await TwitchWatchDog(DEFINITELY_ONLINE).get_description()).find(
        "!fish !stats󠀀 !commands !triggerlist"
    ) != -1
    assert (
        await TwitchWatchDog(DEFINITELY_NOT_EXIST).get_description()
        == "Can't find stream title"
    )


@pytest.mark.anyio
async def test_exists():
    """Test if the Twitch user exists."""
    assert await TwitchWatchDog(DEFINITELY_NOT_EXIST).exists() is False
    assert await TwitchWatchDog(DEFINITELY_BANNED).exists() is True
    assert await TwitchWatchDog(DEFINITELY_OFFLINE).exists() is True
    assert await TwitchWatchDog(DEFINITELY_ONLINE).exists() is True
    assert await TwitchWatchDog(DEFINITELY_EXISTS).exists() is True
