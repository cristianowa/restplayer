import os
import shelve
import copy
import config
from nestedict import Nestedict
from player import NOTFOUND
import random

def extension(s):
    try:
        return s.rsplit(".", 1)[1]
    except:
        return ""


class DirManager:
    def __init__(self, dirs=[]):
        assert(isinstance(dirs, list) == True)
        self.dirs = dirs
        self.load_directories()
        self.add_directory(config.url_location)
        self.add_directory(config.playlist_location)
        self.add_directory(config.uploaded_location)

    def load_directories(self):
        if not os.path.exists(config.player_persistance):
            return
        d = shelve.open(config.player_persistance)
        for dr in d["dirs"]:
            self.add_directory(dr)
        d.close()

    def save_directories(self):
        d = shelve.open(config.player_persistance)
        d["dirs"] = self.get_directory()
        d.sync()
        d.close()

    def found_entry(self, entry):
        ext = extension(entry)
        try:
            if ext not in config.supported_extensions:
                return None
            if ext == "url":
                return open(os.path.join(config.url_location, entry)).read().strip("\n")
            for directory in self.dirs:
                try:
                    if entry in os.listdir(directory):
                        return os.path.join(directory, entry)
                except OSError:
                    pass
        except:
            return None
        return None

    def found_entries(self, directory):
        if directory not in self.dirs:
            return []
        entries = os.listdir(directory)
        for e in copy.copy(entries):
            if extension(e) not in config.supported_extensions:
                entries.remove(e)
        return entries

    def list_available(self):
        ret = {}
        for directory in self.dirs:
            try:
                try:
                    dirlist = os.listdir(directory)
                    dirlist.reverse()
                    for entry in dirlist:
                        ext = entry.rsplit(".", 1)
                        if len(ext) > 1 and ext[1] in ["url", "m3u"] + config.supported_extensions:
                            if directory not in ret.keys():
                                ret[directory] = []
                            ret[directory].append(entry)
                except IndexError:
                    pass
            except OSError:#missing directories are not a problem
                pass
        return ret

    def list_available_nested_dict(self):
        d = None
        for directory in self.dirs:
            try:
                for entry in os.listdir(directory):
                    try:
                        if entry.rsplit(".", 1)[1] in ["url", "m3u"] + config.supported_extensions:
                            path = os.path.split(directory)[1]
                            fullname = "/".join([path, entry])
                            if d is None:
                                d = Nestedict("all", 1)
                            d.add_node("all/" + fullname, 1)
                    except IndexError: #files without extensions should not break this
                        pass
            except OSError:#missing directories are not a problem
                pass
        return d

    def add_directory(self, entry):
        if entry not in self.dirs:
            self.dirs.append(entry)
        self.dirs = list(set(self.dirs))
        self.save_directories()

    def del_directory(self, entry):
        self.dirs.remove(entry)

    def get_directory(self, entry=None):
        if entry == None:
            return self.dirs
        if entry in self.dirs:
            return entry
        return NOTFOUND

    def random_list(self, directory=None):
        if directory is None:
            files = []
            for d in self.dirs:
                try:
                    files += [f for f in os.listdir(d)]
                except OSError:
                    pass
        else:
            files = os.listdir(directory)
        for f in files:
            if extension(f) not in config.supported_extensions:
                files.remove(f)
        random.shuffle(files)
        return files

dirmanager = DirManager()