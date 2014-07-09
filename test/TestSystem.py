import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from client import System

class TestSystem(unittest.TestCase):

    def setUp(self):
        global data
        global r
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://192.168.1.4:8080/jsonrpc"
        r = System(data)

    def test_get_properties(self):
        params = {"properties": ["canshutdown", "cansuspend", "canhibernate", \
        "canreboot"]}
        s = r.get_properties(params=params)
        print(s)
        self.assertTrue(s)

    def test_hibernate(self):
        params = {"properties": ["canhibernate"]}
        s = r.get_properties(params=params)
        if s[u"canhibernate"]:
            self.assertTrue(r.hibernate())
        # else:

    def test_reboot(self):
        params = {"properties": ["canreboot"]}
        s = r.get_properties(params=params)
        #if s[u"canreboot"]:
            #self.assertTrue(r.reboot())
        # else:

    def test_shutdown(self):
        params = {"properties": ["canshutdown"]}
        s = r.get_properties(params=params)
        #if s[u"canshutdown"]:
            #self.assertTrue(r.shutdown())
        #else:

    def test_suspend(self):
        params = {"properties": ["cansuspend"]}
        s = r.get_properties(params=params)
        if s[u"cansuspend"]:
            self.assertTrue(r.suspend())
        #else:

    if __name__ == "__main__":
        unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

