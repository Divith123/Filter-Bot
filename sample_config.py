import os
import time

class Config:
    # Initialize all required environment variables with error handling
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    if not TG_BOT_TOKEN:
        raise ValueError("TG_BOT_TOKEN is not set. Please configure it in environment variables.")

    API_ID = os.environ.get("API_ID")
    if not API_ID or not API_ID.isdigit():
        raise ValueError("API_ID is not set or invalid. Please configure it as a valid integer in environment variables.")
    API_ID = int(API_ID)

    API_HASH = os.environ.get("API_HASH")
    if not API_HASH:
        raise ValueError("API_HASH is not set. Please configure it in environment variables.")

    DATABASE_URI = os.environ.get("DATABASE_URI")
    if not DATABASE_URI:
        raise ValueError("DATABASE_URI is not set. Please configure it in environment variables.")

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

    AUTH_USERS = {int(user) for user in os.environ.get("AUTH_USERS", "").split() if user.isdigit()}
    if not AUTH_USERS:
        print("Warning: AUTH_USERS is not set. Commands will be accessible to all users.")

    SAVE_USER = os.environ.get("SAVE_USER", "no").lower() in ["yes", "true", "1"]

    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")

    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMAND", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMAND", "disconnect")

    BOT_START_TIME = time.time()

    # Debugging: Log all loaded environment variables (sensitive data redacted)
    print("[DEBUG] Configuration loaded:")
    print(f"TG_BOT_TOKEN: {'[REDACTED]' if TG_BOT_TOKEN else None}")
    print(f"API_ID: {API_ID}")
    print(f"API_HASH: {'[REDACTED]' if API_HASH else None}")
    print(f"DATABASE_URI: {'[REDACTED]' if DATABASE_URI else None}")
    print(f"DATABASE_NAME: {DATABASE_NAME}")
    print(f"AUTH_USERS: {AUTH_USERS}")
    print(f"SAVE_USER: {SAVE_USER}")

# Example usage
if __name__ == "__main__":
    try:
        print("Starting bot with the following configuration:")
        config = Config()
    except ValueError as e:
        print(f"Startup error: {e}")
