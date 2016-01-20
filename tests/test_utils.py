import config
import unittest
import tempfile
from dirmanager import DirManager
test_dir = "../test_files/"
dot = "DOt_-_05_-_IMF.mp3"
kriss = "Kriss_-_03_-_jazz_club.mp3"
import os, shutil

class TestSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config.base_dir = tempfile.mkdtemp()
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(config.base_dir)

class TestWithDir(TestSetup):
    def setUp(self):
        self.dm = DirManager()
        self.dm.add_directory(test_dir)

    def tearDown(self):
        self.dm.del_directory(test_dir)