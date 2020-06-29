import math
from functools import reduce
import operator


def radix_sort(l):
    """
    Radix sort a list of POSITIVE BASE 10 numbers
    @param l {list} : list of POSITIVE BASE 10 numbers to sort
    @return {list} sorted list
    """
    # get the digits in the largest number in list
    # [3, 1, 10, 9]
    max_dig = get_max_digits_in_list(l)
    for k in range(0, max_dig):
        buckets = [[] for _ in range(10)]
        for i in range(0, len(l)):
            num = l[i]
            buckets[get_n_digit(num, k)].append(num)
        l = reduce(operator.add, buckets)
    return l


def get_n_digit(num, n):
    """
    Returns the nth index (from the right) of a base 10 number
    Example: 
        get_n_digit(897, 0) returns 7
        get_n_digit(897, 1) returns 9
        get_n_digit(897, 2) returns 8
        get_n_digit(897, 5) returns 0 (out of boudns)
    @param num {number}
    @param n {n}
    @return {number} : digit at nth position, 0 if out of bounds
    """
    if n < 0:
        return 0
    x = abs(num) // 10**n % 10
    return x


def get_digit_count(num):
    """
    Returns the number of digits in a number
    @param num {number}
    @return {number} : number of digits
    """
    if num == 0:
        return 1
    return math.floor(math.log(abs(num), 10)) + 1


def get_max_digits_in_list(l):
    """
    Returns the maximum number of digits found in all the numbers in
    the list
    @param l {list}
    @return {number}
    """
    if l == []:
        return 0
    return get_digit_count(max(l))
