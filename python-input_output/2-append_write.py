#!/usr/bin/python3
""" Defines the function """


def append_write(filename="", text=""):
    """ function appends text to given file """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
