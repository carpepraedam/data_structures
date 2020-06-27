def selection_sort(l):
    """
    @param {list} l - the list to sort
    @return {tuple(list, number)} - Tuple(sorted list, number of iterations)
    """
    sweeps = 0
    for i in range(len(l)):
        sweeps += 1
        min_val_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_val_index]:
                min_val_index = j
        if i != min_val_index:
            swap(l, i, min_val_index)
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
