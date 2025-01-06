"""
test_euler_totient.py

This module contains unit tests for the `euler_totient` function, which computes Euler's totient
function (ϕ(n)). The function calculates the number of integers between 1 and n that are coprime
with n.

Author: Fahed Daibes
Date: Mon Jan 6 2025
Group: ET6-foundations-group-16

Tests:
- Valid positive integer inputs for Euler's totient function.
- Edge cases like 1 and prime numbers.
- Invalid inputs such as negative numbers, zero, and non-integer values.
"""

import unittest
from solutions.euler_totient import euler_totient


class TestEulerTotient(unittest.TestCase):
    """
    This test class contains unit tests for the `euler_totient` function.

    It tests the function's ability to handle various valid inputs, including edge cases like 1,
    and invalid inputs such as non-integer values, negative numbers, and zero.
    """

    def test_valid_input(self):
        """Test case for valid positive integer input."""
        self.assertEqual(euler_totient(9), 6)
        self.assertEqual(euler_totient(12), 4)
        self.assertEqual(euler_totient(5), 4)
        self.assertEqual(euler_totient(1), 1)

    def test_invalid_input_negative(self):
        """Test case for negative input."""
        with self.assertRaises(ValueError):
            euler_totient(-5)

    def test_invalid_input_zero(self):
        """Test case for zero input."""
        with self.assertRaises(ValueError):
            euler_totient(0)

    def test_invalid_input_non_integer(self):
        """Test case for non-integer input."""
        with self.assertRaises(ValueError):
            euler_totient("string")
        with self.assertRaises(ValueError):
            euler_totient(3.5)

    def test_large_input(self):
        """Test case for a large positive integer."""
        self.assertEqual(euler_totient(1000), 400)

    def test_prime_number(self):
        """Test case for prime number input."""
        self.assertEqual(euler_totient(7), 6)
        self.assertEqual(euler_totient(13), 12)


if __name__ == "__main__":
    unittest.main()