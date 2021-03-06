import unittest
import random

from selection import selection_sort


class SelectionSortTests(unittest.TestCase):

    def test_selection_sort(self):
        """
        Tests the selection_sort(list) method
        """
        data = [3, 1, 10, 9]
        results = selection_sort(data)
        self.assertIsInstance(results, tuple)
        self.assertEqual(results[0], [1, 3, 9, 10])
        data = random.sample(range(0, 100), 10)
        results = selection_sort(data)
        self.assertEqual(results[0], sorted(data))


if __name__ == "__main__":
    unittest.main()
