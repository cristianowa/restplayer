from unittest import TestCase
from player import  Player
import time
import vlc

class TestPlayer(TestCase):
  def test_found_entry(self):
    player = Player()
    player.add_directory("./test_files/")
    ans = player.found_entry("DOt_-_05_-_IMF.mp3")
    self.assertTrue(ans == "./test_files/DOt_-_05_-_IMF.mp3")

  def test_add_directory(self):
    player = Player()
    player.add_directory("./teste/")
    self.assertTrue("./teste/" in player.get_directory())
    self.assertTrue("./teste/" == player.get_directory("./teste/"))

  def test_del_directory(self):
    player = Player()
    player.add_directory("./teste/")
    player.del_directory("./teste/")
    self.assertFalse("./teste/" in player.get_directory())
    self.assertFalse("./teste/" == player.get_directory("./teste/"))


  def test_get_directory(self):
    player = Player()
    player.add_directory("./teste/")
    self.assertTrue("./teste/" in player.get_directory())
    self.assertTrue("./teste/" == player.get_directory("./teste/"))

  def test_pause(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start("DOt_-_05_-_IMF.mp3")
    time.sleep(4)#take a bit to start
    player.pause()
    self.assertTrue(True)

  def test_play(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start("DOt_-_05_-_IMF.mp3", play=False)
    player.play()
    time.sleep(4)#take a bit to start
    self.assertTrue(True)

  def test_stop(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start("DOt_-_05_-_IMF.mp3", play=False)
    player.play()
    time.sleep(4)#take a bit to start
    self.assertTrue(True)
    player.stop()
    self.assertTrue(True)

  def test_start(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start("DOt_-_05_-_IMF.mp3", play=False)
    self.assertTrue(True)

  def test_start_playlist(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start(["Kriss_-_03_-_jazz_club.mp3","DOt_-_05_-_IMF.mp3" ])
    time.sleep(4)#take a bit to start
    self.assertTrue(isinstance(player.player, vlc.MediaListPlayer))

  def test_next(self):
    player = Player()
    player.add_directory("./test_files/")
    player.start(["Kriss_-_03_-_jazz_club.mp3","DOt_-_05_-_IMF.mp3" ])
    time.sleep(4)#take a bit to start
    player.next()
    self.assertTrue(True)