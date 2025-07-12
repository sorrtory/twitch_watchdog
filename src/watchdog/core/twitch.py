import time
from abc import ABC, abstractmethod
import requests
import bs4


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
    def get_stream_title(self) -> str:
        """
        Get the title of the current stream.
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
    """Twitch WatchDog using html parsing"""

    def __init__(self, user_login : str):
        super().__init__(user_login)
        self.twitch_url = f"https://www.twitch.tv/{user_login}"

    def get_soup(self) -> bs4.BeautifulSoup:
        """
        Get the BeautifulSoup object for the Twitch page.
        """
        soup = bs4.BeautifulSoup(
            requests.get(self.twitch_url, timeout=10).content, "html.parser"
        )
        if not soup:
            raise ValueError("Failed to fetch or parse the Twitch page.")
        return soup

    def is_stream_live(self) -> bool:
        soup = self.get_soup()
        return "isLiveBroadcast" in str(soup)

    def get_stream_info(self):
        pass

    def get_stream_title(self) -> str:
        meta_tag = self.get_soup().find("meta", attrs={"name": "description"})
        if (
            meta_tag is not None
            and isinstance(meta_tag, bs4.Tag)
            and "content" in meta_tag.attrs
        ):
            return str(meta_tag["content"])

        return "Can't find stream title"


class TwitchWatchDog(TwitchWatchDogBase):
    """Twitch WatchDog using the best available method"""

    def __init__(self, user_login : str):
        super().__init__(user_login)
        self.watchdog = TwitchWatchDogHTML(user_login)

    def is_stream_live(self):
        return self.watchdog.is_stream_live()

    def get_stream_info(self):
        return self.watchdog.get_stream_info()

    def get_stream_title(self):
        return self.watchdog.get_stream_title()
