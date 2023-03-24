#!/usr/bin/python3
""" function"""


def is_same_class(obj, a_class):
    """ check if the object is an instance of a_class"""

    return type(obj) == a_class


if __name__ == '__main__':
    a = 5
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
