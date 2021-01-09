"""
A test script for the function iso_8601.

Author: Charles Smith
Date: 04 January 2021
"""
import func
import introcs
"""
Returns True if s is a string in ISO 8601 format, False otherwise

ISO 8601 format the form 'hh:mm:ss' where h, m, and s are digits.  There must be
exactly two digits each for minutes and seconds, so they are padded with 0s when
necessary. The hours may either be 1 or 2 digits. For
more information, see
"""

def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')

    # Valid Values
    result = func.iso_8601('02:10:22')
    introcs.assert_equals(True, result)

    result = func.iso_8601('00:01:01')
    introcs.assert_equals(True, result)

    result = func.iso_8601('00:00:01')
    introcs.assert_equals(True, result)

    result = func.iso_8601('1:01:01')
    introcs.assert_equals(True, result)

    # Missing hour
    result = func.iso_8601(':01:01')
    introcs.assert_equals(False, result)

    # Missing minute
    result = func.iso_8601('1::01')
    introcs.assert_equals(False, result)

    # Missing second
    result = func.iso_8601('1:01:')
    introcs.assert_equals(False, result)

    # Non-numeric values
    result = func.iso_8601('a:01:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('02:a:01')
    introcs.assert_equals(False, result)

    # Out of bounds values
    result = func.iso_8601('25:01:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('23:67:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('23:59:67')
    introcs.assert_equals(False, result)

    # Misc errors
    result = func.iso_8601('101::01:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('010101')
    introcs.assert_equals(False, result)

if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')
