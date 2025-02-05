"""
Test suite for calculator functions.
"""

from calculator import add, subtract

def test_addition():
    """
    Test the add function.
    """
    result = add(2, 3)
    assert result == 5

def test_subtraction():
    """
    Test the subtract function.
    """
    result = subtract(5, 3)
    assert result == 2
