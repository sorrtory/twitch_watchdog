import time
from abc import ABC, abstractmethod

import bs4
import httpx
import anyio

# TODO: It is better to send requests concurrently instead of in cycle


class TwitchWatchDogBase(ABC):
    """Abstract base class for Twitch WatchDog."""

    def __init__(self, user_login):
        """
        Initialize the Twitch WatchDog with the user login.
        """
        self.user_login = user_login

    @abstractmethod
    async def is_stream_live(self) -> bool:
        """
        Check if the stream is live.
        """

    @abstractmethod
    async def get_stream_info(self):
        """
        Get information about the current stream.
        """

    @abstractmethod
    async def get_description(self) -> str:
        """
        Get the title of the current stream or channel description.
        """

    @abstractmethod
    async def exists(self) -> bool:
        """
        Check if the Twitch user exists.
        """

    def listen(self, on_live_callback, on_offline_callback):
        """
        Start listening for stream status changes.
        """
        while True:
            live = self.is_stream_live()
            if live:
                print("Stream is live!")
                on_live_callback()
            else:
                print("Stream is offline.")
                on_offline_callback()
            time.sleep(10)


# ! I can't get TOKEN, because I'm from Russia :(
class TwitchWatchDogApi(TwitchWatchDogBase):
    """Twitch WatchDog using Twitch API"""

    def __init__(self, user_login):
        super().__init__(user_login)
        raise NotImplementedError("Twitch API integration is not implemented yet.")


class TwitchWatchDogHTML(TwitchWatchDogBase):
    """
    Twitch WatchDog using html parsing.

    curl the page, analyze the meta tags and their content.
    """

    # This is the number of requests to send to the Twitch page
    # The bigger the number, the more time every method will take
    REQUEST_NUMBER = 3

    def __init__(self, user_login: str):
        super().__init__(user_login)
        self.twitch_url = f"https://www.twitch.tv/{user_login}"
        self.lock = anyio.Lock()
        self.responses = {}

    async def fetch(self, url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                return None
            async with self.lock:
                self.responses[response.text] = self.responses.get(response.text, 0) + 1

    async def get_soup(self) -> bs4.BeautifulSoup:
        """
        Get the BeautifulSoup object for the Twitch page.
        """
        self.responses = {}
        # Send multiple requests to avoid network issues
        # and to ensure we get the most reliable response.
        # Run all requests concurrently
        async with anyio.create_task_group() as tg:
            for _ in range(self.REQUEST_NUMBER):
                tg.start_soon(self.fetch, self.twitch_url)
        reqs = self.responses

        # Get the most common response content
        content, _ = max(reqs.items(), key=lambda item: item[1])

        if not content:
            raise ValueError("Failed to fetch the Twitch page.")

        soup = bs4.BeautifulSoup(content, "html.parser")
        if not soup:
            raise ValueError("Failed to parse the Twitch page.")
        return soup

    async def is_stream_live(self) -> bool:
        soup = await self.get_soup()
        return "isLiveBroadcast" in str(soup)

    async def get_stream_info(self):
        raise NotImplementedError("Stream info retrieval is not implemented yet.")

    async def get_description(self) -> str:
        soup = await self.get_soup()
        meta_tag = soup.find("meta", attrs={"name": "description"})
        if (
            meta_tag is not None
            and isinstance(meta_tag, bs4.Tag)
            and "content" in meta_tag.attrs
        ):
            return str(meta_tag["content"])

        return "Can't find stream title"

    async def exists(self) -> bool:
        """
        Check if the Twitch user exists.
        """
        soup = await self.get_soup()
        return (
            soup.find("meta", attrs={"property": "og:title", "content": "Twitch"})
            is None
        )


class TwitchWatchDog(TwitchWatchDogBase):
    """Twitch WatchDog using the best available method"""

    def __init__(self, user_login: str):
        super().__init__(user_login)
        self.watchdog = TwitchWatchDogHTML(user_login)

    async def is_stream_live(self):
        return await self.watchdog.is_stream_live()

    async def get_stream_info(self):
        return await self.watchdog.get_stream_info()

    async def get_description(self):
        return await self.watchdog.get_description()

    async def exists(self):
        return await self.watchdog.exists()
