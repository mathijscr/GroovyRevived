import youtube_dl
import re
import Song


def download_mp3_from_yt(url, file_location):
    """
    This functions downloads the audio of a youtube url, encoded as mp3, to a specific file lcoation
    :param url: url of the youtube video
    :param file_location: filename and location of where the file should be saved
    :return: on success, returns file location
    """
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }], 'outtmpl': file_location}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return file_location


def find_top_yt_url(phrase):
    """
    This functions finds the first video associated with a certain search term on youtube
    :param phrase: the search phrase
    :return: a dict containing the url,title and duration of the video
    """
    from youtubesearchpython import VideosSearch
    VSresult = VideosSearch(phrase, limit=1)
    parsed_result = VSresult.result()["result"][0]
    url = parsed_result["link"]
    title = parsed_result["title"]
    duration = parsed_result["duration"]
    return_dict = {"url": url, "title": title, "duration": duration}
    return return_dict


def get_mp3_from_search_phrase(phrase):
    search_results = find_top_yt_url(phrase)
    file_name = search_results["title"]
    file_name = re.sub(r'[^\w\s-]', '', file_name.lower())
    file_name = re.sub(r'[-\s]+', '-', file_name).strip('-_')
    file_name = "music/"+file_name + ".mp3"
    yt_url = search_results["url"]
    print("params are: ",yt_url,file_name)
    download_mp3_from_yt(yt_url,file_name)
    return file_name


def get_song_from_search_phrase(phrase):
    search_results = find_top_yt_url(phrase)
    title = search_results["title"]
    url = search_results["url"]
    duration = search_results["duration"]
    file_name = search_results["title"]
    file_name = re.sub(r'[^\w\s-]', '', file_name.lower())
    file_name = re.sub(r'[-\s]+', '-', file_name).strip('-_')
    file_name = "music/"+file_name + ".mp3"
    yt_url = search_results["url"]
    print("params are: ",yt_url,file_name)
    download_mp3_from_yt(yt_url,file_name)
    resulting_song = Song.Song(title, file_name, duration, url )
    return resulting_song

