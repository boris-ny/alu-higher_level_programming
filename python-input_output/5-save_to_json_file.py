#!/usr/bin/python3
""" use json module to use functions """
import json
""" module converts object to json and writes to file """


def save_to_json_file(my_obj, filename):
    """ converts to json and writes to file """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
