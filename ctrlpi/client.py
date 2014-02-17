import json
import requests

class RequestHandler(object):

    def __init__(self, object):
        global data
        data = object

    def get(self, url, auth=None):
        r = requests.get(url=url, auth=auth)
        return r.text

    def post(self, payload):
        """
        .. todo:: Implement a better exception handling.
        """
        try:
            r = requests.post(url=data["url"], data=json.dumps(payload),
                    headers=data["headers"])
        except requests.exceptions.ConnectionError:
            return False
        return r.json()

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
            r = RequestHandler(data)
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

class System(JSONRPC):
    """
    .. class:: System.System

    Controls the basic state of XMBC system.

    Inherits from *JSONRPC* class.

    .. todo:: Implement failing procedure.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(System, self).__init__(object)

    def get_properties(self, params = {"properties": ["canshutdown",
        "cansuspend", "canhibernate", "canreboot"]}):
        r = self.post(method="System.GetProperties", params=params)
        if r and ("result" in r):
            return r["result"]
        else:
            return False

    def hibernate(self):
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["canhibernate"]})
            if r["canhibernate"]:
                r = self.post(method="System.Hibernate")
                if r["result"] == u"OK":
                    return True
                else:
                    return False
        return False

    def reboot(self):
        if self.has_permission(permission="ControlPower"):
            r = self.post(method="System.Reboot")
            if r["result"] == u"OK":
                return True
            else:
                return False

    def shutdown(self):
        """
        Turn off the client.
        """
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["canshutdown"]})
            if r["canshutdown"]:
                r = self.post(method="System.Shutdown")
                if r["result"] == u"OK":
                    return True
                else:
                    return False
        return False

    def suspend(self):
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["cansuspend"]})
            if r["cansuspend"]:
                r = self.post(method="System.Suspend")
                if r["result"] == u"OK":
                    return True
                else:
                    return False
        return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

