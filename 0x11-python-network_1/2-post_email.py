#!/usr/bin/python3
"""Is a Python script that takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """
import urllib.request
from urllib.parse import urlparse
from sys import argv

if __name__ == "__main__":
    email = urlparse({"email", argv[2]}).encode()
    req = urllib.request(argv[1])

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf8"))
