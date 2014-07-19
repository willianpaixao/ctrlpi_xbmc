import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from client import JSONRPC

class TestJSONRPC(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        r = JSONRPC(data)

    def test_get_configuration(self):
        """
        Not working in Raspbmc. Returning False.
        """
        s = r.get_configuration()
        self.assertTrue(s)

    def test_get_permission(self):
        s = r.get_permission()
        print(s)
        self.assertTrue(s)

    def test_introspect(self):
        s = r.instrospect(params={u"getdescriptions": "True"})
        print(s)
        self.assertTrue(s)
        s = r.instrospect(params={u"getmetadata": "True"})
        print(s)
        self.assertTrue(s)
        s = r.instrospect(params={u"filterbytransport": "True"})
        print(s)
        self.assertTrue(s)

    def test_notify_all(self):
        params={"sender": "test sender",
            "message": "I still don't know where this message is going to."
        }
        s = r.notify_all(params=params)
        self.assertTrue(s)

    def test_ping(self):
        s = r.ping()
        self.assertTrue(s)

    def test_version(self):
        s = r.version()
        print(s)
        self.assertTrue(s)

