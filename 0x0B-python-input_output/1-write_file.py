#!/usr/bin/python3
'''A function that writes a string to a text file 
(UTF8) and returns the number of characters written '''


def write_file(filename="", text=""):
    '''Read or create filename and put write text into it'''
    with open(filename, mode="w+", encoding="utf-8") as my_file:
        file = my_file.write(text)

    return(file)
