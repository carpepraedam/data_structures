import unittest
import random

from bubble import bubble


class BubbleSortTests(unittest.TestCase):

    def test_bubble(self):
        """
        Tests the bubble(list) method
        """
        data = [3, 1, 10, 9]
        results = bubble(data)
        self.assertIsInstance(results, tuple)
        self.assertEqual(results[0], [1, 3, 9, 10])
        data = random.sample(range(0, 100), 10)
        results = bubble(data)
        self.assertEqual(results[0], sorted(data))

        # test is_sorted functionality
        # sweeps should be 1 on a fully sorted list
        data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        results = bubble(data)
        self.assertEqual(results[0], [1, 2, 3, 4, 5, 6, 7, 8, 10])
        self.assertEqual(results[1], 1)  # 1 sweep

        # another more sweep, test, should be 9 sweeps
        data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 0]
        results = bubble(data)
        self.assertEqual(results[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10])
        self.assertEqual(results[1], 9)  # 9 sweeps

        # last sweep, test, should be 2 sweeps
        data = [1, 0, 2, 3, 4, 5, 6, 7, 8, 10]
        results = bubble(data)
        self.assertEqual(results[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10])
        self.assertEqual(results[1], 2)  # 2 sweeps

    def test_comparator(self):
        """
        Tests the comparator kwarg, which allows a user to define a 
        custom comparator function
        """
        def ascending_string_length_comparator(str_a, str_b):
            """
            @param {string} str_a
            @param {string} str_b
            @param {bool} ascending
            @return {bool} return len(str_a) > len(str_b)
            """
            # strings with less characters get moved left
            return len(str_a) > len(str_b)

        data = ['a', 'big', 'brown', 'giraffe']
        results = bubble(data, ascending_string_length_comparator)
        self.assertEqual(results[0], ['a', 'big', 'brown', 'giraffe'])
        self.assertEqual(results[1], 1)  # sweeps

        data = ['a', 'big', 'brown', 'giraffe'][::-1]  # reverse list
        results = bubble(data, ascending_string_length_comparator)
        # same results
        self.assertEqual(results[0], ['a', 'big', 'brown', 'giraffe'])
        self.assertEqual(results[1], 3)  # but more sweeps


if __name__ == "__main__":
    unittest.main()
