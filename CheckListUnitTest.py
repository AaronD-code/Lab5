# Write a Python unit test program to check if a list is sorted in ascending order.

# Import the 'unittest' module for writing unit tests.
import unittest

# Define a function 'is_sorted_ascending' to check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    # Check if all elements at index i are less than or equal to elements at index i+1.
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Define a test case class 'TestSortedAscending' that inherits from 'unittest.TestCase'.
class TestSortedAscending(unittest.TestCase):
    # Define a test method 'test_sorted_list' to test a sorted list.
    def test_sorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [5, 7, 2, 8, 1, 9]
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Sorted list: ", lst)
        # Assert that the list is sorted in ascending order.
        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")

    # Define a test method 'test_unsorted_list' to test an unsorted list.
    def test_unsorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [1, 2, 3]
        lst = [5, 7, 2, 8, 1, 9]
        print("Unsorted list: ", lst)
        # Assert that the list is not sorted in ascending order.
        self.assertFalse(is_sorted_ascending(lst), "The list is sorted in ascending order")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()
