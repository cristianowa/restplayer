from unittest import TestCase, main
from test_utils import *
import tempfile, os
from dirmanager import DirManager


class TestDirManager(TestSetup):
    def test_found_entry(self):
        dirManager = DirManager()
        dirManager.add_directory(test_dir)
        ans = dirManager.found_entry(dot)
        self.assertTrue(ans == "../test_files/DOt_-_05_-_IMF.mp3")

    def test_add_directory(self):
        dirManager = DirManager()
        dirManager.add_directory("./teste/")
        self.assertTrue("./teste/" in dirManager.get_directory())
        self.assertTrue("./teste/" == dirManager.get_directory("./teste/"))

    def test_del_directory(self):
        dirManager = DirManager()
        dirManager.add_directory("./teste/")
        dirManager.del_directory("./teste/")
        self.assertFalse("./teste/" in dirManager.get_directory())
        self.assertFalse("./teste/" == dirManager.get_directory("./teste/"))

    def test_get_directory(self):
        dirManager = DirManager()
        dirManager.add_directory("./teste/")
        self.assertTrue("./teste/" in dirManager.get_directory())
        self.assertTrue("./teste/" == dirManager.get_directory("./teste/"))

    def test_available(self):
        dirManager = DirManager()
        self.assertTrue(isinstance(dirManager.list_available(), dict))

    def test_available_dict(self):
        dirManager = DirManager()
        json = dict(dirManager.list_available_nested_dict())
        self.assertTrue(isinstance(json, dict))

    def test_empty_dir(self):
        dirManager = DirManager()
        tmpdir = tempfile.mkdtemp()
        open(os.path.join(tmpdir,"test"), "w").close()
        open(os.path.join(tmpdir,"other"), "w").close()
        dirManager.add_directory(tmpdir)
        self.assertTrue(isinstance(dirManager.list_available(), dict))

if __name__ == '__main__':
    main()
