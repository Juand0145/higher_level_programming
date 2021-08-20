#!/usr/bin/python3
"""Is a Python script that takes in a URL, sends a request to the
URL and displays the body of the response."""

from sys import argv
import requests

if __name__ == "__main__":
    status_number = requests.get(argv[1]).status_code
    req = requests.get(argv[1])

    if status_number >= 400:
        print("Error code: {}".format(status_number))

    else:
        print(req.text)
