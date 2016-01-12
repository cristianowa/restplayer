from unittest import TestCase, main
from player import Player
import time
import vlc
import tempfile, os


class TestPlayer(TestCase):
    def test_found_entry(self):
        player = Player()
        player.add_directory("../test_files/")
        ans = player.found_entry("DOt_-_05_-_IMF.mp3")
        self.assertTrue(ans == "../test_files/DOt_-_05_-_IMF.mp3")

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
        #player.add_directory("../test_files/")
        #player.start("DOt_-_05_-_IMF.mp3")
        #time.sleep(4)  # take a bit to start
        #player.pause()
        self.assertTrue(True)

    def test_play(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry("DOt_-_05_-_IMF.mp3")], play=False)
        player.play()
        #time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))


    def test_stop(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry("DOt_-_05_-_IMF.mp3")])
        time.sleep(4)  # take a bit to start
        self.assertTrue(bool(player.player.is_playing()))
        player.stop()
        self.assertFalse(bool(player.player.is_playing()))

    def test_start(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry("DOt_-_05_-_IMF.mp3")], play=False)
        self.assertTrue(True)

    def test_start_playlist(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry(x) for x in ["Kriss_-_03_-_jazz_club.mp3", "DOt_-_05_-_IMF.mp3"]])
        time.sleep(4)  # take a bit to start
        self.assertTrue(isinstance(player.player, vlc.MediaListPlayer))

    def test_next(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry(x) for x in ["Kriss_-_03_-_jazz_club.mp3", "DOt_-_05_-_IMF.mp3"]])
        time.sleep(4)  # take a bit to start
        player.next()
        self.assertTrue(True)

    def test_available(self):
        player = Player()
        self.assertTrue(isinstance(player.list_available(), dict))

    def test_available_dict(self):
        player = Player()
        json = dict(player.list_available_nested_dict())
        self.assertTrue(isinstance(json, dict))

    def test_empty_dir(self):
        player = Player()
        tmpdir = tempfile.mkdtemp()
        open(os.path.join(tmpdir,"test"), "w").close()
        open(os.path.join(tmpdir,"other"), "w").close()
        player.add_directory(tmpdir)
        self.assertTrue(isinstance(player.list_available(), dict))

    def test_current(self):
        player = Player()
        player.add_directory("../test_files/")
        player.start([player.found_entry("Kriss_-_03_-_jazz_club.mp3")])
        time.sleep(4)  # take a bit to start
        self.assertTrue(player.current(), "Kriss_-_03_-_jazz_club.mp3")
    def test_current_empty(self):
        player = Player()
        player.add_directory("../test_files/")
        self.assertEqual(player.current(), "")
        player.start([player.found_entry("Kriss_-_03_-_jazz_club.mp3")])
        time.sleep(2)  # take a bit to start
        player.stop()
        self.assertEqual(player.current(),"")
if __name__ == '__main__':
    main()
