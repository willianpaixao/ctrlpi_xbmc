import RequestHandler

class JSONRPC(object):
    """
    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        global data
        data = object

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
        data["payload"]["method"] = method
        if params:
            data["payload"]["params"] = params
        try:
            r = RequestHandler.RequestHandler(data)
            s = r.post(data["payload"])
        except requests.exceptions.ConnectionError:
            return False
        data["payload"].pop("method", None)
        data["payload"].pop("params", None)
        return s

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

