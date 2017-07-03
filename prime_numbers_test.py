''' 5 unit tests for the prime numbers function '''

import unittest
from prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    '''this class tests generated prime numbers'''

    def test_prime_numbers(self):
        """testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(10), [2, 3, 5, 7])

    def test_zero(self):
        """testing if 0 is correctly determined not to be a prime number."""

        self.assertEqual(prime_numbers(0), "0 or 1 are not prime numbers.")

    def test_one(self):
        """"testing if 1 is correctly determined not to be prime number."""

        self.assertEqual(prime_numbers(1), "0 or 1 are not prime numbers.")

    def test_invalid_type_string_list(self):
        """testing if error returned for non-integer input."""

        self.assertEqual(prime_numbers([]), "only integers are allowed.")

    def test_only_positive(self):
        """testing if error returned for negative integers input."""

        self.assertEqual(prime_numbers(-1), "integers less than 2 cannot be prime numbers")


if __name__ == "__main__":
    unittest.main()
