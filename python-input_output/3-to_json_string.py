#!/usr/bin/python3
""" defines a function that returns Json representation of an object """

import json


def to_json_string(my_obj):
    """
    return JSON representation
    """
    return json.dumps(my_obj)
