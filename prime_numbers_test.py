''' 5 unit tests for the prime numbers function '''

import unittest
from prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    '''this class tests generated prime numbers'''

    def test_prime_numbers(self):
        """testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_zero(self):
        """testing if zero is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(
            0), "zero or one are not prime numbers.")

    def test_one(self):
        """"testing if one is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(
            1), "zero or one are not prime numbers.")

    def test_invalid_type_string_list(self):
        """Testing if error returned for non-integer input."""

        self.assertEqual(prime_numbers([]), "Only integers are allowed.")

    def test_only_positive(self):
        """Testing if error returned for negative integers input."""

        self.assertEqual(
            prime_numbers(-1), "integers less than 2 cannot be prime numbers")


if __name__ == "__main__":
    unittest.main()
