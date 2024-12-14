import os
import time

class Config(object):
    # Get a bot token from BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    if not TG_BOT_TOKEN:
        raise ValueError("Missing TG_BOT_TOKEN environment variable")

    # Get API ID and Hash from https://my.telegram.org
    API_ID = os.environ.get("API_ID", None)
    if not API_ID or not API_ID.isdigit():
        raise ValueError("Invalid or missing API_ID environment variable")
    API_ID = int(API_ID)

    API_HASH = os.environ.get("API_HASH", "")
    if not API_HASH:
        raise ValueError("Missing API_HASH environment variable")

    # Database URL from MongoDB Atlas or other sources
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    if not DATABASE_URI:
        raise ValueError("Missing DATABASE_URI environment variable")

    # Database name for MongoDB
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

    # IDs of authorized users (comma-separated in environment variable)
    AUTH_USERS = {int(x) for x in os.environ.get("AUTH_USERS", "").split(",") if x.isdigit()}

    # Option to save user details
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower() == "yes"

    # Optional: Heroku API Key for checking dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

    # Commands (with optional customizations via environment variables)
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMAND", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMAND", "disconnect")

    # Track bot's start time
    BOT_START_TIME = time.time()
