import ConfigParser
import os
import sys

import System

__author__ = "Willian Paixao"
__category__ = "video"
__version__ = "0.01"
__description__ = ""

data = {}
data["headers"] = {"content-type": "application/json"}
data["payload"] = {"jsonrpc": "2.0", "id": 1}

def read_config():
    config_file = os.environ["HOME"] + "/.ctrlpi/" + "settings.ini"
    if os.path.isfile(config_file) == True:
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        data["url"] = config.get("default", "url")
    else: raise

if __name__ == "__main__":
    read_config()
    c = System.System(data)
    print(c.ping())
    print(c.version())
    print(c.get_permission())
    print(c.get_properties())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

