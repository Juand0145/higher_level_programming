#!/usr/bin/python3
"""Is a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get("https://api.github.com/user",
                       auth=(argv[1], argv[2])).json()

    if "id" not in req:
        print("None")
    else:
        print(req["id"])
