import discord
import os
import json
from dotenv import load_dotenv
load_dotenv()

class bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Detect if message is from correct channel
        if message.channel.id == int(os.getenv('DETECTION_CHANNEL_ID')):
            # Send off to channels
            print("Detected message, content: {0}".format(message.content))
            # Load channels
            with open('discord-channels.json') as f:
                channels = json.load(f)
            for channel in channels:
                # Get channel
                channel = client.get_channel(channel["channel"])
                # Post in channel
                await channel.send("{0} (From {1})".format(message.content, message.author))

client = bot()
client.run(os.getenv('DISCORD_TOKEN'))

