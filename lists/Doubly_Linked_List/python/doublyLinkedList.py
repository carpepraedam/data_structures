class Node:
    """
    Class representation of a Node for use in a
    Doubly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Representation of a Singly Linked List
    Methods:
    - to_list() - O(N)
        returns a list representation of the SinglyLinkedList
    - push(data) - O(1)
        adds data onto the end of the list
    - pop() - O(1)
        removes and returns the last node in the list
    - unshift(data) - O(1)
        adds data to the front of the list
    - shift() - O(1)
        removes first element in list
    - get(index) - O(N/2)
        returns Node at index
    - set(index, data) - O(N/2)
        sets the data at the given index
    - insert(index, data) - O(N/2)
        inserts data at index 
    - delete(index) - O(N/2)
        removes node at index
    - clear() - O(1)
        Removes all nodes
    """

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def to_list(self):
        """
        Converts the Linked List into a python native datatype List
        O(N)
        @return List
        """
        returnList = []
        if(self.length <= 0):
            return returnList
        currentNode = self.head
        while(currentNode is not None):
            returnList.append(currentNode.data)
            currentNode = currentNode.next
        return returnList

    def push(self, data):
        """
        Adds data to the end of the list
        O(1)
        @param {*} data
        @return DoublyLinkedList
        """
        newNode = Node(data)
        if(self.length == 0):
            # empty list, set head and tail, do not set next/prev
            self.head = newNode
            self.tail = newNode
        else:
            # list not empty, push newNode right of tail
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        """
        Removes and returns the last node in the list
        O(1)
        @return Node || None
        """
        if(self.length == 0):
            return None
        # pop the tail
        popped = self.tail
        if(self.length == 1):
            # single node in list, remove the head
            # and null out head/tail
            self.head = None
            self.tail = None
        else:
            # set the new tail to popped.prev
            self.tail = popped.prev
            self.tail.next = None

        self.length -= 1
        popped.prev = None
        return popped

    def unshift(self, data):
        """
        Adds data to the front of the list
        O(1)
        @param {*} data
        @return DoublyLinkedList
        """
        if(self.length == 0):
            return self.push(data)

        newNode = Node(data)
        # connect newNode and self.head
        self.head.prev = newNode
        newNode.next = self.head
        # set head to newNode
        self.head = newNode

        self.length += 1
        return self

    def shift(self):
        """
        Removes data from the front of the list
        O(1)
        @return Node || None
        """
        if(self.length == 0):
            return None
        if(self.length == 1):
            return self.pop()
        shifted = self.head
        # move head right and remove references to prev
        self.head = self.head.next
        self.head.prev = None
        # remove shift references to next
        shifted.next = None
        # increment lenth and return node
        self.length -= 1
        return shifted

    def get(self, index):
        """
        Get node at index
        O(N/2)
        @param {number} index
        @return Node || None
        """
        if (index < 0) or (index >= self.length):
            return None

        currentNode = None
        if (index > self.length / 2):
            # index is right of halfway, work left from tail
            currentNode = self.tail
            for _ in range(self.length - 1, index, -1):
                # from 0 to index (exclusive)
                # ex: index = 5, loop from 0 to 4
                currentNode = currentNode.prev
        else:
            # index is left of halfway, work right from head
            currentNode = self.head
            for _ in range(0, index):
                # from 0 to index (exclusive)
                # ex: index = 5, loop from 0 to 4
                currentNode = currentNode.next
        return currentNode

    def set(self, index, data):
        node = self.get(index)
        if(node is not None):
            node.data = data
        return node

    def insert(self, index, data):
        """
        inserts data at index
        O(N/2) 
        @param {number} index
        @param {*} data
        @return DoublyLinkedList || None
        """
        if (index < 0) or (index > self.length):
            return None
        if (index == 0):
            # insert at head, push
            return self.unshift(data)
        if (index == self.length):
            return self.push(data)

        newNode = Node(data)
        indexNode = self.get(index)

        # push indexNode node right, inserting newNode at the given index
        newNode.next = indexNode
        newNode.prev = indexNode.prev
        indexNode.prev.next = newNode
        indexNode.prev = newNode

        self.length += 1
        return self

    def delete(self, index):
        """
        Removes and returns node at index
        O(N/2)
        @param {number} index
        @return None || None
        """
        if(index < 0) or (index >= self.length):
            return None
        if(index == 0):
            # deleting from head, just shift
            return self.shift()
        if(index == self.length - 1):
            return self.pop()

        # remove node at index, and create connections between
        # the neighboring left and right nodes
        indexNode = self.get(index)
        prevNode = indexNode.prev
        nextNode = indexNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        self.length -= 1
        return indexNode

    def clear(self):
        """
        Empties list
        O(1)
        @return DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.length = 0
        return self
