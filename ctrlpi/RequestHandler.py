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

