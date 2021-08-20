#!/usr/bin/python3
"""Is a Python script that takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """
from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    values = {"email": argv[2]}
    email = parse.urlencode(values).encode()
    req = request.Request(argv[1], email)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
