from src.vk import VKBot
from src.twitch import TwitchWatchDog
from src.config import VK_WRITE_TO
from pprint import pprint
import time


if __name__ == "__main__":
    bot = VKBot()
    watchDog = TwitchWatchDog()

    # TODO: This must be moved to watchDog logic
    peer_id = 2000000000 + int(VK_WRITE_TO[0])
    was_live = False

    while True:
        try:
            is_live = watchDog.is_stream_live()
            if is_live and not was_live:
                bot.send_message("Стрим начался!", peer_id)
                was_live = True
            elif not is_live and was_live:
                bot.send_message("Стрим закончен!", peer_id)
                was_live = False
        except Exception as e:
            print(f"Error: {e}")
        finally:
            time.sleep(10)