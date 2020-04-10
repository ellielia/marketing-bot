### marketing-bot

Discord.py bot for marketing in Discord channels (repost from one channel to others)

***

#### Set-Up

1. Install the `discord.py` and `python-dotenv` packages.
2. Create a `.env` file with the following content:
    ```
   DISCORD_TOKEN="<your token here>"
   DETECTION_CHANNEL_ID=<channel id here>
   ```
   The detection channel id is the channel the bot detects message from to post.
3. Create a json file name `discord-channels.json`. Create objects for each channel you wish for the bot to post messages in, for example:
    ```json
   [
     {
       "channel": <channel id here>
     },
     {
       "channel": <channel id here>
     },
   ]
   ```
4. Run the bot!

***

#### Contributors

* elliellia

