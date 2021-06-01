import unittest
import fizzbuzz

class fizzbuzz_test(unittest.TestCase):
    def test_fizz_pass(self):
        result = fizzbuzz.fizzbuzz_loop(15)
        self.assertEqual(result, 1)

    def test_fizz_2_pass(self):
        result = fizzbuzz.fizzbuzz_loop(3)
        self.assertEqual(result, 2)

    def test_fizz_3_pass(self):
        result = fizzbuzz.fizzbuzz_loop(5)
        self.assertEqual(result, 3)

    def test_fizz_fail(self):
        result = fizzbuzz.fizzbuzz_loop(100)
        self.assertEqual(result, 1)

    def test_fizz_2_fail(self):
        result = fizzbuzz.fizzbuzz_loop(150)
        self.assertEqual(result, 3)

