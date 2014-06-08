import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from media import VideoLibrary

class TestVideoLibrary(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        r = VideoLibrary(data)

    def test_clean(self):
        self.assertTrue(r.clean())

    def test_export(self):
        self.assertTrue(r.export())
        self.assertTrue(r.export(params={u"options": {u"path": u"/tmp"}}))

    def test_get_episodes(self):
        msg="Video library not retrieved."
        s = {u'limits': {u'start': 0, u'total': 0, u'end': 0}}
        t = r.get_episodes()
        self.assertGreaterEqual(t[u"limits"][u"total"], 0, msg=msg)

    def test_get_movies(self):
        msg="Video library not retrieved."
        s = {u'limits': {u'start': 0, u'total': 0, u'end': 0}}
        t = r.get_movies()
        self.assertGreaterEqual(t[u"limits"][u"total"], 0, msg=msg)

    def test_get_movie_details(self):
        t = r.get_movies()
        i = t[u"limits"][u"total"]
        for j in xrange(1, i + 1):
            t = r.get_movie_details(params={"movieid": j})
            print(t[u"moviedetails"])

    def test_get_recently_added_movies(self):
        t = r.get_recently_added_movies()
        i = t[u"limits"][u"total"]
        for j in xrange(1, i + 1):
            t = r.get_movie_details(params={"movieid": j})
            print(t[u"moviedetails"])

    def test_get_tvshows(self):
        msg="Video library not clean."
        s = {u'limits': {u'start': 0, u'total': 0, u'end': 0}}
        t = r.get_tvshows()
        self.assertTrue(t == s, msg=msg)

    def test_scan(self):
        self.assertTrue(r.scan())

    if __name__ == "__main__":
        unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

