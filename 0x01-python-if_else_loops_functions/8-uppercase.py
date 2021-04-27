#!/usr/bin/python3
def uppercase(str):
    for word in(str):
        c = ord(word)
        if c >= ord('a') and c <= ord('z'):
            char = chr(c - 32)

        else:
            char = word

        print("{:s}".format(char), end="")
    print()
