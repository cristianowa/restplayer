import config
import unittest
import tempfile
import re
from dirmanager import DirManager, dirmanager
test_dir = "../test_files/"
dot = "DOt_-_05_-_IMF.mp3"
kriss = "Kriss_-_03_-_jazz_club.mp3"
import os, shutil
from commands import getoutput as cmd

class TestSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global dirmanager
        config.base_dir = tempfile.mkdtemp()
        config.__reload__()
        dirmanager = DirManager()
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(config.base_dir)

class TestWithDir(TestSetup):
    def setUp(self):
        self.dm = DirManager()
        self.dm.add_directory(test_dir)

    def tearDown(self):
        self.dm.del_directory(test_dir)

def get_volume():
    val = cmd("amixer")
    ret = re.findall("Playback [0-9]* \[([0-9]*)%\] \[([\w]*)\]",val)
    return int(ret[0][0]), ret[0][1]