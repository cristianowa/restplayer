import os
from vlc import  MediaPlayer

x = MediaPlayer("teste")
x.

class Player:
    def __init__(self, dirs=[]):
        assert(isinstance(dirs, list) == True)
        self.dirs = dirs

    def found_entry(self, entry):
        for directory in self.dirs:
            if entry in os.listdir(directory):
                return os.path.join(directory, entry)

    def add_directory(self, entry):
        if entry not in self.dirs:
            self.dirs.append(entry)

    def del_directory(self, entry):
        self.dirs.remove(entry)

    def pause(self):
        if self.player is not None:
            self.player.stop()

    def play(self):
        if self.player is not None:
            self.player

    def stop(self):
        self.player.stop()

    def start(self, name, play=True):
        if self.player != None:
            del self.player
        self.player = MediaPlayer(self.found_entry(name))
        if play:
            self.play()