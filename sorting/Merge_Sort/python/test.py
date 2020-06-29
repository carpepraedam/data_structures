import unittest
import random

from merge import merge_list, merge_sort


class MergeSortTests(unittest.TestCase):

    def test_merge_list(self):
        """
        Tests the merge_list(list) array
        """
        # [1,3,5] & [2,4,6] => [1,2,3,4,5,6]
        l1 = [1, 3, 5]
        l2 = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_list(l1, l2), expected)

        # [1, 32, 49] & [2, 41, 83, 123] => [1, 2, 32, 41, 49, 83, 123]
        l1 = [1, 32, 49]
        l2 = [2, 41, 83, 123]
        expected = [1, 2, 32, 41, 49, 83, 123]
        self.assertEqual(merge_list(l1, l2), expected)

        # Tests when numbers equal each other
        # [1, 2, 3] & [1, 2, 3] => [1, 1, 2, 2, 3, 3]
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        expected = [1, 1, 2, 2, 3, 3]
        self.assertEqual(merge_list(l1, l2), expected)

        # Test empty lists
        l1 = []
        l2 = []
        expected = []
        self.assertEqual(merge_list(l1, l2), expected)

        # Test l1 empty
        l1 = [1, 2, 3]
        l2 = []
        expected = [1, 2, 3]
        self.assertEqual(merge_list(l1, l2), expected)

        # Test l2 empty
        l1 = []
        l2 = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(merge_list(l1, l2), expected)

    def test_merge_sort(self):
        """
        Tests the merge_sort(list) method
        """
        data = [3, 1, 10, 9]
        results = merge_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [1, 3, 9, 10])
        data = random.sample(range(0, 100), 10)
        results = merge_sort(data)
        self.assertEqual(results, sorted(data))

        # test empty list
        data = []
        results = merge_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
