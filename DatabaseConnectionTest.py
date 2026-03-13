import unittest
import sqlite3

class TestDatabaseConnection(unittest.TestCase):
    def test_connection_successful(self):
        conn = sqlite3.connect(":memory:")
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == "__main__":
    unittest.main()