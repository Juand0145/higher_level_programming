# 0x0C. Web server
In this directory, we will find a compilation of files that will help us to understand the concept of hhttp request and the structure of and URL and help us to answer the next questions:
-   What a URL is
-   What HTTP is
-   How to read a URL
-   The scheme for a HTTP URL
-   What a domain name is
-   What a sub-domain is
-   How to define a port number in a URL
-   What a query string is
-   What an HTTP request is
-   What an HTTP response is
-   What HTTP headers are
-   What the HTTP message body is
-   What an HTTP request method is
-   What an HTTP response status code is
-   What an HTTP Cookie is
-   How to make a request with cURL
-   What happens when you type google.com in your browser (Application level)

## Files

 - 0-body_size.sh is a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
 - 1-body.sh is Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
 - 2-delete.sh is a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response
 - 3-methods.sh is a Bash script that takes in a URL and displays all HTTP methods the server will accept.
 - 4-header.sh is a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
 - 5-post_params.sh is a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
 - 6-peak.py, 6-peak.txt is a function that finds **a peak** in a list of unsorted integers.