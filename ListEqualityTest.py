import unittest

class TestListEquality(unittest.TestCase):
    def test_equal_lists(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(a, b)

    def test_not_equal_lists(self):
        a = [1, 2, 3]
        b = [1, 2, 4]
        self.assertNotEqual(a, b)

if __name__ == "__main__":
    unittest.main()