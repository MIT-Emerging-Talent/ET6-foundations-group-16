#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for count_character function

Created on 11/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""

import unittest

from ..count_character import count_character


class TestCountCharacter(unittest.TestCase):
    """Test suite for the count_character function"""

    def test_string_with_no_occurrence(self):
        """it should return zero when the character is not in the string"""
        self.assertEqual(count_character("abcdefg", "h"), 0)

    def test_empty_string(self):
        """it should return zero when the input string is empty"""
        self.assertEqual(count_character("", "h"), 0)

    def test_string_with_normal_occurrence(self):
        """it should return the number of occurrences when the character in the string"""
        self.assertEqual(count_character("looking for a char", "o"), 3)

    def test_string_with_capital_and_small_letters(self):
        """it should treat capital letters as different characters compared to their small
        counterparts"""
        self.assertEqual(count_character("Mohammed Made soMething", "M"), 3)

    def test_counting_spaces(self):
        """it should count the number of spaces in a string when passed a space as
        a character"""
        self.assertEqual(
            count_character("there are a  l ot of spaces i n  this l ine", " "), 13
        )

    def test_input1_is_not_a_string(self):
        """It should raise AssertionError if first input is not a string"""
        with self.assertRaises(AssertionError):
            count_character(["mohamed"], "m")

    def test_character_is_not_a_string(self):
        """It should raise AssertionError if first input is not a single character string"""
        with self.assertRaises(AssertionError):
            count_character(["mohamed"], 2)

    def test_length_of_character_is_not_one(self):
        """It should raise AssertionError if length of character is not one"""
        with self.assertRaises(AssertionError):
            count_character(["mohamed"], "med")
