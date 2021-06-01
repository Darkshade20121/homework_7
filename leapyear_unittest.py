import unittest
import leapyear

class leapyear_test(unittest.TestCase):
    def test_leapyear_pass(self):
        result = leapyear.leap_year(2000)
        self.assertEqual(result,1)

    def test_leapyear_2_pass(self):
        result = leapyear.leap_year(2004)
        self.assertEqual(result,1)

    def test_leapyear_3_pass(self):
        result = leapyear.leap_year(2008)
        self.assertEqual(result,1)
    
    def test_leapyear_fail(self):
        result = leapyear.leap_year(2001)
        self.assertEqual(result,1)

    def test_leapyear_2_fail(self):
        result = leapyear.leap_year(2003)
        self.assertEqual(result,1)

    def test_leapyear_3_fail(self):
        result = leapyear.leap_year(2000)
        self.assertEqual(result,0)
