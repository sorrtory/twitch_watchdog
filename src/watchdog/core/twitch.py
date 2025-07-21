import time
from abc import ABC, abstractmethod

import bs4
import requests


class TwitchWatchDogBase(ABC):
    """Abstract base class for Twitch WatchDog."""

    def __init__(self, user_login):
        """
        Initialize the Twitch WatchDog with the user login.
        """
        self.user_login = user_login

    @abstractmethod
    def is_stream_live(self) -> bool:
        """
        Check if the stream is live.
        """

    @abstractmethod
    def get_stream_info(self):
        """
        Get information about the current stream.
        """

    @abstractmethod
    def get_description(self) -> str:
        """
        Get the title of the current stream or channel description.
        """

    @abstractmethod
    def exists(self) -> bool:
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

    def get_soup(self) -> bs4.BeautifulSoup:
        """
        Get the BeautifulSoup object for the Twitch page.
        """

        # Send multiple requests to avoid network issues
        # and to ensure we get the most reliable response.
        reqs = {}
        for _ in range(TwitchWatchDogHTML.REQUEST_NUMBER):
            time.sleep(1)
            data = requests.get(self.twitch_url, timeout=10)
            if data.status_code == 200:
                reqs[data.content] = reqs.get(data.content, 0) + 1

        # Get the most common response content
        content, _ = max(reqs.items(), key=lambda item: item[1])

        if not content:
            raise ValueError("Failed to fetch the Twitch page.")

        soup = bs4.BeautifulSoup(content, "html.parser")
        if not soup:
            raise ValueError("Failed to parse the Twitch page.")
        return soup

    def is_stream_live(self) -> bool:
        soup = self.get_soup()
        return "isLiveBroadcast" in str(soup)

    def get_stream_info(self):
        raise NotImplementedError("Stream info retrieval is not implemented yet.")

    def get_description(self) -> str:
        meta_tag = self.get_soup().find("meta", attrs={"name": "description"})
        if (
            meta_tag is not None
            and isinstance(meta_tag, bs4.Tag)
            and "content" in meta_tag.attrs
        ):
            return str(meta_tag["content"])

        return "Can't find stream title"

    def exists(self) -> bool:
        """
        Check if the Twitch user exists.
        """
        soup = self.get_soup()
        return (
            soup.find("meta", attrs={"property": "og:title", "content": "Twitch"})
            is None
        )


class TwitchWatchDog(TwitchWatchDogBase):
    """Twitch WatchDog using the best available method"""

    def __init__(self, user_login: str):
        super().__init__(user_login)
        self.watchdog = TwitchWatchDogHTML(user_login)

    def is_stream_live(self):
        return self.watchdog.is_stream_live()

    def get_stream_info(self):
        return self.watchdog.get_stream_info()

    def get_description(self):
        return self.watchdog.get_description()

    def exists(self):
        return self.watchdog.exists()
