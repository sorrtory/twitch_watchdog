import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')  # id группы для отправки сообщения
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN')
TWITCH_USER_LOGIN = os.getenv('TWITCH_USER_LOGIN')  # логин стримера
TWITCH_CHECK_METHOD = os.getenv('TWITCH_CHECK_METHOD', 'api')  # 'api' или 'html'

if any(var is None for var in [VK_TOKEN, TWITCH_CLIENT_ID, TWITCH_ACCESS_TOKEN, TWITCH_USER_LOGIN, VK_GROUP_ID]):
    raise ValueError("One or more environment variables are not set. Please check your .env file.")

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()



def is_stream_live_html():
    url = f'https://www.twitch.tv/{TWITCH_USER_LOGIN}'
    try:
        contents = requests.get(url, timeout=10).content.decode('utf-8')
        return 'isLiveBroadcast' in contents
    except Exception as e:
        print(f"Error fetching Twitch page: {e}")
        return False


def is_stream_live():
    if TWITCH_CHECK_METHOD == 'html':
        return is_stream_live_html()
    url = f"https://api.twitch.tv/helix/streams?user_login={TWITCH_USER_LOGIN}"
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return len(data.get('data', [])) > 0
    else:
        print(f"Twitch API error: {response.status_code}")
        return False


def send_vk_message(message):
    vk_session.method("messages.send", {
        "peer_id": int(VK_GROUP_ID),  # ! Ensure this is the correct group ID
                                      # ! Mine is always 1
        
        "message": message,
        "random_id": 0
    })


def main_loop():
    was_live = False
    while True:
        try:
            live = is_stream_live()
            if live and not was_live:
                send_vk_message("Стрим начался!")
                was_live = True
            elif not live and was_live:
                send_vk_message("Стрим закончен!")
                was_live = False
            time.sleep(10)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main_loop()