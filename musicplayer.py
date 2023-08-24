import asyncio

import discord

from foldersizehelper import get_music_folder_size


class MusicPlayer:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.status = "off"
        self.songs = []
        self.attached_player = None
        self.attached_text_channel = None
        self.states = ("off", "playing", "paused")
        self.active_song = ""

    def resume(self):
        self.attached_player.resume()
        self.status = self.states[1]

    def pause(self):
        self.attached_player.pause()
        self.status = self.states[2]

    def is_playing(self):
        return self.status != "off"

    def stop(self):
        player_ref = self.attached_player
        self.message("Stopping player")
        if self.attached_player.is_playing():
            self.attached_player.stop()
        asyncio.ensure_future(player_ref.disconnect())
        self.status = "off"

    async def start(self, channel, message_channel, initial_song):
        # todo clear all temp files
        self.status = self.states[1]
        # make sure you're not already in a voice channel playing stuff
        try:
            self.attached_player = await channel.connect()
        except (
            discord.errors.ClientException
        ):  # if already in a voice channel, just add the song to the queueue
            self.songs.append(initial_song)
        else:
            self.attached_player.play(
                discord.FFmpegPCMAudio(initial_song.filename), after=self.play_next_song
            )
            self.attached_text_channel = message_channel
            self.message("Player started!")
            size = get_music_folder_size()
            self.message("current space used is: " + str(size))

    def add_song(self, song):
        self.songs.append(song)
        self.message("there are now: " + str(len(self.songs)) + " in queue.")
        self.message("added: " + str(song))

    def play_next_song(self, error):
        print(error)
        if len(self.songs) > 0:
            next_song = self.songs.pop(0)
            next_song_filename = next_song.filename
            m2 = str(len(self.songs))
            self.active_song = next_song
            self.attached_player.play(
                discord.FFmpegPCMAudio(next_song_filename), after=self.play_next_song
            )
            self.message("now playing " + next_song_filename)
            self.message("there are " + m2 + " left in queue.")
        else:
            print("no more songs to play")
            self.stop()

    def message(self, message):
        if self.is_playing() and self.attached_text_channel is not None:
            asyncio.ensure_future(self.attached_text_channel.send(message))

    def skip_last_song(self):
        removed_song = self.songs.pop()
        message = "Removed " + str(removed_song.title) + " from queue"
        self.message(message)

    def skip_current_song(self):
        # stop playing
        if len(self.songs) > 0:
            self.attached_player.pause()
            self.play_next_song("skipped")
        else:
            self.stop()

    def skip_index(self, index):
        if index == 1:
            self.skip_current_song()
        elif index == len(self.songs) and index > 1:
            self.skip_last_song()
        else:
            self.songs.pop(index - 1)
        self.print_queue()

    def print_queue(self):
        total_duration = 0
        if len(self.songs) > 0:
            for index, song in enumerate(self.songs):
                message = str(index + 1) + ") " + song.title + " " + str(song.duration)
                message = f" {index +1} ) {song.title}  {song.duration}"
                total_duration += song.duration_in_minutes
                self.message(message)
            self.message(
                "total duration of songs in queue is approximately : "
                + str(round(total_duration))
                + " minutes"
            )
        else:
            self.message("queue is empty")
