import os
import pyrogram

# Dynamically import Config based on the environment
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config  # For webhook-based deployment (e.g., Heroku)
else:
    from config import Config  # For local deployment

if __name__ == "__main__":
    # Specify plugin directory
    plugins = dict(
        root="plugins"
    )

    # Create Pyrogram Client instance
    app = pyrogram.Client(
        "filter_bot",               # Session name
        bot_token=Config.TG_BOT_TOKEN,  # Bot token from BotFather
        api_id=Config.API_ID,          # API ID from my.telegram.org
        api_hash=Config.API_HASH,      # API Hash from my.telegram.org
        plugins=plugins,               # Plugin root directory
        workers=300                    # Number of worker threads for handling updates
    )

    # Add a default authorized user (ensure Config.AUTH_USERS exists and is mutable)
    Config.AUTH_USERS.add(680815375)

    # Run the bot
    app.run()
