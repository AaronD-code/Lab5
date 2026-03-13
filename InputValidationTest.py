import unittest
from main import validate_and_parse_user

class TestInputValidation(unittest.TestCase):
    def test_valid_input(self):
        data = {"name": " Aaron ", "age": "21"}
        parsed = validate_and_parse_user(data)
        self.assertEqual(parsed, {"name": "Aaron", "age": 21})

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            validate_and_parse_user({"name": "", "age": 10})

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            validate_and_parse_user({"name": "Aaron", "age": "abc"})

if __name__ == "__main__":
    unittest.main()