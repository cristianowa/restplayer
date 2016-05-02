import config


NOTFOUND = "Not Found"

import subprocess
import signal
from commands import getstatusoutput as cmd

class Mpg123Player:
    def __init__(self):
        ret, val = cmd("which mpg123")
        assert ret == 0, "Mpg123 not available"
        self.p = None
        self.list = None
    def __del__(self):
        if self.p is not None:
            self.p.kill()

    def pause(self):
        if self.p is not None:
            self.p.kill()

    def play(self):
        if self.p is not None:
            self.p.kill()
        self.p = subprocess.Popen(["mpg123"] + self.list)
    def stop(self):
        if self.p is not None:
            self.p.kill()
            self.p = None

    def next(self):
        self.p.send_signal(signal.SIGINT)

    def start(self, name, play=True):
        assert(isinstance(name, list))
        self.list = name
        if play:
            self.play()

    def current(self):
        return "Not Available for Mpg123"

    def is_playing(self):
        return self.p is not None


from vlc import  MediaPlayer, MediaListPlayer, MediaList
class VlcPlayer:
    def __init__(self):
        self.player = None
        self.mediaplayer = None

    def __del__(self):
        if self.player is not None:
            self.player.stop()

    def pause(self):
        if self.mediaplayer is not None:
            self.mediaplayer.pause()

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
        self.mediaplayer = MediaPlayer()
        assert(isinstance(name, list))
        playlist = MediaList()
        for entry in name:
            if entry is not None:
                playlist.add_media(entry)
        self.player = MediaListPlayer()
        self.player.set_media_list(playlist)
        self.player.set_media_player(self.mediaplayer)
        if play:
            self.play()

    def current(self):
        try:
            if self.mediaplayer.is_playing():
                return self.mediaplayer.get_media().get_meta(0)
            return ""
        except:
            return ""

    def is_playing(self):
        return self.player.is_playing()

player_choices = {
    "vlc" : VlcPlayer,
    "mpg123" : Mpg123Player
}
try:
    Player = player_choices[config.player_choice]
except:
    Player = Mpg123Player