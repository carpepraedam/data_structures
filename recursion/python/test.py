import unittest

from exercises import (
    factorial,
    fib,
    power,
    product_of_list,
    reverse,
    sum_range
)


class TestRecursionExercises(unittest.TestCase):

    def test_power(self):
        """
        Tests the power(base, exponent) method
        """
        self.assertEqual(4, power(2, 2))
        self.assertEqual(2, power(2, 1))
        self.assertEqual(16, power(2, 4))
        self.assertEqual(27, power(3, 3))
        # edge cases
        self.assertEqual(1, power(6, 0))
        self.assertEqual(1, power(12, 0))
        self.assertEqual(0, power(0, 5))
        self.assertEqual(1, power(0, 0))

    def test_factorial(self):
        """
        Tests the factorial(num) method
        """
        self.assertEqual(120, factorial(5))
        self.assertEqual(3628800, factorial(10))
        self.assertEqual(1, factorial(0))

    def test_product_of_list(self):
        """
        Tests the product_of_list(l) method
        """
        self.assertEqual(100, product_of_list([2, 5, 10]))
        self.assertEqual(120, product_of_list([1, 2, 3, 4, 5]))
        self.assertEqual(0, product_of_list([]))
        self.assertEqual(1, product_of_list([1]))

    def test_sum_range(self):
        """
        Tests the sum_range(num) method
        """
        self.assertEqual(6, sum_range(3))
        self.assertEqual(55, sum_range(10))
        self.assertEqual(5050, sum_range(100))

    def test_fib(self):
        """
        Tests the fib(num) method
        """
        self.assertEqual(3, fib(4))
        self.assertEqual(55, fib(10))

    def test_reverse(self):
        """
        Tests the reverse(seq) method
        """
        self.assertEqual('hello'[::-1], reverse('hello'))
        self.assertEqual('', reverse(''))
        self.assertEqual(' ', reverse(' '))


if __name__ == "__main__":
    unittest.main()
