#!/usr/bin/python3
"""Is a Python script that fetches https://intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":

    with request.urlopen("https://intranet.hbtn.io/status") as response:
        value = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(value)))
    print("\t- content: {}".format(value))
