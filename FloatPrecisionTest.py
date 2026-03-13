import unittest
from main import safe_add_floats

class TestFloatPrecision(unittest.TestCase):
    def test_float_addition(self):
        # 0.1 + 0.1 + ... sometimes not exactly 1.0, so use almost equal
        result = safe_add_floats([0.1] * 10)
        self.assertAlmostEqual(result, 1.0, places=7)

if __name__ == "__main__":
    unittest.main()