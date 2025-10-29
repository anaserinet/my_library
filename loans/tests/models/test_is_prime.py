from django.test import TestCase

from loans.helpers import is_prime


class IsPrimeTextCase(TestCase):
    def test_3_is_primer(self):
        actual_resut = is_prime(3)
        self.assertTrue(actual_resut)

    def test_4_is_not_prime(self):
        actual_resut = is_prime(4)
        self.assertFalse(actual_resut)

# Create your tests here.
