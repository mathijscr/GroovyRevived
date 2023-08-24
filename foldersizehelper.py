import os

from humanize import naturalsize


def get_music_folder_size():
    total = 0
    path = "./music/"
    list_of_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root, file))

    for f in list_of_files:
        total += os.path.getsize(f)

    readable_result = naturalsize(total)
    return readable_result
