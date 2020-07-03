class Node:
    __slots__ = 'next', 'data'

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    FiFo Queue
    Methods:
    - to_list() - O(n)
        Returns list representation of queue, used for debugging
    - enqueue(data) - O(1)
        Enter data at the end of the queue
    - dequeue() - O(1)
        Remove data from the start of the queue
    """
    __slots__ = 'first', 'last', 'size'

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def to_list(self):
        """
        Converts the Queue into a python native datatype list
        O(N)
        @return {list}}
        """
        _return = []
        pointer = self.first
        while pointer is not None:
            _return.append(pointer.data)
            pointer = pointer.next
        return _return

    def enqueue(self, data):
        """
        Enter data at the end of the queue
        O(1)
        @param data {*} data to enqueue
        @return {number} current size of queue
        """
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
        return self.size

    def dequeue(self):
        """
        Enter data at the end of the queue
        O(1)
        @return {*} dequeued data
        """
        if self.first is None:
            return None
        if self.first is self.last:
            # If only one node, set last to None
            # this way when we set self.first = self.first.next
            # we are setting both nodes to None
            self.last = None
        dequeued = self.first
        self.first = dequeued.next
        dequeued.next = None
        self.size -= 1
        return dequeued.data
