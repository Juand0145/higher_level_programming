#!/usr/bin/python3
'''A function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''Open and print whats in filename'''
    with open(filename, encoding="utf-8") as my_file:
        text = my_file.read()
        print(text, end='')
