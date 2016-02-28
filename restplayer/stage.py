from common import sanitize
import os
import config
from dirmanager import dirmanager
import random

class Stage:
    def __init__(self):
        self.array = []

    def add(self, entry):
        if entry.rsplit(".", 1)[1] == "m3u":
            with open(os.path.join(config.playlist_location, entry)) as f:
                for music in f.readlines():
                    self.array.append(music.replace("\n", "").decode("UTF-8"))

        if dirmanager.found_entry(sanitize(entry)) is not None:
            self.array.append(entry)

    def adddir(self, entry):
        self.array += dirmanager.found_entries(entry)

    def addshuffle(self, entry=None):
        self.array = dirmanager.random_list(entry)

    def clear(self):
        self.array = []

    def createplaylist(self, filename):
        f = open(os.path.join(config.playlist_location, filename + ".m3u"), "w")
        entries = [x.encode("UTF-8") for x in self.array]
        text = "\n".join(entries)
        f.write(text)
        f.close()
    def shuffle(self):
        random.shuffle(self.array)

stage = Stage()