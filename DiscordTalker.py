import discord
import asyncio
import os
import time
import MusicPlayer
from YTdownloader import get_mp3_from_search_phrase
from YTdownloader import get_song_from_search_phrase

client = discord.Client()
player = MusicPlayer.MusicPlayer()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user = message.author
    if message.author == client.user:  # skip messages printed by the bot.
        return
    elif str(message.channel).strip() != "rhythm-beats":
        print("not in rhythm-beats channel")
        return
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
    elif message.content == "que":
        player.print_que()
    elif message.content == "mistake":
        player.skip_last_song()
    elif message.content == "stop":
        player.stop()
    elif user.voice is not None and user.voice.channel is not None :
        text_channel = message.channel
        song = get_song_from_search_phrase(message.content)
        if player.is_playing():  # if already playing, add to que
            player.add_song(song)
        else:  # attach player to class
                voice_channel = user.voice.channel
                # grab user's voice channel
                print("starting)")
                await player.start(voice_channel, text_channel, song)
    else:
        text_channel = message.channel
        await text_channel.send("not in an active voice channel")


client.run(token)
