import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from watchdog.config import settings

# Note: Fucking joke, in the vk doc "group" can mean public (сообщество) and chat (беседа)
# peer_id is used to identify them anyway (2000000000 + chat_id for chats)


class VKBot:
    """
    This class is used to interact with the VK API.
    """

    def __init__(self):
        self.vk_session = vk_api.VkApi(token=settings.vk_token)
        self.longpoll = VkBotLongPoll(self.vk_session, settings.vk_group_id)

    def send_message(self, message, peer_id) -> bool:
        """
        Send to the VK_GROUP_ID a message
        """
        try:
            params = {
                "peer_id": peer_id,  # ! Ensure this is the correct group ID
                # Mine is always 1, because I have only one group
                # Then peer_id is 2000000000 + 1
                "message": message,
                "random_id": 0,
            }
            self.vk_session.method("messages.send", params)
            return True
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
        except Exception as e:
            print(f"Error sending message: {e}")
        return False

    def listen(self):
        """
        Listen in cycle for new messages in the VK group and respond to them.
        """

        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.message is not None and "text" in event.object.message:
                    print(f"New message: {event.object.message['text']}")
                else:
                    print("New message received, but no text found.")
                # Example response logic
                ## self.send_message("Received your message!", event.object.message['peer_id'])
                ## print(f"Sent response to {event.object.message}")

    def check(self):
        """
        Check the messages in the VK group and respond to them.
        """
        try:
            messages = self.vk_session.method(
                "messages.getConversations", {"filter": "unread"}
            )
            for message in messages["items"]:
                peer_id = message["conversation"]["peer"]["id"]
                text = message["last_message"]["text"]
                print(f"New message from {peer_id}: {text}")
                # Example response logic
                # self.send_message("Received your message!", peer_id)
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
        except Exception as e:
            print(f"Error checking messages: {e}")

    def get_group_info(self):
        """
        Returns information about VK public where the bot is originated.
        """
        try:
            group_info = self.vk_session.method(
                "groups.getById", {"group_id": settings.vk_group_id}
            )
            return group_info[0] if group_info else None
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return None

    def get_chats(self):
        """
        Returns a list of chats where the bot is present.
        """
        try:
            chats = self.vk_session.method(
                "messages.getConversations", {"filter": "all", "extended": 1}
            )
            return chats
        except vk_api.exceptions.ApiError as e:
            print(f"VK API error: {e}")
            return []
