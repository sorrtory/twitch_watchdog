"""
Run the server ...
"""

# import time

# from watchdog.core.vk import VKBot
# from watchdog.core.twitch import TwitchWatchDog
# from watchdog.config import settings



from fastapi import FastAPI
from watchdog.server.api import router

app = FastAPI()


app.include_router(router, prefix="/api", tags=["api"])









# if __name__ == "__main__":
#     bot = VKBot(settings.vk_token, settings.vk_group_id)
#     watchDog = TwitchWatchDog("shylily")

    # print(bot.get_chats())
    # TODO: This must be moved to watchDog logic
    # peer_id = 2000000000 + settings.vk_write_to[0]
    # was_live = False

    # print("Starting Twitch WatchDog...")
    # print(watchDog.is_stream_live())
    # print(watchDog.get_stream_title())
    # while True:
    #     try:
    #         is_live = watchDog.is_stream_live()
    #         if is_live and not was_live:
    #             bot.send_message("Стрим начался!", peer_id)
    #             was_live = True
    #         elif not is_live and was_live:
    #             bot.send_message("Стрим закончен!", peer_id)
    #             was_live = False
    #     except Exception as e:
    #         print(f"Error: {e}")
    #     finally:
    #         time.sleep(10)
