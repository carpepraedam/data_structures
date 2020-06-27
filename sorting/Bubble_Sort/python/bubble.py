def comparator(val_a, val_b):
    """
    Default comparator, checks if val_a > val_b
    @param {number} val_a
    @param {number} val_b
    @return {bool} : True if val_a > val_b else False
    """
    return val_a > val_b


def bubble(l, comparator=comparator):
    """
    Bubble sort a given list
    @param {list} l - the list to sort
    @param {function(arg_a, arg_b)} - function reference
        If return value is True, indices with values arg_a and arg_b will be swapped
        Default:
        comparator(val_a, val_b):
            return val_a > val_b
    @return {tuple(list, number)} - (sorted list, number of iterations) 
    """
    # outer bubble
    sweeps = 0
    for i in range(len(l) - 1, 0, -1):
        sweeps += 1
        is_sorted = True
        for j in range(i):
            if(comparator(l[j], l[j+1])):
                is_sorted = False
                swap(l, j, j+1)
        if is_sorted:
            break
    return (l, sweeps)


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
