#!/usr/bin/python3
"""Is a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""

if __name__ == "__main__":
    import requests
    from sys import argv

    if argv[1]:
        values = {"q": argv[1]}

    else:
        values = {"q": ""}

    req = requests.post("http://0.0.0.0:5000/search_user", data=values)

    if req.headers.get("content-type") != "application/json":
        print("Not a valid JSON")
    elif req.json() == {}:
        print("No result")
    else:
        print("[{}] {}".format(req.json()["id"], req.json()["name"]))
