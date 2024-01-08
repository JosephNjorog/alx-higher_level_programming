#!/usr/bin/python3
"""
This is '101-add_attribute' module.
Functions and Classes:
    add_attribute(obj, attribute, value)
"""


def add_attribute(obj, attribute, value):
    """
    new attribute to an object if it’s possible
    """
    if hasattr(obj, "__dict__"):
        print("to be added... {}".format(attribute))
        setattr(obj, attribute, value)
        print("done")
    else:
        raise TypeError("can't add new attribute")
