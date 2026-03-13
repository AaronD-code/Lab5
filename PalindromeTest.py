import unittest
from main import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()