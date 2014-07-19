import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from media import Files

class TestFiles(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        r = Files(data)

    def test_prepare(self):
        params = {"path": "http://cdn.meme.li/instances/500x/52711161.jpg"}
        s = r.prepare(params=params)
        print(s)
        self.assertTrue(s)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

