# 0x11. Python - Network #1

In this directory, we will find a compilation of files that will help us to understand the concept of how to incorporate python with server and all the kind of request we use in commons URL and help us to answer the next questions ?
 -   How to fetch internet resources with the Python package  `urllib`
 -   How to decode  `urllib`  body response
 -   How to use the Python package  `requests`  #requestsiswaysimplerthanurllib
 -   How to make HTTP  `GET`  request
 -   How to make HTTP  `POST`/`PUT`/etc. request
 -   How to fetch JSON resources
 -   How to manipulate data from an external service
## Files
 - 0-hbtn_status.py is a Python script that fetches `https://intranet.hbtn.io/status`
 - 1-hbtn_header.py is a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
 - 2-post_email.py is a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
 - 3-error_code.py is a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
 - 4-hbtn_status.py is a Python script that fetches `https://intranet.hbtn.io/status`
 - 5-hbtn_header.py is a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
 - 6-post_email.py is a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
 - 7-error_code.py is a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
 - 8-json_api.py is a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
 - 10-my_github.py is a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://intranet.hbtn.io/rltoken/7CiInsXY2fMRZWSoHQs_TA "GitHub API") to display your `id`