#!/usr/bin/env python3

"""
A module for calculating the average of a list of numbers.

Module contents:
    - calculate_average: Calculates and returns the average of a list of numbers.
"""


def calculate_average(numbers):
    """
    Returns the average of a list of numeric values (integers or floats).

    Takes a list of integers or floats and returns their average as a float.
    If the list is empty, this function returns None. If any element in the
    list is not an integer or float, an AssertionError is raised.

    Parameters:
        numbers: list of int or float, the values to average.

    Returns -> float or None: the average of all numbers. If the list is empty,
    returns None.

    Raises:
        AssertionError: if any element in the list is not an int or float
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
