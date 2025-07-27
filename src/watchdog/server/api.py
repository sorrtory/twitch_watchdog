# I want to use FastAPI to create a server that can handle requests from frontend,
# which will be used to send messages to VK group and check Twitch stream status
# for now

from fastapi import APIRouter

from watchdog.config import settings
from watchdog.core.twitch import TwitchWatchDog
from watchdog.core.vk import VKBotConversation

router = APIRouter()


### Twitch API Endpoints ###
@router.get("/is_alive/", tags=["stream"])
async def is_stream_alive():
    """Check if the stream is alive."""
    watchdog = TwitchWatchDog(settings.twitch_user_login)
    return {"is_alive": watchdog.is_stream_live()}


@router.get("/get_stream_title/", tags=["stream"])
async def get_stream_title():
    """Get the title of the current stream."""
    watchdog = TwitchWatchDog(settings.twitch_user_login)
    return {"title": watchdog.get_description()}


### VK API Endpoints ###
@router.post("/send_message/", tags=["vk"])
# async def send_message(peer_id: int, message: str):
async def send_message():
    """Send a message to a VK group."""
    # TODO: Implement peer_id and message as parameters
    for peer_id in settings.vk_write_to:
        peer_id = 2000000000 + int(peer_id)  # Convert group ID
        conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
        conv.send_message("Hello from WatchDog!")

@router.post("/change_message/", tags=["vk"])
async def change_message():
    """Change the message sent to a VK group."""
    # settings TODO

@router.get("/get_chats/", tags=["vk"])
async def get_chats():
    """Get the list of chats. Send chat title, members count, and avatar."""
    chats = []
    for peer_id in settings.vk_write_to:
        peer_id = 2000000000 + int(peer_id)  # Convert group ID
        conv = VKBotConversation(settings.vk_token, settings.vk_group_id, peer_id)
        chats.append(conv.get_chat_info())
    return {"chats": chats}
