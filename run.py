import logging
from environs import Env
from os import listdir
from os.path import exists, join
from datetime import date, datetime
from discord import (Client as DiscordClient,
                     Intents as DiscordIntents,
                     File as DiscordFile)

env = Env()
env.read_env()

DISCORD_TOKEN = env.str("DISCORD_TOKEN")
CHANNEL_ID = env.int("CHANNEL_ID")
IMAGE_FOLDER = env.str("IMAGE_FOLDER")
START_DATE = datetime.strptime(env.str("START_DATE"), "%Y-%m-%d").date()
LOG_FILE = env.str("LOG_FILE")

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
logging.info(f"Running script at {datetime.now()}")

client = DiscordClient(intents = DiscordIntents.default())

@client.event
async def on_ready():
    try:
        if not exists(IMAGE_FOLDER):
            raise FileNotFoundError(f"The folder {IMAGE_FOLDER} does not exist.")

        files = sorted(listdir(IMAGE_FOLDER))

        if not files:
            raise ValueError(f"No files found in {IMAGE_FOLDER}.")

        today = date.today()
        days_passed = (today - START_DATE).days
        index = days_passed % len(files)
        image_path = join(IMAGE_FOLDER, files[index])

        if not exists(image_path):
            raise FileNotFoundError(f"Image file {image_path} does not exist.")

        channel = client.get_channel(CHANNEL_ID)
        if not channel:
            raise LookupError(f"Channel with ID {CHANNEL_ID} not found.")

        await channel.send(file=DiscordFile(image_path))

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.close()

client.run(token=DISCORD_TOKEN)
