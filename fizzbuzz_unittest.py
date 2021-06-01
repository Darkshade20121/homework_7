import unittest
import fizzbuzz

class fizzbuzz_test(unittest.TestCase):
    def test_fizz_pass(self):
        result = fizzbuzz.fizzbuzz_loop(15)
        self.assertEqual(result, 1)

    
