import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from client import RequestHandler

class TestRequestHandler(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        r = RequestHandler(data)

    def test_get(self):
        data["url"] = "http://localhost:8000/users/"
        t = r.get(url=data["url"], auth=("willian", "1q2w3e4r"))
        self.assertTrue("results" in t)

    def test_post(self):
        data["headers"] = {"content-type": "application/json"}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["payload"]["method"] = "JSONRPC.Ping"

        s = {u'jsonrpc': u'2.0', u'id': 1, u'result': u'pong'}
        t = r.post(data["payload"])
        self.assertEquals(t, s)

        data["payload"]["method"] = "JSONRPC.Version"
        s = {u'jsonrpc': u'2.0', u'id': 1, u'result': {u'version': {u'major': 6,
            u'minor': 14, u'patch': 3}}}
        t = r.post(data["payload"])
        self.assertEquals(t, s)

    if __name__ == "__main__":
        unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

