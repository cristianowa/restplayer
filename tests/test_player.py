from unittest import TestCase, main
from test_utils import *
from player import Player
import time
import vlc
import tempfile, os


class TestPlayer(TestWithDir):
    def test_pause(self):
        player = Player()
        #player.add_directory("../test_files/")
        #player.start(dot)
        #time.sleep(4)  # take a bit to start
        #player.pause()
        self.assertTrue(True)

    def test_play(self):
        player = Player()
        player.start([self.dm.found_entry(dot)], play=False)
        player.play()
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))


    def test_stop(self):
        player = Player()
        player.start([self.dm.found_entry(dot)])
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))
        player.stop()
        self.assertFalse(bool(player.player.is_playing()))

    def test_start(self):
        player = Player()
        player.start([self.dm.found_entry(dot)], play=False)
        self.assertTrue(True)

    def test_start_playlist(self):
        player = Player()
        player.start([self.dm.found_entry(x) for x in [kriss, dot]])
        time.sleep(4)  # take a bit to start
        self.assertTrue(isinstance(player.player, vlc.MediaListPlayer))

    def test_next(self):
        player = Player()
        player.start([self.dm.found_entry(x) for x in [kriss, dot]])
        time.sleep(4)  # take a bit to start
        player.next()
        self.assertTrue(True)

    def test_current(self):
        player = Player()
        player.start([self.dm.found_entry(kriss)])
        time.sleep(4)  # take a bit to start
        self.assertTrue(player.current(), kriss)

    def test_current_empty(self):
        player = Player()
        self.assertEqual(player.current(), "")
        player.start([self.dm.found_entry(kriss)])
        time.sleep(2)  # take a bit to start
        player.stop()
        self.assertEqual(player.current(),"")

if __name__ == '__main__':
    main()
