import os
import pyrogram

# Define the actual values directly in the code (not recommended for production)
TELEGRAM_BOT_TOKEN = "8000582879:AAGJzhmq5EmebvhC9DKQ1OgYDDsWGG9mmpM"
API_ID = 22147229
API_HASH = "178464a9d58e0c5948fc1f1134a7415b"
AUTH_USERS = {"2133843296"}  # Add user IDs in a set
DATABASE_URI = "mongodb+srv://hustleronduty:ninja%402654@cluster0.v6xn9.mongodb.net/"
DATABASE_NAME = "Cluster0"
HEROKU_API_KEY = "HRKU-f89d9d81-de23-4110-ae49-9f9c3182fffe"
SAVE_USER = "no"  # or "yes" based on your use case

if __name__ == "__main__":
    # Define plugins directory
    plugins = dict(
        root="plugins"
    )

    # Initialize Pyrogram client with actual values
    app = pyrogram.Client(
        "filter_bot",
        bot_token=TELEGRAM_BOT_TOKEN,  # Actual bot token
        api_id=API_ID,  # Actual API ID
        api_hash=API_HASH,  # Actual API Hash
        plugins=plugins,
        workers=300
    )

    # Add specific authorized user (for testing or debugging)
    AUTH_USERS.add(str(680815375))  # Add a test user ID (optional)

    # Run the bot
    app.run()
