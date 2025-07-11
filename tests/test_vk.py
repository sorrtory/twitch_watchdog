from datetime import datetime

from watchdog.core.vk import VKBot
from watchdog.config import settings


def test_send_message():
    """Test sending a message to the VK group."""
    bot = VKBot()
    msg = f"Test message at {datetime.now()}"  # Create a test message
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    # Test sending a message
    response = bot.send_message(msg, peer_id)
    assert response is not False
