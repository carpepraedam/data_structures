import unittest
import random

from radix import (
    get_n_digit,
    get_digit_count,
    get_max_digits_in_list,
    radix_sort
)


class RadixSortTests(unittest.TestCase):

    def test_get_n_digit(self):
        """
        Tests the get_n_digit(number, n) method
        """
        self.assertEqual(get_n_digit(758, 0), 8)
        self.assertEqual(get_n_digit(758, 1), 5)
        self.assertEqual(get_n_digit(758, 2), 7)
        # test with negative num
        self.assertEqual(get_n_digit(-758, 0), 8)
        self.assertEqual(get_n_digit(-758, 1), 5)
        self.assertEqual(get_n_digit(-758, 2), 7)
        # test with negative n
        self.assertEqual(get_n_digit(758, -1), 0)
        self.assertEqual(get_n_digit(758, -2), 0)
        self.assertEqual(get_n_digit(758, -2), 0)
        self.assertEqual(get_n_digit(758, -99), 0)
        # test index out of bounds returns zero
        self.assertEqual(get_n_digit(758, 3), 0)
        self.assertEqual(get_n_digit(758, 9), 0)
        # test with num 0
        self.assertEqual(get_n_digit(0, 0), 0)

    def test_get_digit_count(self):
        """
        Tests the get_digit_count(number) method
        """
        self.assertEqual(get_digit_count(0), 1)
        self.assertEqual(get_digit_count(1), 1)
        self.assertEqual(get_digit_count(11), 2)
        self.assertEqual(get_digit_count(111), 3)
        self.assertEqual(get_digit_count(1111), 4)
        self.assertEqual(get_digit_count(11111), 5)
        # test with negative numbers
        self.assertEqual(get_digit_count(-0), 1)
        self.assertEqual(get_digit_count(-1), 1)
        self.assertEqual(get_digit_count(-11), 2)
        self.assertEqual(get_digit_count(-111), 3)
        self.assertEqual(get_digit_count(-1111), 4)
        self.assertEqual(get_digit_count(-11111), 5)

    def test_get_max_digits_in_list(self):
        """
        Tests the get_max_digits_in_list(list) method
        """
        l = [0, 123, 5, 12, 7]
        self.assertEqual(get_max_digits_in_list(l), 3)
        l = [1230, 12342, 15, 1322, 7455]
        self.assertEqual(get_max_digits_in_list(l), 5)
        l = [0, 0, 0, 0]
        self.assertEqual(get_max_digits_in_list(l), 1)
        # test empty list
        l = []
        self.assertEqual(get_max_digits_in_list(l), 0)

    def test_radix_sort(self):
        """
        Tests the radix_sort(list) method
        """
        data = [3, 1, 10, 9]
        results = radix_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [1, 3, 9, 10])
        data = random.sample(range(0, 100), 10)
        results = radix_sort(data)
        self.assertEqual(results, sorted(data))

        # test empty list
        data = []
        results = radix_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [])

        # test single index list
        data = [1]
        results = radix_sort(data)
        self.assertIsInstance(results, list)
        self.assertEqual(results, [1])


if __name__ == "__main__":
    unittest.main()
