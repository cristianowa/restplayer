from unittest import TestCase, main
from test_utils import *
from player import Player, VlcPlayer, Mpg123Player
import time
import vlc
import tempfile, os


class TestPlayer(TestWithDir):
    player = Player
    def test_pause(self):
        player = self.player()
        #player.add_directory("../test_files/")
        #player.start(dot)
        #time.sleep(4)  # take a bit to start
        #player.pause()
        self.assertTrue(True)

    def test_play(self):
        player = self.player()
        player.start([self.dm.found_entry(dot)], play=False)
        player.play()
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.is_playing()))



    def test_stop(self):
        player = self.player()
        player.start([self.dm.found_entry(dot)])
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.is_playing()))
        player.stop()
        self.assertFalse(bool(player.is_playing()))

    def test_start_false(self):
        player = self.player()
        player.start([self.dm.found_entry(dot)], play=False)
        self.assertFalse(player.is_playing())

    def test_start(self):
        player = self.player()
        player.start([self.dm.found_entry(dot)], play=True)
        self.assertTrue(player.is_playing())

    def test_next(self):
        player = self.player()
        player.start([self.dm.found_entry(x) for x in [kriss, dot]])
        time.sleep(4)  # take a bit to start
        player.next()
        self.assertTrue(True)

    def test_current(self):
        player = self.player()
        player.start([self.dm.found_entry(kriss)])
        time.sleep(4)  # take a bit to start
        self.assertTrue(player.current(), kriss)

    def test_current_empty(self):
        player = self.player()
        self.assertEqual(player.current(), "")
        player.start([self.dm.found_entry(kriss)])
        time.sleep(2)  # take a bit to start
        player.stop()
        self.assertEqual(player.current(),"")


class TestVlcPlayer(TestPlayer):
    player = VlcPlayer
    def test_start_playlist(self):
        player = self.player()
        player.start([self.dm.found_entry(x) for x in [kriss, dot]])
        time.sleep(4)  # take a bit to start
        self.assertTrue(isinstance(player.player, vlc.MediaListPlayer))
        
class TestMpg123Player(TestPlayer):
    player = Mpg123Player

if __name__ == '__main__':
    main()
