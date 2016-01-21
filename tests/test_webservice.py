import unittest
import webservice.start_ws
import test_utils
import json
test_app = webservice.start_ws.app.test_client()

valid_codes = [ 200,201,302]

class TestWebservice(test_utils.TestSetup):
# '/control/directory/', '/control/createurl/', '/control/createurl/[entry]',
#   '/upload/playlist/',  '/upload/music/',
#  '/player/available.json', '/player/available/',
#  '/player/current', '/player/pause', '/player/stop', '/player/play', '/player/next', '/player/prev',
#  '/volume/down', '/volume/off', '/volume/up',
#  '/stage/clear/', '/stage/save/', '/stage.json', '/stage', '/stage/adddir/[entry]', '/stage/add/[entry]'
#  '/map/', '/',  , '/[filename]', '//[path:filename]'
    def test_main_page(self):
        rv = test_app.get("/")
        self.assertTrue(rv.status_code in valid_codes)
        print(dir(test_app))
        print(dir(test_app.application))

    def test_available_json(self):
        rv = test_app.get("/player/available.json")
        self.assertTrue(rv.status_code in valid_codes)
        try:
            json.loads(rv.data)
        except:
            self.assertFalse(True, "Wrong json data")

    def test_add_dir(self):
        url = "/control/directory/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)
        #rv = test_app.post(url, )
        #TODO: what is the format that cames in the post ?

    def test_upload(self):
        url = "/upload/music/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)

    def test_save(self):
        url = "/stage/save/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)

    def test_clear(self):
        url = "/stage/clear/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)

    def test_volume_down(self):
        url = "/volume/down"
        prev_vol = test_utils.get_volume()[0]
        self.assertGreater(prev_vol, 0, "Please start the test with volume in 50%")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)
        self.assertLess(test_utils.get_volume()[0], prev_vol)

    def test_volume_up(self):
        url = "/volume/up"
        prev_vol = test_utils.get_volume()[0]
        self.assertLess(prev_vol, 100, "Please start the test with volume in 50%")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)
        self.assertGreater(test_utils.get_volume()[0], prev_vol)

    def test_volume_off(self):
        url = "/volume/off"
        self.assertEqual(test_utils.get_volume()[1], "on", "Please start the test with volume turned on")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes)
        self.assertEqual(test_utils.get_volume()[1], "off")

if __name__ == '__main__':
    unittest.main()
