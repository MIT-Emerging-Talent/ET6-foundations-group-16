#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting occurrences of a character in a string.

Created on 12/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)

Module functions:
    - count_character: counts occurrences of a character in a string.

"""


def count_character(input_string: str, character: str):
    """
    Counts the number of occurrences of a specific character in a string
    It will treat capital letters as different characters compared to small letters.

    Arguments:
      input_string (str): The string to count in.
      character (str): The character to count.

    Returns:
      int: The number of occurrences of the character in the string.

    Raises:
    AssertionError: if input string is not a string or character is not a single
      character string.

    >>> count_character("Mohamed", "m")
    1

    >>> count_character("test", "l")
    0

    >>> count_character("mississippi", "s")
    4

    """
    # Make sure inputs are correct
    if not isinstance(input_string, str):
        raise AssertionError("The input_string must be a string.")
    if not isinstance(character, str) or len(character) != 1:
        raise AssertionError("The character must be a single character string.")

    # Return the number of occurrences of character in the string
    return input_string.count(character)
