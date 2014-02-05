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

    def get_permission(self):
        r = self.post(method="JSONRPC.Permission")
        if r and ("result" in r):
            return r["result"]
        else:
            return False

    def has_permission(self, permission):
        r = self.get_permission()
        if r and (permission in r):
            return r[permission]
        else:
            return False

    def ping(self):
        r = self.post("JSONRPC.Ping")
        if r and (r["result"] == u"pong"):
            return True
        else:
            return False

    def post(self, method, params={}):
        """
        .. todo:: Implement a better exception handling.
        """
        self.payload["method"] = method
        if params:
            self.payload["params"] = params
        try:
            r = requests.post(self.url, data=json.dumps(self.payload),
                    headers=self.headers)
        except requests.exceptions.ConnectionError:
            return False
        self.payload.pop("method", None)
        self.payload.pop("params", None)
        return r.json()

    def result_is_ok(self, r, ok=u"OK"):
        if r and ("result" in r):
            if r["result"] == ok:
                return True
        else:
            return False


    def version(self):
        """
        .. todo:: Implement exception handling.
        """
        r = self.post("JSONRPC.Version")
        if r and ("result" in r):
            return r["result"]["version"]
        else:
            return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

