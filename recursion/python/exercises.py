def power(base, exponent):
    """
    Recursively raising base to exponent
    @param {number} base
    @param {number} exp
    @return {number}
    """
    # base case
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def factorial(num):
    """
    Recursively returns the factorial of a number
    @param {number}
    @return {number} factorial value
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)


def product_of_list(l):
    """
    Recursively returns the product of all numbers in a list
    @param {list} list of numbers
    @return {number} product of all numbers in list
    """
    # define an inner function
    def inner(l):
        if l == []:
            return 1
        return l.pop() * inner(l)

    # if empty list, return 0, do NOT call inner
    if l == []:
        return 0

    # call inner
    return inner(l)


def sum_range(num):
    """
    Recursively sums from 0 to num
    @param {number} num
    @return {number}
    """
    if num == 0:
        return 0
    return num + sum_range(num - 1)


def fib(num):
    """
    Recursively finds the nth number in the Fibonnacci sequence
    1, 1, 2, 3, 5, 8
    @param {number} num
    @return {number}
    """
    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)


def reverse(seq):
    """
    Recursively reverses a string
    @param {string} sequence to reverse
    @return {string}
    """
    if seq == '':
        return ''
    last_index = len(seq) - 1
    return seq[last_index] + reverse(seq[:last_index])
