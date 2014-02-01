class VideoLibrary(object):
    def __init__(self, object):
        self.url = object["url"]
        self.headers = object["headers"]
        self.payload = object["payload"]

    def clean(self):
        self.payload["method"] = "VideoLibrary.Clean"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

    def scan(self):
        self.payload["method"] = "VideoLibrary.Scan"
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        return r.json()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

