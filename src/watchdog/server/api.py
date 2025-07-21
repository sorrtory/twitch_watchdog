# I want to use FastAPI to create a server that can handle requests from frontend,
# which will be used to send messages to VK group and check Twitch stream status
# for now

from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    """Get a list of users."""
    # This is a placeholder implementation.
    return [{"username": "Rick"}, {"username": "Morty"}]
