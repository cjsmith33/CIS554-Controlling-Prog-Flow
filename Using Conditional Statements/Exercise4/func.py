"""
A function to search for the first vowel position

Author: Charles Smith
Date: 01 January 2021
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)     #  In case there is no 'a'

    if(introcs.find_str(s, 'a') >= 0):
        result = introcs.find_str(s, 'a')
    if(introcs.find_str(s, 'e') >= 0):
        if(introcs.find_str(s, 'e') < result):
            result = introcs.find_str(s, 'e')
    if(introcs.find_str(s, 'i') >= 0):
        if(introcs.find_str(s, 'i') < result):
            result = introcs.find_str(s, 'i')
    if(introcs.find_str(s, 'o') >= 0):
        if(introcs.find_str(s, 'o') < result):
            result = introcs.find_str(s, 'o')
    if(introcs.find_str(s, 'u') >= 0):
        if(introcs.find_str(s, 'u') < result):
            result = introcs.find_str(s, 'u')
    if(introcs.find_str(s, 'y', 1, len(s)) >= 1):
        if(introcs.find_str(s, 'y', 1, len(s)) < result):
            result = introcs.find_str(s, 'y', 1, len(s))

    return result if result < len(s) else -1
