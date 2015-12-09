import os
from vlc import  MediaPlayer, MediaListPlayer, MediaList
import config
NOTFOUND = "Not Found"

class Player:
    def __init__(self, dirs=[]):
        assert(isinstance(dirs, list) == True)
        self.dirs = dirs
        self.add_directory(config.url_location)
        self.add_directory(config.playlist_location)
        self.player = None

    def __del__(self):
        if self.player is not None:
            self.player.stop()


    def found_entry(self, entry):
        for directory in self.dirs:
            if entry in os.listdir(directory):
                return os.path.join(directory, entry)

    def add_directory(self, entry):
        if entry not in self.dirs:
            self.dirs.append(entry)

    def del_directory(self, entry):
        self.dirs.remove(entry)

    def get_directory(self, entry=None):
        if entry == None:
            return self.dirs
        if entry in self.dirs:
            return entry
        return NOTFOUND


    def pause(self):
        if self.player is not None:
            self.player.stop()

    def play(self):
        if self.player is not None:
            self.player.play()

    def stop(self):
        self.player.stop()

    def next(self):
        if isinstance(self.player, MediaListPlayer):
            self.player.next()

    def start(self, name, play=True):
        if self.player != None:
            self.player = None
        if isinstance(name, str):
            self.player = MediaPlayer(self.found_entry(name))
        elif isinstance(name, list):
            playlist = MediaList()
            for entry in name:
                playlist.add_media(self.found_entry(entry))
            self.player = MediaListPlayer()
            self.player.set_media_list(playlist)
        if play:
            self.play()
