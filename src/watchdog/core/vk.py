from collections.abc import Iterable
from typing import AsyncGenerator

import vk_api
from anyio import sleep
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

from watchdog.config import settings

# Note: Fucking joke, in the vk doc "group" can mean public (сообщество) and chat (беседа)
# peer_id is used to identify them anyway (2000000000 + chat_id for chats)


class VKBot:
    """
    This class is used to interact with the VK API.
    """

    def __init__(self, token, group_id):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id)

    def listen(self):
        """
        Listen in cycle for new messages in the VK group.
        """
        print("Listening for new messages...")
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.message is not None and "text" in event.object.message:
                    print(f"New message: {event.object.message['text']}")
                else:
                    print("New message received, but no text found.")
                # Example response logic
                ## self.send_message("Received your message!", event.object.message['peer_id'])
                ## print(f"Sent response to {event.object.message}")

    def get_group_info(self):
        """
        Returns information about VK public where the bot originated from.
        """
        try:
            group_info = self.vk_session.method(
                "groups.getById", {"group_id": settings.vk_group_id}
            )
            return group_info[0] if group_info else None
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return None

    def get_conversations(self) -> list:
        """
        Returns a list of conversations where the bot is present.
        Basically that doesn't fully work as expected, because of VK side :(
        """
        try:
            chats = self.vk_session.method(
                "messages.getConversations", {"filter": "all"}
            )
            return chats
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return []


class VKBotConversation(VKBot):
    """
    This class is used to interact with a specific VK conversation.
    It inherits from VKBot and can be extended with additional methods.
    """

    def __init__(self, token, group_id, peer_id):
        super().__init__(token, group_id)
        self.peer_id = peer_id

    def does_conversation_exist(self) -> bool:
        """
        Check if the conversation with the given peer_id exists for the bot.
        """
        try:
            response = self.vk_session.method(
                "messages.getConversationsById", {"peer_ids": self.peer_id}
            )
            return bool(response.get("items"))
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return False

    def is_conversation_writable(self) -> bool:
        """
        Check if the conversation with the given peer_id is writable.
        """
        try:
            response = self.vk_session.method(
                "messages.getConversationsById", {"peer_ids": self.peer_id}
            )
            return (
                response.get("items", [{}])[0]
                .get("can_write", {})
                .get("allowed", False)
            )
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return False

    def get_chat_info(self) -> dict:
        """
        Returns chat title, members_count, photo_link

        Suppose conversation is a chat, not a private conversation.
        """
        try:
            response = self.vk_session.method(
                "messages.getConversationsById", {"peer_ids": self.peer_id}
            )
            items = response.get("items", [])
            if not items or len(items) == 0:
                return {}
            chat_settings = items[0].get("chat_settings", {})
            return {
                "title": chat_settings.get("title", "Can't find chat title"),
                "members_count": chat_settings.get("members_count", -1),
                "photo": chat_settings.get("photo", {}).get("photo_200", ""),
            }
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return {}

    def get_conversation_members(self) -> list:
        """
        Returns a list of members in the conversation specified by peer_id.
        """
        try:
            response = self.vk_session.method(
                "messages.getConversationMembers", {"peer_id": self.peer_id}
            )
            return response.get("items", [])
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return []

    def send_message(self, message: str) -> bool:
        """
        Send to the VK_GROUP_ID a message
        """
        try:
            params = {
                "peer_id": self.peer_id,  # ! Ensure this is the correct group ID
                # Mine is always 1, because I have only one group
                # Then peer_id is 2000000000 + 1
                "message": message,
                "random_id": 0,
            }
            self.vk_session.method("messages.send", params)
            return True
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
        except vk_api.exceptions.Captcha as e:
            print(f"VK API captcha error: {e}")
        return False


class ConversationExplorer:
    """
    This class is used to explore all conversations which the bot has access to.
    """

    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

    async def get_all_conversations(self) -> AsyncGenerator[VKBotConversation, None]:
        """
        Request every peer_id consecutively until it returns error.
        Yields VKBotConversation instances.
        """
        peer_id = 2000000001
        max_check_number = 10000  # Arbitrary limit to avoid infinite loop
        while peer_id < 2000000000 + max_check_number:
            try:
                conversation = VKBotConversation(self.token, self.group_id, peer_id)
                if conversation.does_conversation_exist():
                    yield conversation
                else:
                    break
                peer_id += 1
                await sleep(0.1)  # Sleep to avoid hitting API limits
            except vk_api.exceptions.ApiError as e:
                print(f"VK API error: {e}")
                break

    async def get_all_chats_info(self) -> list:
        """
        Get info of all conversations the bot has access to.
        """
        chats_info = []
        async for conv in self.get_all_conversations():
            chats_info.append(conv.get_chat_info())
        return chats_info
