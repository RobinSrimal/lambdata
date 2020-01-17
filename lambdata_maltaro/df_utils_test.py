import unittest
from df_utils import UtilityFunctions

class SqrtTests(unittest.TestCase):
    """Functions to test the increment of attributes


    """
    ut = UtilityFunctions()

    def test_raise_power(self):
        #ut = UtilityFunctions()
        self.assertEqual(ut.raise_power(5,2),25)

    def test_raise_power_coolness(self):
        #ut = UtilityFunctions()
        self.assertEqual(ut.raise_power_coolness(2),25)

    def test_coolness_attribute(self):
        #ut = UtilityFunctions()
        self.assertEqual(ut.coolness,5)


if __name__ == "__main__":
    unittest.main()
