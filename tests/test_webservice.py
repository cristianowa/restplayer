import unittest
import webservice.start_ws
import test_utils
import json
test_app = webservice.start_ws.app.test_client()

valid_codes = [200,201,302]

class TestWSStatic(test_utils.TestSetup):

#  '/map/', '/',  , '/[filename]', '//[path:filename]'
    def test_main_page(self):
        rv = test_app.get("/")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        print(dir(test_app))
        print(dir(test_app.application))

    def test_static_file(self):
        rv = test_app.get("/player.html")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        rv = test_app.get("/bootstrap.min.css")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))



class TestWSPlayer(test_utils.TestSetup):
    def test_available_json(self):
        rv = test_app.get("/player/available.json")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        try:
            json.loads(rv.data)
        except:
            self.assertFalse(True, "Wrong json data")
#  '/player/current', '/player/pause', '/player/stop', '/player/play', '/player/next', '/player/prev',
    def test_available(self):
        url = "/player/available/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))


class TestWSControl(test_utils.TestSetup):
# '/control/directory/', '/control/createurl/', '/control/createurl/[entry]',
    def test_add_dir(self):
        url = "/control/directory/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        payload = {"text":"newdir"}
        test_app.post(url, content_type='multipart/form-data', data=payload)

    def test_upload_playlist(self):
        url = "/upload/playlist/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

    def test_upload(self):
        url = "/upload/music/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))


class TestWSStage(test_utils.TestSetup):
    def test_save(self):
        url = "/stage/save/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

    def test_clear(self):
        url = "/stage/clear/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

    def test_stage_json(self):
        rv = test_app.get("stage.json")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        try:
            json.loads(rv.data)
        except:
            self.assertFalse(True, "Wrong json data")

#  '/stage/clear/', '/stage/save/', '/stage.json', '/stage', '/stage/adddir/[entry]', '/stage/add/[entry]'


class TestWSVolume(test_utils.TestSetup):
    def test_volume_down(self):
        url = "/volume/down"
        prev_vol = test_utils.get_volume()[0]
        self.assertGreater(prev_vol, 0, "Please start the test with volume in 50%")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        self.assertLess(test_utils.get_volume()[0], prev_vol)

    def test_volume_up(self):
        url = "/volume/up"
        prev_vol = test_utils.get_volume()[0]
        self.assertLess(prev_vol, 100, "Please start the test with volume in 50%")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        self.assertGreater(test_utils.get_volume()[0], prev_vol)

    def test_volume_off(self):
        url = "/volume/off"
        self.assertEqual(test_utils.get_volume()[1], "on", "Please start the test with volume turned on")
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        self.assertEqual(test_utils.get_volume()[1], "off")

if __name__ == '__main__':
    unittest.main()
