from test_utils import *
from stage import Stage
import stage
import unittest
import copy

class TestPlaylist(TestWithDir):
    def test_add(self):
        stage = Stage()
        stage.add(dot)
        stage.add(kriss)
        self.assertMusicIn(stage)

    def assertMusicIn(self, stg):
        self.assertTrue(dot in stg.array)
        self.assertTrue(kriss in stg.array)

    def test_adddir(self):
        stage = Stage()
        stage.adddir(test_dir)
        self.assertMusicIn(stage)

    def test_clear(self):
        stage = Stage()
        stage.add(dot)
        stage.add(kriss)
        stage.clear()
        self.assertTrue(dot not in stage.array)
        self.assertTrue(kriss not in stage.array)

    def test_playlist(self):
        stage = Stage()
        stage.add(dot)
        stage.add(kriss)
        stage.createplaylist("test")
        stage.clear()
        self.assertEqual(len(stage.array),0)
        stage.add("test.m3u")
        self.assertMusicIn(stage)

    def test_shuffle(self):
        stage = Stage()
        for i in range(5):
            stage.add(dot)
            stage.add(kriss)
        prev = copy.copy(stage.array)
        stage.shuffle()
        self.assertFalse(prev == stage.array)
        prev.sort()
        stage.array.sort()
        self.assertTrue(prev == stage.array)

    def test_add_random(self):
        stage = Stage()
        stage.addshuffle(test_dir)
        self.assertMusicIn(stage)

    def test_add_random_empty(self):
        stg = Stage()
        dirmanager.add_directory(test_dir)
        stg.addshuffle()
        self.assertMusicIn(stg)

if __name__ == '__main__':
    unittest.main()
