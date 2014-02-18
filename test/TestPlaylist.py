import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
import Playlist

class TestPlaylist(unittest.TestCase):

    def setUp(self):
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.39:8080/jsonrpc"
        r = Playlist.Playlist(data)

    def test_clear(self):
        self.assertTrue(r.clear(params={"playlistid": 0}))
        self.assertTrue(r.clear(params={"playlistid": 1}))
        self.assertTrue(r.clear(params={"playlistid": 2}))

    def test_get_items(self):
        self.assertTrue(r.get_items(params={"playlistid": 0}))
        self.assertTrue(r.get_items(params={"playlistid": 1}))
        self.assertTrue(r.get_items(params={"playlistid": 2}))

    def test_get_playlists(self):
        s = [{u'playlistid': 0, u'type': u'audio'},
                {u'playlistid': 1, u'type': u'video'},
                {u'playlistid': 2, u'type': u'picture'}]
        t = r.get_playlists()
        self.assertTrue(t == s, msg="Playlists mismatch.")

    def test_get_playlist_properties(self):
        params={"playlistid": 0, "properties": ["type", "size"]}
        self.assertTrue(r.get_playlist_properties(params=params))
        params["playlistid"] = 1
        self.assertTrue(r.get_playlist_properties(params=params))
        params["playlistid"] = 2
        self.assertTrue(r.get_playlist_properties(params=params))

    if __name__ == "__main__":
        unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

