import unittest
import webservice.start_ws
import test_utils
import json
test_app = webservice.start_ws.app.test_client()

valid_codes = [200,201,301, 302]

class TestWSStatic(test_utils.TestSetup):
    def test_main_page(self):
        rv = test_app.get("/")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

    def test_static_file(self):
        rv = test_app.get("/player.html")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        rv = test_app.get("/bootstrap.min.css")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

    def test_map(self):
        rv = test_app.get("/map")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))

class TestWSPlayer(test_utils.TestSetup):
    def test_available_json(self):
        rv = test_app.get("/player/available.json")
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        try:
            json.loads(rv.data)
        except:
            self.assertFalse(True, "Wrong json data")
    def test_current(self):
        url = '/player/current'
        #TODO:write test
    def test_pause(self):
        url = '/player/pause'
        #TODO:write test
    def test_stop(self):
        url = '/player/stop'
        #TODO:write test
    def test_play(self):
        url = '/player/play'
        #TODO:write test
    def test_next(self):
        url = '/player/next'
        #TODO:write test
    def test_prev(self):
        url = '/player/prev',
        #TODO:write test
    def test_available(self):
        url = "/player/available/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))


class TestWSControl(test_utils.TestSetup):
    def test_add_dir(self):
        url = "/control/directory/"
        rv = test_app.get(url)
        self.assertTrue(rv.status_code in valid_codes, "Wrong return code. Code was : " + str(rv.status_code))
        payload = {"text":"newdir"}
        test_app.post(url, content_type='multipart/form-data', data=payload)

    def test_create_url(self):
        url = "/control/createurl/"
        #TODO:write test

    def test_create_url_entry(self):
        url = "/control/createurl/newurl"
        #TODO:write test

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
    def test_stage(self):
        url = '/stage'
        #TODO:write test
    def test_adddir(self):
        url = '/stage/adddir/' + test_utils.test_dir
        #TODO:write test
    def test_add(self):
        url = '/stage/add/' + test_utils.dot
        #TODO:write test

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
