import unittest
import os
import tempfile

class TestFileExists(unittest.TestCase):
    def test_file_exists(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "test.txt")
            with open(path, "w") as f:
                f.write("hi")
            self.assertTrue(os.path.exists(path))

    def test_file_not_exists(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "missing.txt")
            self.assertFalse(os.path.exists(path))

if __name__ == "__main__":
    unittest.main()