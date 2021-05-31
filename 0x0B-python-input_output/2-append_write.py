#!/usr/bin/python3
'''A function that appends a string at the end of a
text file (UTF8) and returns the number of characters added '''


def append_write(filename="", text=""):
    '''Create or append a file with text content '''
    with open(filename, mode="a", encoding="utf-8") as my_file:
        file = my_file.write(text)

        return file
