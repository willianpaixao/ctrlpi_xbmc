import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from media import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        r = Player(data)

    def test_get_active_players(self):
        s = r.get_active_players()
        print(s)
        self.assertTrue(s)

    def test_get_item(self):
        s = r.get_item(params={u"playerid": 1})
        print(s)
        self.assertTrue(s)

    def test_get_properties(self):
        params={
            u"playerid": 1, u"properties": [u"canrepeat", u"canmove", \
            u"canshuffle", u"speed", u"percentage", u"playlistid", u"audiostreams", \
            u"position", u"repeat", u"currentsubtitle", u"canrotate", u"canzoom", \
            u"canchangespeed", u"type", u"partymode", u"subtitles", u"canseek", \
            u"time", u"totaltime", u"shuffled", u"currentaudiostream", u"live", \
            u"subtitleenabled"] \
        }
        s = r.get_properties(params=params)
        print(s)
        self.assertTrue(s)

    def test_play_pause(self):
        s = r.play_pause(params={u"playerid": 1})
        print(s)
        self.assertTrue(s)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

