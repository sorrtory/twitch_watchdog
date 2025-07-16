from datetime import datetime

from watchdog.config import settings
from watchdog.core.vk import VKBot


def test_send_message():
    """Test sending a message to the VK group."""
    bot = VKBot(settings.vk_token, settings.vk_group_id)
    msg = f"Test message at {datetime.now()}"  # Create a test message
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    # Test sending a message
    response = bot.send_message(msg, peer_id)
    assert response is not False
