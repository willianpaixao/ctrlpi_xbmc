"""
Created on 31 January 2014
"""

import requests
import json

class JSONRPC(object):
    """
    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        self.url = object["url"]
        self.headers = object["headers"]
        self.payload = object["payload"]

    def get_permission(self): return self.post(method="JSONRPC.Permission")

    def has_permission(self, permission):
        p = self.get_permission()
        return p["result"][permission]

    def ping(self):
        p = self.post("JSONRPC.Ping")
        if p["result"] == u'pong':
            return True
        else:
            return False

    def post(self, method, params={}):
        self.payload["method"] = method
        if params:
            self.payload["params"] = params
        r = requests.post(self.url, data=json.dumps(self.payload),
                headers=self.headers)
        self.payload.pop("method", None)
        self.payload.pop("params", None)
        return r.json()

    def version(self):
        r = self.post("JSONRPC.Version")
        return r["result"]["version"]

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

