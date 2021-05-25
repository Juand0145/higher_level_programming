#!/usr/bin/python3
'''A function that prints a text with 2 new lines
after each of these characters: ., ? and : '''


def text_indentation(text):
    '''text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    There should be no space at the beginning or at the end
    of each printed line'''

    if type(text) != str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']

    for i in characters:
        text = (i + "\n\n").join(line.strip(" ") for line in text.split(i))

    print("{}".format(text), end="")
