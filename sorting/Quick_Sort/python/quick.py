def quick_sort(l, left=0, right=None):
    """
    Recursively sorts list in place using quick_sort
    @param {list} l 
    @param {number} left - the left most index for quick_pivot call
    @param {number} right - the right most index for quick_pivot call
    @return {list}
    """
    if right is None:
        right = len(l)

     # base case, sub list length < 2
    sublist = l[left:right]
    if len(sublist) < 2:
        return l

    # quick_pivot the list and get the final pivot_index
    pivot_index = quick_pivot(l, left, right)
    # sort left of pivot_index
    quick_sort(l, left, pivot_index)
    # sort right of pivot_index
    quick_sort(l, pivot_index + 1, right)

    return l


def quick_pivot(l, left_index=0, right_index=None):
    """
    Pivot utility function for quick sort. Moves all element
    less than the pivot to the left. Then moves the pivot to right
    of all elements less than itself.
    Example: [10,5,3,15,20] with pivot index of 0 (value = 10)
            will alter the list to [3,5,10,15,20], then return
            the final pivot index (index 2, where the value = 10)
    @param {list} l
    @param {number} left_index - default 0
    @param {number} right_index 0 default 0
    @return {number} final pivot index
    """
    # pivot_index = 0  # pivot index will be first element
    store_index = left_index + 1
    if right_index is None:
        right_index = len(l)
    for i in range(left_index + 1, right_index):
        if l[i] < l[left_index]:
            swap(l, i, store_index)
            store_index += 1
    if(len(l) > 0):
        swap(l, left_index, store_index - 1)
    return store_index - 1


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
