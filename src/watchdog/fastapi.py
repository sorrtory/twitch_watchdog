"""
Run the server ...
"""

# https://pre-commit.com/
# https://medium.com/internet-of-technology/beautify-your-python-code-with-pre-commit-linters-a-step-by-step-guide-d63604d6120b
# import time

# from watchdog.core.vk import VKBot
# from watchdog.core.twitch import TwitchWatchDog
# from watchdog.config import settings

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from watchdog.server.api import router

app = FastAPI()
app.include_router(router, prefix="/api", tags=["api"])

origins = [
    "http://localhost:3000",  # React default
    "http://localhost:5173",  # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("watchdog.fastapi:app", host="0.0.0.0", port=8000)

# main()

# watchDog = TwitchWatchDog("shylily")

# print(bot.get_chats())
# TO!DO: This must be moved to watchDog logic # pylint: disable=fixme
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
