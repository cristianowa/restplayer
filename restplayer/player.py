from vlc import  MediaPlayer, MediaListPlayer, MediaList

NOTFOUND = "Not Found"


class Player:
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