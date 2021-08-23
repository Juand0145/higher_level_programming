#!/bin/bash
#Is a Bash script that takes
curl -sI "$1" | grep Allow: | cut -d ' ' -f 2-
