import config
import os
def createplaylist(entries, filename):
    """

    :param entries: list of files with fullpath included or urls
    :param filename:file to create, it will be putted in the playlist
    :return:
    """
    open(os.path.join(config.playlist_location, filename + ".m3u"), "w").writelines(entries)