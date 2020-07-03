class Node:
    __slots__ = 'next', 'data'

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    LiFo Stack
    Methods:
    - to_list() - O(n)
        Returns list representation of stack, used for debugging
    - peek() - O(1)
        Returns the data on the top of the stack
    - push(data) - O(1)
        Push new data onto top of stack
    - pop() - O(1)
        Pops from top of stack
    """
    __slots__ = 'first', 'last', 'size'

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def to_list(self):
        """
        Converts the Stack into a python native datatype list
        O(N)
        @return {list}}
        """
        _return = []
        pointer = self.first
        while pointer is not None:
            _return.append(pointer.data)
            pointer = pointer.next
        return _return

    def peek(self):
        """
        Returns the data on the top of the stack
        @return {*}
        """
        if self.size == 0:
            return None
        return self.first.data

    def push(self, data):
        """
        Pushes data on to the top of the stack
        O(1)
        @param data {*}
        @return {number} size of the stack after the push
        """
        newNode = Node(data)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            tmp = self.first
            self.first = newNode
            self.first.next = tmp
        self.size += 1
        return self.size

    def pop(self):
        """
        Pops and returns the data at the top of the stack
        O(1)
        @return {*}
        """
        if self.first is None:
            return None
        if self.first == self.last:
            # If only one node, set last to None
            # this way when we set self.first = self.first.next
            # we are setting both nodes to None
            self.last = None
        poppedNode = self.first
        self.first = self.first.next
        poppedNode.next = None
        self.size -= 1
        return poppedNode.data
