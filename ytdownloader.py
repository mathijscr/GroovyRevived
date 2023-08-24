import re
from song import Song
from youtubesearchpython import VideosSearch
import asyncio
from pytube import YouTube


def download_mp3_from_yt(url, file_location):
    """
    This functions downloads the audio of a youtube url, encoded as mp3, to a specific file lcoation
    :param url: url of the youtube video
    :param file_location: filename and location of where the file should be saved
    :return: on success, returns file location
    """

    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=file_location)
        print("The video is downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")
    return file_location


def find_top_yt_url(phrase):
    """
    This functions finds the first video associated with a certain search term on youtube
    :param phrase: the search phrase
    :return: a dict containing the url,title and duration of the video
    """

    vs_result = VideosSearch(phrase, limit=1)
    parsed_result = vs_result.result()["result"][0]
    url = parsed_result["link"]
    title = parsed_result["title"]
    duration = parsed_result["duration"]
    return_dict = {"url": url, "title": title, "duration": duration}
    return return_dict


def get_song_from_search_phrase(phrase):
    search_results = find_top_yt_url(phrase)
    title = search_results["title"]
    url = search_results["url"]
    duration = search_results["duration"]
    file_name = "music/" + title + ".mp3"
    yt_url = search_results["url"]
    download_mp3_from_yt(yt_url, file_name)
    resulting_song = Song(title, file_name, duration, url)
    return resulting_song

