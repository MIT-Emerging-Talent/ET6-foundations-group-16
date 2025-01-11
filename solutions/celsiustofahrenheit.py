#!/usr/bin/env python3

"""
A module for converting temperatures between Celsius and Fahrenheit.

Module contents:
    - celsius_to_fahrenheit: Converts a temperature from Celsius to Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit.

    Parameters:
        celsius: float, the temperature in Celsius.

    Returns -> float: the temperature converted to Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(25)
        77.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    return (celsius * 9/5) + 32
