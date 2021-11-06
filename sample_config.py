import os

class Config(object):
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # Array to store users who are authorized to use the bot
    DOWNLOAD_LOCATION = "./DOWNLOADS"
