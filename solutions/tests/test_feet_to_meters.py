"""
Test module for the feet_to_meters function.

Test categories:
    - Standard cases: positive numbers, zero
    - Edge cases: negative numbers
    - Defensive tests: non-numeric input
"""

import unittest

from feet_to_meters import feet_to_meters


class TestFeetToMeters(unittest.TestCase):
    """Test suite for the feet_to_meters function."""

    # Standard test cases
    def test_positive_number(self):
        """It should return the correct meters for a positive number of feet."""
        self.assertEqual(feet_to_meters(10), 3.048)

    def test_zero(self):
        """It should return 0 for zero feet."""
        self.assertEqual(feet_to_meters(0), 0.0)

    # Edge cases
    def test_negative_number(self):
        """It should return the correct meters for a negative number of feet."""
        self.assertEqual(feet_to_meters(-5), -1.524)

    # Defensive tests
    def test_non_numeric_input(self):
        """It should raise an AssertionError if the input is not a number."""
        with self.assertRaises(AssertionError):
            feet_to_meters("10")  # Non-numeric input

    def test_non_numeric_float_input(self):
        """It should raise an AssertionError if the input is not a number (even if it's a string float)."""
        with self.assertRaises(AssertionError):
            feet_to_meters("3.14")  # Non-numeric float input


if __name__ == "__main__":
    unittest.main()
