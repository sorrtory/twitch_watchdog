import signal
from datetime import datetime

from watchdog.config import settings
from watchdog.core.vk import VKBot


def timeout_handler(signum, frame):
    """
    SIGALARM handler
    """
    raise TimeoutError("VKBot initialization timed out")


def test_vk_bot_initialization():
    """Test the initialization of the VKBot with a timeout."""
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)  # Set timeout to 5 seconds
    try:
        bot = VKBot(settings.vk_token, settings.vk_group_id)
        assert bot is not None
    finally:
        signal.alarm(0)  # Disable the alarm


def test_send_message():
    """Test sending a message to the VK group."""
    bot = VKBot(settings.vk_token, settings.vk_group_id)
    msg = f"Test message at {datetime.now()}"  # Create a test message
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    # Test sending a message
    response = bot.send_message(msg, peer_id)
    assert response is not False
