import os
from nestedict import  Nestedict

from vlc import  MediaPlayer, MediaListPlayer, MediaList
import config
NOTFOUND = "Not Found"

class Player:
    def __init__(self, dirs=[]):
        assert(isinstance(dirs, list) == True)
        self.dirs = dirs
        self.add_directory(config.url_location)
        self.add_directory(config.playlist_location)
        self.add_directory(config.uploaded_location)
        self.player = None

    def __del__(self):
        if self.player is not None:
            self.player.stop()


    def found_entry(self, entry):
        if entry.rsplit(".", 1)[1] == "url":
            return open(os.path.join(config.url_location, entry)).read().strip("\n")
        for directory in self.dirs:
            if entry in os.listdir(directory):
                return os.path.join(directory, entry)

    def list_available(self):
        ret = []
        for directory in self.dirs:
            try:
                for entry in os.listdir(directory):
                    if entry.rsplit(".", 1)[1] in ["url", "mp3", "wma", "wav", "m3u"]:
                        ret.append(entry)
            except OSError:#missing directories are not a problem
                pass
            return ret

    def list_available_nested_dict(self):
        d = None
        for directory in self.dirs:
            try:
                for entry in os.listdir(directory):
                    if entry.rsplit(".", 1)[1] in ["url", "mp3", "wma", "wav", "m3u"]:
                        fullname = os.path.relpath(os.path.join(directory, entry[:entry.rfind(".")]), config.base_dir)
                        if d is None:
                            d = Nestedict(fullname, 1)
                        else:
                            d.add_node(fullname, 1)
            except OSError:#missing directories are not a problem
                pass
        return d

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
            self.player.stop()
            self.player = None
        if isinstance(name, str) or isinstance(name, unicode):
            print str(self.found_entry(name))
            self.player = MediaPlayer(str(self.found_entry(name)))
        elif isinstance(name, list):
            playlist = MediaList()
            for entry in name:
                playlist.add_media(self.found_entry(entry))
            self.player = MediaListPlayer()
            self.player.set_media_list(playlist)
        if play:
            self.play()

if __name__ == '__main__':
    p = Player()
    print p.list_available_nested_dict()