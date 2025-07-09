from dotenv import load_dotenv
import os

# Use .env for easy docker integration
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN') # Bot token 
VK_GROUP_ID = os.getenv('VK_GROUP_ID') # Bot group ID
VK_WRITE_TO = [2] # List of chat IDs to write. TODO: put in db
TWITCH_USER_LOGIN = os.getenv('TWITCH_USER_LOGIN')

# I can't have the TOKEN, so it's disabled for now
TWITCH_APP_ID = os.getenv('TWITCH_APP_ID', "PLACEHOLDER")
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN', "PLACEHOLDER")
if any(var is None for var in [VK_TOKEN, TWITCH_APP_ID, TWITCH_ACCESS_TOKEN, TWITCH_USER_LOGIN, VK_GROUP_ID]):
    raise ValueError("One or more environment variables are not set. Please check your .env file.")