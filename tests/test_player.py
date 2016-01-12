from unittest import TestCase, main
from player import Player
from dirmanager_ws import DirManager
import time
import vlc
import tempfile, os


class TestPlayer(TestCase):
    def test_pause(self):
        player = Player()
        #player.add_directory("../test_files/")
        #player.start("DOt_-_05_-_IMF.mp3")
        #time.sleep(4)  # take a bit to start
        #player.pause()
        self.assertTrue(True)
    def setUp(self):
        self.dm = DirManager()
        self.dm.add_directory("../test_files/")

    def tearDown(self):
        self.dm.del_directory("../test_files/")

    def test_play(self):
        player = Player()
        player.start([self.dm.found_entry("DOt_-_05_-_IMF.mp3")], play=False)
        player.play()
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))


    def test_stop(self):
        player = Player()
        player.start([self.dm.found_entry("DOt_-_05_-_IMF.mp3")])
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))
        player.stop()
        self.assertFalse(bool(player.player.is_playing()))

    def test_start(self):
        player = Player()
        player.start([self.dm.found_entry("DOt_-_05_-_IMF.mp3")], play=False)
        self.assertTrue(True)

    def test_start_playlist(self):
        player = Player()
        player.start([self.dm.found_entry(x) for x in ["Kriss_-_03_-_jazz_club.mp3", "DOt_-_05_-_IMF.mp3"]])
        time.sleep(4)  # take a bit to start
        self.assertTrue(isinstance(player.player, vlc.MediaListPlayer))

    def test_next(self):
        player = Player()
        player.start([self.dm.found_entry(x) for x in ["Kriss_-_03_-_jazz_club.mp3", "DOt_-_05_-_IMF.mp3"]])
        time.sleep(4)  # take a bit to start
        player.next()
        self.assertTrue(True)

    def test_current(self):
        player = Player()
        player.start([self.dm.found_entry("Kriss_-_03_-_jazz_club.mp3")])
        time.sleep(4)  # take a bit to start
        self.assertTrue(player.current(), "Kriss_-_03_-_jazz_club.mp3")

    def test_current_empty(self):
        player = Player()
        self.assertEqual(player.current(), "")
        player.start([self.dm.found_entry("Kriss_-_03_-_jazz_club.mp3")])
        time.sleep(2)  # take a bit to start
        player.stop()
        self.assertEqual(player.current(),"")

if __name__ == '__main__':
    main()
