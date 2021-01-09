"""
A collection of functions to support the translation of words into Pig Latin.

This module contains two functions.  The first function searchs for the location of the
first vowel.  The second function uses this as a helper to perform the conversion.

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


def pigify(s):
    """
    Returns a copy of s converted to Pig Latin

    Pig Latin is childish encoding of English that adheres to the following rules:

    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.

        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y')
        and three consonants (the first 'y', 'r', and 'l').

    2.  If the English word begins with a vowel, append 'hay' to the end of the word
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes
        'usehay'.

    3.  If the English word starts with 'q', then it must be followed by'u'; move
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.

    4.  If the English word begins with a consonant, move all the consonants up to
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato'
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and
        'ssssh' becomes 'sssshay'.

    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """
    result = first_vowel(s)
    #No Vowel
    if(result == -1):
        return s + 'ay'
    #Begin with Consonant
    elif(result > 0 and s[0] != str('q')):
        return s[result:len(s)] + s[:result] + 'ay'
    #Begin with Vowel
    elif(result == 0):
        return s + 'hay'
    #Begin with QU
    else:
        #result = funcs.pigify('quiet')
        #introcs.assert_equals('ietquay',result)
        return s[2:len(s)] + 'quay'


    
