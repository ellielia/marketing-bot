import discord
import os
import json
from dotenv import load_dotenv
import datetime
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
                embed = discord.Embed(title="New economic news from NubBank", colour=discord.Colour(0xf144b3), url=message.jump_url, description=message.content, timestamp=datetime.datetime.utcfromtimestamp(datetime.datetime.utcnow().timestamp()))
                embed.set_author(name="NubBank Marketing", url="https://banking.nub.international", icon_url="https://bank.nub.international/img/logo_transparent_2.png")
                embed.set_footer(text="Sent by {0}".format(message.author.name), icon_url=message.author.avatar_url)
                # Check if there is an image
                attachments = message.attachments
                if len(attachments) > 0:
                    # Add image
                    embed.set_image(url=attachments[0].url)
                # Send embed
                await channel.send(embed=embed)
                print("Sent to {0}".format(channel.id))
            print("Finished!")

client = bot()
client.run(os.getenv('DISCORD_TOKEN'))

