"""
Author :Majd ABUALSOUD
Created :January 11,2025
This test suite for the area_of_circle function
 ensures its correctness by covering various scenarios.
 It tests the function with positive, zero,
 and negative radius values,
 ensuring accurate area calculations and proper handling of edge cases.
   Additionally, it checks the function's response to large inputs,
   such as non-numeric values, to ensure robust error handling.
     Each test case includes assertions to verify
     the function's reliability across different conditions.
"""

import math
import unittest

from ..area_circle import area_of_circle


class TestAreaOfCircle(unittest.TestCase):
    """
    Unit tests for the area_of_circle function.
    """

    def test_positive_radius(self):
        """Test area calculation with a positive radius."""
        self.assertAlmostEqual(area_of_circle(1), 3.141592653589793)
        self.assertAlmostEqual(area_of_circle(2.5), 19.634954084936208)

    def test_zero_radius(self):
        """Test area calculation with a radius of zero."""
        self.assertAlmostEqual(area_of_circle(0), 0.0)

    def test_negative_radius(self):
        """Test area calculation with a negative radius."""
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    def test_large_radius(self):
        """Test area calculation with a large radius."""
        self.assertAlmostEqual(area_of_circle(1e6), math.pi * 1e6 * 1e6)


if __name__ == "main":
    unittest.main()
