#!/usr/bin/python3
""" counting number of characters in a file"""


def write_file(filename="", text=""):
    """ function creates a new file or
    overwrites current one and counts number of characters """
    with open(filename, mode='w', encoding='utf-8') as a_text:

        return a_text.write(str(text))
