import unittest
from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """1 нь анхны тоо биш."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """2 нь анхны тоо мөн."""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """8 нь анхны тоо биш."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """11 нь анхны тоо мөн."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """25 нь анхны тоо биш."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """28 нь анхны тоо биш."""
        self.assertFalse(is_prime(28))


# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()