__all__ = ["System", "VideoLibrary"]

import ConfigParser
import json
import os
import requests
import sys

import System
import VideoLibrary

headers = {"content-type": "application/json"}
payload = {"jsonrpc": "2.0", "id": 1}
data = {}

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

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

