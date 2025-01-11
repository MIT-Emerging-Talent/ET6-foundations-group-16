#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for celsius_to_fahrenheit function.

Test categories:
    - Standard cases: positive and negative numbers
    - Edge cases: freezing point, boiling point, absolute zero
"""

import unittest
from ..celsiustofahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Test suite for the celsius_to_fahrenheit function."""

    # Standard test cases
    def test_positive_temperature(self):
        """It should convert positive Celsius temperatures to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(25), 77.0)

    def test_negative_temperature(self):
        """It should convert negative Celsius temperatures to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    # Edge cases
    def test_freezing_point(self):
        """It should convert the freezing point of water correctly."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling_point(self):
        """It should convert the boiling point of water correctly."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_absolute_zero(self):
        """It should convert absolute zero correctly."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)


if __name__ == "__main__":
    unittest.main()
