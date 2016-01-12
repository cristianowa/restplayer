from playlist import *

import unittest
import tempfile
import os
class TestPlaylist(unittest.TestCase):
    def test_save(self):
        tmp = tempfile.mktemp()
        tmp=tmp[tmp.rfind("/") +1:]
        plist = ["foo.mp3","foo2.mp3","another.mp4"]
        createplaylist(plist, tmp)
        name = os.path.join(config.playlist_location,tmp +".m3u")
        self.assertTrue(os.path.exists(name))
        lines = open(name).read().splitlines()
        for l,p in zip(lines,plist):
            self.assertEqual(l,p)
        os.remove(name)


if __name__ == '__main__':
    unittest.main()
