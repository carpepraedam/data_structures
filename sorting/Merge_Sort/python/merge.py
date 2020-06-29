def merge_sort(l):
    """
    Recursively sorts an array using merge sort
    @param {list} l
    @return {list}
    """
    # base case: list is has one index or is empty
    if len(l) <= 1:
        return (l)
    left = merge_sort(l[:len(l) // 2])
    right = merge_sort(l[len(l) // 2:])
    return merge_list(left, right)


def merge_list(i_list, j_list):
    """
    Merges two sorted lists into one sorted list
    [1,3,5] & [2,4,6] => [1,2,3,4,5,6]
    @param {list} i_list
    @param {list} j_list
    @return {list}
    """
    _return = []
    i = 0
    j = 0
    while (i < len(i_list)) and (j < len(j_list)):
        if(i_list[i] <= j_list[j]):
            _return.append(i_list[i])
            i += 1
        elif(j_list[j] <= i_list[i]):
            _return.append(j_list[j])
            j += 1

    # merge remaining items into _return
    if i < len(i_list):
        for _ in range(i, len(i_list)):
            _return.append(i_list[_])
    else:
        for _ in range(j, len(j_list)):
            _return.append(j_list[_])
    return _return
