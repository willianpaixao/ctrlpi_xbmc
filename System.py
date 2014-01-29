"""
Created on 28 January 2014
"""

class System(object):
    """
    Controls the basic state of XMBC system.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        self.url = object["url"]
        self.headers = object["headers"]
        self.payload = object["payload"]

    def get_properties(self):
        self.payload["method"] = "System.GetProperties"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

    def hibernate(self):
        self.payload["method"] = "System.Hibernate"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

    def reboot(self):
        self.payload["method"] = "System.Reboot"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

    def shutdown(self):
        self.payload["method"] = "System.Shutdown"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

    def suspend(self):
        self.payload["method"] = "System.Suspend"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

