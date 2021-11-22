import discord
import asyncio
import os
import time
from dotenv import load_dotenv
from musicplayer import MusicPlayer
from ytdownloader import get_song_from_search_phrase

client = discord.Client()
player = MusicPlayer()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user = message.author
    if message.author == client.user:  # skip messages printed by the bot.
        pass
        # do nothing i guess lolz
    elif str(message.channel).strip() != "rhythm-beats":
        print("not in rhythm-beats channel")
    elif message.content == "skip":
        print("regular skip")
        player.skip_current_song()
    elif message.content.startswith("skipx"):
        try:
            parts = message.content.strip().split(" ")
            pos_to_skip = int(parts[1])
            player.skip_index(pos_to_skip)
            print("special skip")
        except:
            await message.channel.send("postion to skip couldn't be parsed")
    elif message.content == "queue":
        player.print_queue()
    elif message.content == "mistake":
        player.skip_last_song()
    elif message.content == "stop":
        player.stop()
    elif user.voice is not None and user.voice.channel is not None :
        text_channel = message.channel
        song = get_song_from_search_phrase(message.content)
        # todo add if test to player.add_song() which either starts() or just adds?
        # shouldn't be a problem to have add_song as an async function
        if player.is_playing():  # if already playing, add to queueue
            player.add_song(song)
        else:  # attach player to class
                voice_channel = user.voice.channel
                # grab user's voice channel
                print("starting)")
                await player.start(voice_channel, text_channel, song)
    else:
        text_channel = message.channel
        await text_channel.send("not in an active voice channel")

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")
client.run("ODcxNDI2NzIyNDA5NjM1ODQw.YQbJYA.qA58c_wyzJhgpSMQGkObdaKN_uU")