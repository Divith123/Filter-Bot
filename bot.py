import os
import pyrogram

# Check if running in webhook mode
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config  # If running in webhook mode, use sample_config
else:
    from config import Config  # Otherwise, use config (fallback)

if __name__ == "__main__":
    # Define plugins directory
    plugins = dict(
        root="plugins"
    )

    # Initialize Pyrogram client
    app = pyrogram.Client(
        "filter_bot",
        bot_token="8000582879:AAGJzhmq5EmebvhC9DKQ1OgYDDsWGG9mmpM",  # Bot token must be a string
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )

    # Add specific authorized user (for testing or debugging)
    Config.AUTH_USERS.add(str(680815375))

    # Run the bot
    app.run()
