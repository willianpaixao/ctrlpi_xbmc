import json
import requests

class JSONRPC(object):
    """
    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        global data
        data = object

    def get_configuration(self):
        """
        This method isn't working in Raspbmc.
        """
        r = self.post(method="JSONRPC.GetConfiguration")
        return self.result_is_ok(r)

    def get_permission(self):
        r = self.post(method="JSONRPC.Permission")
        return self.result_is_ok(r)

    def instrospect(self, params={}):
        r = self.post(method="JSONRPC.Introspect")
        return self.result_is_ok(r)

    def has_permission(self, permission):
        r = self.get_permission()
        if r and (permission in r):
            return r[permission]
        else:
            return False

    def notify_all(self, params={}):
        """
        .. todo: To figure out to where the hell these messages go.
        """
        r = self.post(method="JSONRPC.NotifyAll", params=params)
        return self.result_is_ok(r)

    def ping(self):
        r = self.post("JSONRPC.Ping")
        if r and (r["result"] == u"pong"):
            return True
        else:
            return False

    def set_configuration(self, params={}):
        r = self.post(method="JSONRPC.SetConfiguration")
        return self.result_is_ok(r)

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
                return r["result"]
        else:
            return False

    def set_configuration(self):
        r = self.post(method="JSONRPC.SetConfiguration")
        print(r)

    def version(self):
        """
        .. todo:: Implement exception handling.
        """
        r = self.post("JSONRPC.Version")
        if r and ("result" in r):
            return r["result"]["version"]
        else:
            return False

class RequestHandler(object):
    """
    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01

    .. class:: ctrlpi.RequestHandler

    This class id responsible for send the HTTP requests, including headers,
    authentication, proxy and make a small processing with the response.

    .. todo:: Implement proxy support.
    """

    def __init__(self, object):
        global data
        data = object

    def get(self, url, auth=None):
        """
        Make HTTP GET requests. Has support to HTTP simple authentication, using
        the *auth* tuple.
        """
        r = requests.get(url=url, auth=auth)
        return r.text

    def post(self, payload):
        """
        Most important method of this class. Send POST requests to a given url,
        with custom headers and payload.

        .. todo:: Implement a better exception handling.
        """
        try:
            r = requests.post(url=data["url"], data=json.dumps(payload),
                    headers=data["headers"])
        except requests.exceptions.ConnectionError:
            return False
        return r.json()

class System(JSONRPC):
    """
    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01

    .. class:: ctrlpi.System

    Controls the basic state of XMBC system.

    Inherits from *JSONRPC* class.

    .. todo:: Implement failing procedure.
    """

    def __init__(self, object):
        super(System, self).__init__(object)

    def cpu_usage(self, params={}):
        """
        .. todo: to be implemented. RPC not recognized by the server.
        """
        #r = self.post(method="System.CPUUsage", params=params)
        #return self.result_is_ok(r)
        return False

    def get_properties(self, params={}):
        r = self.post(method="System.GetProperties", params=params)
        return self.result_is_ok(r)

    def get_tasks(self):
        return False

    def get_uptime(self):
        return False

    def hibernate(self):
        """
        Hibernate the client.
        Doesn't work in the Raspberry Pi.
        """
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["canhibernate"]})
            if r["canhibernate"]:
                r = self.post(method="System.Hibernate")
                return self.result_is_ok(r)
        return False

    def reboot(self):
        """
        Restart the client.
        """
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["canreboot"]})
            if r["canreboot"]:
                r = self.post(method="System.Reboot")
            return self.result_is_ok(r)
        return False

    def shutdown(self):
        """
        Turn off the client.
        """
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["canshutdown"]})
            if r["canshutdown"]:
                r = self.post(method="System.Shutdown")
                return self.result_is_ok(r)
        return False

    def suspend(self):
        """
        Suspend the client.
        Doesn't work in the Raspberry Pi.
        """
        if self.has_permission(permission="ControlPower"):
            r = self.get_properties(params={"properties": ["cansuspend"]})
            if r["cansuspend"]:
                r = self.post(method="System.Suspend")
                return self.result_is_ok(r)
        return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

