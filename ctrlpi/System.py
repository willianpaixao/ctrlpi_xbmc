import JSONRPC

class System(JSONRPC.JSONRPC):
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

