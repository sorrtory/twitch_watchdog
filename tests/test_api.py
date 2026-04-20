from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from watchdog.server.api import router

# filepath: /home/chinalap/Documents/twitch_watchdog/tests/test_api.py


client = TestClient(router)


@pytest.fixture
def mock_settings(monkeypatch):
    class MockSettings:
        twitch_user_login = "test_user"
        vk_write_to = [12345, 67890]
        vk_token = "fake_token"
        vk_group_id = 1

    monkeypatch.setattr("watchdog.server.api.settings", MockSettings())


def test_is_stream_alive(mock_settings):
    with patch("watchdog.server.api.TwitchWatchDog") as MockTwitchWatchDog:
        instance = MockTwitchWatchDog.return_value
        instance.is_stream_live.return_value = True
        response = client.get("/is_alive/")
        assert response.status_code == 200
        assert response.json() == {"is_alive": True}


def test_get_stream_title(mock_settings):
    with patch("watchdog.server.api.TwitchWatchDog") as MockTwitchWatchDog:
        instance = MockTwitchWatchDog.return_value
        instance.get_description.return_value = "Test Stream Title"
        response = client.get("/get_stream_title/")
        assert response.status_code == 200
        assert response.json() == {"title": "Test Stream Title"}


def test_send_message(mock_settings):
    with patch("watchdog.server.api.VKBotConversation") as MockVKBotConversation:
        instance = MockVKBotConversation.return_value
        instance.send_message.return_value = None
        response = client.post("/send_message/")
        assert (
            response.status_code == 200 or response.status_code == 204
        )  # FastAPI default for no return


def test_get_chats(mock_settings):
    with patch("watchdog.server.api.VKBotConversation") as MockVKBotConversation:
        instance = MockVKBotConversation.return_value
        instance.get_chat_info.side_effect = [
            {"title": "Chat 1", "members_count": 10, "avatar": "url1"},
            {"title": "Chat 2", "members_count": 5, "avatar": "url2"},
        ]
        response = client.get("/get_chats/")
        assert response.status_code == 200
        assert response.json() == {
            "chats": [
                {"title": "Chat 1", "members_count": 10, "avatar": "url1"},
                {"title": "Chat 2", "members_count": 5, "avatar": "url2"},
            ]
        }
