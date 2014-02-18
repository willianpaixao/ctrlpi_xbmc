import os, sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
import RequestHandler

class TestUser(unittest.TestCase):

    def setUp(self):
        pass

    def test_user_auth(self):
        global data
        global r
        data = {}
        r = RequestHandler.RequestHandler(data)

        data["url"] = "http://localhost:8000/users/"
        t = r.get(url=data["url"], auth=("willian", "1q2w3e4r"))
        print(t)

    if __name__ == "__main__":
        unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

