import os
import time

class Config(object):
    # Get a bot token from botfather, renamed to avoid conflicts
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", None)
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Error: TELEGRAM_BOT_TOKEN is not set. Please check your environment variables.")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 0))
    if not API_ID:
        raise ValueError("Error: API_ID is not set. Please check your environment variables.")

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", None)
    if not API_HASH:
        raise ValueError("Error: API_HASH is not set. Please check your environment variables.")

    # Database URL from MongoDB Atlas
    DATABASE_URI = os.environ.get("DATABASE_URI", None)
    if not DATABASE_URI:
        raise ValueError("Error: DATABASE_URI is not set. Please check your environment variables.")

    # Your database name from MongoDB
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    if not AUTH_USERS:
        print("Warning: AUTH_USERS is not set. Bot commands may not work properly.")

    # To save user details (useful for getting user info and total user counts)
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()

    # Heroku API key to check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    # Optional: Alternate bot commands
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMAND", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMAND", "disconnect")

    # Bot start time
    BOT_START_TIME = time.time()

    # Debugging: Print environment variables during startup
    print(f"TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
    print(f"API_ID: {API_ID}")
    print(f"API_HASH: {API_HASH}")
    print(f"DATABASE_URI: {DATABASE_URI}")
    print(f"DATABASE_NAME: {DATABASE_NAME}")
    print(f"AUTH_USERS: {AUTH_USERS}")
    print(f"SAVE_USER: {SAVE_USER}")
