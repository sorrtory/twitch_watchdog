import signal
from datetime import datetime
from unittest.mock import patch

import pytest

from watchdog.config import settings
from watchdog.core.vk import ConversationExplorer, VKBot, VKBotConversation


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
    msg = f"Test message at {datetime.now()}"  # Create a test message
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
    # Test sending a message
    response = conv.send_message(msg)
    assert response is not False


def test_write_to_is_ok():
    """
    Test write_to field in config specifies only existing and writable conversations.
    """
    for group_id in settings.vk_write_to:
        peer_id = 2000000000 + int(group_id)
        conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
        assert conv.does_conversation_exist(), True
        assert conv.is_conversation_writable(), True


def test_get_chat_info():
    """Test getting chat info for a specific conversation."""
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
    with patch.object(conv, "vk_session") as mock_vk_session:
        mock_vk_session.method.return_value = {
            "items": [
                {
                    "chat_settings": {
                        "title": "Test Chat",
                        "members_count": 10,
                        "photo": {"photo_200": "url"},
                    }
                }
            ]
        }
        chat_info = conv.get_chat_info()
        assert isinstance(chat_info, dict)
        assert chat_info["title"] == "Test Chat"
        assert chat_info["members_count"] == 10
        assert chat_info["photo"] == "url"


def test_get_chat_info2():
    """Test getting chat info for first conversation."""
    peer_id = 2000000000 + int(settings.vk_write_to[0])  # Convert group ID to peer_id
    conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
    chat_info = conv.get_chat_info()
    print(f"Chat info: {chat_info}")
    assert chat_info is not None
    assert isinstance(chat_info, dict)
    assert "title" in chat_info
    assert "members_count" in chat_info
    assert "photo" in chat_info
    

@pytest.mark.anyio
async def test_get_chats():
    """
    Test getting the list of all chats.
    If chats are not available, could probalbly await for a while
    """
    conv_explorer = ConversationExplorer(settings.vk_token, settings.vk_group_id)
    chats_info = await conv_explorer.get_all_chats_info()
    assert isinstance(chats_info, list)
    assert len(chats_info) > 0  # Ensure there are chats available
