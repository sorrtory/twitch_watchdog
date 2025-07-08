from dotenv import load_dotenv
import os

# Use .env for easy docker integration
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
VK_GROUP_ID = os.getenv('VK_GROUP_ID')
VK_WRITE_TO = os.getenv('VK_WRITE_TO').split(',') if os.getenv('VK_WRITE_TO') else []  
TWITCH_APP_ID = os.getenv('TWITCH_APP_ID')
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN')
TWITCH_USER_LOGIN = os.getenv('TWITCH_USER_LOGIN')
if any(var is None for var in [VK_TOKEN, TWITCH_APP_ID, TWITCH_ACCESS_TOKEN, TWITCH_USER_LOGIN, VK_GROUP_ID]):
    raise ValueError("One or more environment variables are not set. Please check your .env file.")