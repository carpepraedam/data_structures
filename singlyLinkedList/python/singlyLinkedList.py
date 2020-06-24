class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    """
    Representation of a Singly Linked List
    Methods:
    - to_list() - O(N)
        returns a list representation of the SinglyLinkedList
    - push(data) - O(1)
        adds data onto the end of the list
    - pop() - O(N)
        removes and returns the last node in the list
    - unshift(data) - O(1)
        adds data to the front of the list
    - shift() - O(1)
        removes first element in list
    - get(index) - O(N)
        returns Node at index
    - insert(index, data) - O(N)
        inserts data at index
    - delete(index) - O(N)
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
        Converts the SinglyLinkedList into a python native datatype list
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
        Push a new node to the end of the SinglyLinkedList
        O(1)
        @param {*} data - Node data
        @return SinglyLinkedList
        """
        newNode = Node(data)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        """
        Remove and return the last node of the list
        O(N)
        @return Node | None
        """
        poppedNode = None
        if(self.length == 0):
            return None
        elif(self.length == 1):
            poppedNode = self.tail
            self.head = None
            self.tail = None
        else:
            # at least two nodes in list, find tail and the node before tail
            # start at head and iterate over list keeping track of
            # two pointers: prevNode and currentNode
            # while currentNode.next != None, move both pointers right
            # if currentNode.next is None, you are at the tail, exit iteration
            # currentNode will point to tail
            # prevNode will point to node before tail (which will be the new tail)
            currentNode = self.head
            prevNode = None
            while(currentNode.next is not None):
                prevNode = currentNode
                currentNode = currentNode.next

            poppedNode = currentNode
            self.tail = prevNode
            self.tail.next = None
        self.length -= 1
        return poppedNode

    def unshift(self, data):
        """
        Add a new node to the beginning of the SinglyLinkedList
        O(N)
        @param {*} data - Node data
        @return SinglyLinkedList
        """
        if(self.length == 0):
            return self.push(data)

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def shift(self):
        """
        Removes and returns the first node in the list
        O(1)
        @return Node | None
        """
        if(self.length == 0):
            return None

        shiftedNode = None
        if(self.length == 1):
            shiftedNode = self.head
            self.head = None
            self.tail = None
        else:
            shiftedNode = self.head
            self.head = self.head.next

        shiftedNode.next = None
        self.length -= 1
        return shiftedNode

    def get(self, index):
        """
        Returns node at given index
        O(N)
        @param {number} index
        @return Node | None
        """
        if(self.length == 0):
            return None
        if(index < 0 or index > self.length - 1):
            return None

        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next

        return currentNode

    def insert(self, index, data):
        """
        Inserts data at given index
        O(N)
        @param {number} index
        @param {*} data
        @return Boolean
        """
        # if insert at head
        if(index < 0 or index > self.length):
            return False
        if(index == 0):
            return bool(self.unshift(data))
        # if insert at tail
        if(index == self.length):
            return bool(self.push(data))
        newNode = Node(data)
        leftNode = self.get(index - 1)
        newNode.next = leftNode.next
        leftNode.next = newNode
        return True

    def delete(self, index):
        """
        Deltes node at given index
        O(N)
        @param {number} index
        @return Boolean
        """
        if((index < 0) or (index > self.length - 1) or (self.length == 0)):
            return False
        if(index == 0):
            # one none in list, pop it
            return bool(self.shift())
        if(index == self.length - 1):
            # deleting from tail
            return bool(self.pop())

        currentNode = self.head
        prevNode = currentNode
        for _ in range(0, index):
            prevNode = currentNode
            currentNode = currentNode.next

        # currentNode is the node to be delete
        prevNode.next = currentNode.next
        currentNode.next = None
        self.length -= 1
        return True

    def reverse(self):
        """
        Reverses the list
        O(N)
        @return SinglyLinkedList
        """
        if(self.length <= 1):
            return self
        if(self.length == 2):
            self.tail.next = self.head
            self.head.next = None
            self.head = self.tail
            self.tail = self.head.next
            return self

        currentNode = self.head
        rightNode = currentNode.next
        leftNode = None

        while(rightNode):
            # move all pointers right
            leftNode = currentNode
            currentNode = rightNode
            rightNode = rightNode.next

            # swap .next attributes
            currentNode.next = leftNode

        self.tail = self.head
        self.tail.next = None
        self.head = currentNode
        return self

    def clear(self):
        """
        Removes all nodes and resets list
        Note this does not clear and nodes in memory, so any pointers
        to nodes that currently exist will still exist, and will still
        have their next attribute set. This simply sets the head and
        tail of the list to empty, and resets length to 0
        @return SinglyLinkedList
        """
        self.length = 0
        self.head = None
        self.tail = None
        return self
