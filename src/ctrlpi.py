import ConfigParser
import os
import sys

import JSONRPC
import System
import VideoLibrary

data = {}
headers = {"content-type": "application/json"}
payload = {"jsonrpc": "2.0", "id": 1}

def read_config():
    config_file = os.environ["HOME"] + "/.ctrlpi/" + "settings.ini"
    if os.path.isfile(config_file) == True:
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        url = config.get("default", "url")
        data["url"] = url
        data["headers"] = headers
        data["payload"] = payload
    else: raise

if __name__ == "__main__":
    read_config()
    c = System.System(data)
    print(c.ping())
    print(c.version())
    print(c.get_permission())
    print(c.get_properties())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

