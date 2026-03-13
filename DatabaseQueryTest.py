import unittest
import sqlite3

class TestDatabaseQuery(unittest.TestCase):
    def test_query_expected_results(self):
        conn = sqlite3.connect(":memory:")
        cur = conn.cursor()

        cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("INSERT INTO users (name) VALUES (?)", ("Aaron",))
        cur.execute("INSERT INTO users (name) VALUES (?)", ("Senja",))
        conn.commit()

        cur.execute("SELECT name FROM users ORDER BY id")
        rows = cur.fetchall()

        self.assertEqual(rows, [("Aaron",), ("Senja",)])

        conn.close()

if __name__ == "__main__":
    unittest.main()