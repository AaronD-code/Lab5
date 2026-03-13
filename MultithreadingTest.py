import unittest
import threading
from main import ThreadCounter

class TestMultithreading(unittest.TestCase):
    def test_thread_safety(self):
        counter = ThreadCounter()

        t1 = threading.Thread(target=counter.increment_many, args=(10000,))
        t2 = threading.Thread(target=counter.increment_many, args=(10000,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        self.assertEqual(counter.value, 20000)

if __name__ == "__main__":
    unittest.main()