import unittest
import random

from quick import quick_pivot, quick_sort


class QuickSortTests(unittest.TestCase):

    def test_quick_pivot(self):
        """
        Tests the quick_pivot(list) array
        """
        data = [10, 5, 3, 15, 20]
        expected_after_pivot = [3, 5, 10, 15, 20]
        result = quick_pivot(data)
        self.assertEqual(data, expected_after_pivot)
        self.assertEqual(result, 2)

        # test single index list
        data = [1]
        expected_after_pivot = [1]
        result = quick_pivot(data)
        self.assertEqual(data, expected_after_pivot)
        self.assertEqual(result, 0)

        # test empty list
        data = []
        expected_after_pivot = []
        result = quick_pivot(data)
        self.assertEqual(data, expected_after_pivot)
        self.assertEqual(result, 0)

    def test_quick_sort(self):
        """
        Tests the quick_sort(list) method
        """
        data = [3, 1, 10, 9]
        results = quick_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [1, 3, 9, 10])
        data = random.sample(range(0, 100), 10)
        results = quick_sort(data)
        self.assertEqual(results, sorted(data))

        # test empty list
        data = []
        results = quick_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [])

        # test single index list
        data = [1]
        results = quick_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [1])

        # test two index list
        data = [1, -1]
        results = quick_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [-1, 1])

        # test three index list
        data = [1, -1, -5]
        results = quick_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [-5, -1, 1])


if __name__ == "__main__":
    unittest.main()
