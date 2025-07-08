import requests
from twitchAPI.twitch import Twitch
from src.config import TWITCH_APP_ID, TWITCH_ACCESS_TOKEN, TWITCH_USER_LOGIN
import time

# ! I can't get TOKEN, because I'm from Russia :(
class TwitchWatchDogApi:
    def __init__(self):
        self.twitch = Twitch(TWITCH_APP_ID, TWITCH_ACCESS_TOKEN)
        self.twitch.authenticate_app([])

    def is_stream_live(self):
        """
        Check if the stream is live.
        """
        streams = self.twitch.get_streams(user_login=TWITCH_USER_LOGIN)
        return len(streams['data']) > 0

    def get_stream_info(self):
        """
        Get information about the current stream.
        """
        streams = self.twitch.get_streams(user_login=TWITCH_USER_LOGIN)
        return streams['data'][0] if streams['data'] else None
    
    

class TwitchWatchDogHTML:
    def __init__(self):
        self.twitch_url = f'https://www.twitch.tv/{TWITCH_USER_LOGIN}'

    def is_stream_live(self):
        """
        Check if the stream is live using HTML content.
        """
        try:
            contents = requests.get(self.twitch_url, timeout=10).content.decode('utf-8')
            return 'isLiveBroadcast' in contents
        except Exception as e:
            print(f"Error fetching Twitch page: {e}")
            return False
        
    def get_stream_info(self):
        """
        Get information about the current stream using HTML content.
        """
        try:
            contents = requests.get(self.twitch_url, timeout=10).content.decode('utf-8')
            if 'isLiveBroadcast' in contents:
                # Extract stream info from the HTML content
                # This is a placeholder; actual extraction logic will depend on the HTML structure
                return {
                    'title': 'Stream Title',
                    'viewers': 0,
                    'game': 'Game Name'
                }
            else:
                return None
        except Exception as e:
            print(f"Error fetching Twitch page: {e}")
            return None

class TwitchWatchDog:
    def __init__(self):
        self.api = TwitchWatchDogHTML() # Change to TwitchWatchDogApi()

    def is_stream_live(self):
        return self.api.is_stream_live()

    def get_stream_info(self):
        return self.api.get_stream_info()
    
    def listen(self, onLiveCallback, onOfflineCallback):
        """
        Start listening for stream status changes.
        """
        while True:
            try:
                live = self.is_stream_live()
                if live:
                    print("Stream is live!")
                    onLiveCallback()
                else:
                    print("Stream is offline.")
                    onOfflineCallback()
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(10)