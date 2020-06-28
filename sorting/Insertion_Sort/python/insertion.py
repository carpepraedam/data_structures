def insertion_sort(l):
    """
    @param {list} l - the list to sort
    @return {tuple(list, number)} - Tuple(sorted list, number of iterations)
    """
    sweeps = 0
    for i in range(1, len(l)):
        sweeps += 1
        current_val = l[i]
        j = i - 1
        while (j >= 0) and (l[j] > current_val):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = current_val
    return (l, 0)


def swap(l, index_a, index_b):
    """
    Swaps two index in a list
    @param {list} l - the list
    @param {number} index_a - The first index
    @param {number} index_b - The second index
    """
    tmp = l[index_a]
    l[index_a] = l[index_b]
    l[index_b] = tmp
