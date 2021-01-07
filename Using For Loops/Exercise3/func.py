"""
Module with range-based for-loop functions.

Author: Charles Smith
Date: 05 January 2021
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    factorial = 0
    if n == 0:
        factorial = 1
    else:
        for x in range(n):
            if x == 0:
                factorial = n
            else:
                factorial = factorial * x
    return factorial


def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter a: the "start" of the range
    Precondition: a is an int <= b

    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    tup = ()
    n = len(tuple(range(a,b)))
    count = 1
    for x in range(n):
        tup = tup + (b-count,)
        count+=1
    return tup
