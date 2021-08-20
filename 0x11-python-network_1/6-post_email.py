#!/usr/bin/python3
"""Is a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":

    email = {"email": argv[2]}
    value = requests.post(argv[1], email).text

    print(value)
