#!/usr/bin/env python3

"""
A module for calculating the average of a list of numbers.

Module contents:
    - calculate_average: Calculates and returns the average of a list of numbers.
"""


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers (integers or floats).
    Returns:
    - float: Average of the numbers.
    - None: If the list is empty.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
