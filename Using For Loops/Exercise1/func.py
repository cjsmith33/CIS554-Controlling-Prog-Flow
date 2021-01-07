"""
Module with simple for-loop functions.

Author: Charles Smith
Date: 04 January 2021
"""


def lesser(tup,value):
    """
    Returns the number of elements in tup strictly less than value

    Examples:
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0

    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints

    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    result = 0

    for x in tup:
        if x < value:
            result = result + 1
    return result


def avg(tup):
    """
    Returns average of all of the elements in the tuple.

    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.

    Examples:
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5

    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    result = 0
    if len(tup) == 0:
        return float(result)
    else:
        for x in tup:
            result = result + x
        return result/len(tup)
