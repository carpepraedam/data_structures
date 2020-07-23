class Node:
    """
    Class representation of a Binary Search Tree Node
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Class representation of a Binary Search Tree
    Methods:
    - insert(data) - O(log n)
        Inserts a new Node containing data into the BST
    - find(data) - O(log n)
        Traverses tree from root to see if data exists in tree
    - breadth_first_search() - O(n)
        returns list of tee data using bfs algorithm
    - depth_first_pre_order_search() - O(n)
        returns list of tee data using dfs pre order algorithm
    - depth_first_in_order_search() - O(n)
        returns list of tee data using dfs in order algorithm
    """

    def __init__(self):
        self.root = None

    def insert(self, data, checkNode=None):
        """
        Inserts a new Node containing data into the BST

        @param data {*} data to insert
        @param checkNode {Node} the node to start the insert recursion from.
            Defaults to self.root
        """
        # Tree is empty, set the the root to be the new node
        if self.root is None:
            # create an instance of a Node to insert
            newNode = Node(data)
            self.root = newNode
            return

        # if the checkNode is None, start from root
        if checkNode == None:
            checkNode = self.root

        # If tree is not empty, compare data value to checkNode.data
        # if data < checkNode.data, move to the left recursively
        # if data > checkNode.data, move to the right recursively
        # if data == checkNode.data, ignore it
        if data < checkNode.data:
            # moving left, first check if the left node exists
            # if it does not, create a new Node and insert it there
            # if it does, recursively call insert passing in the left Node
            if checkNode.left == None:
                checkNode.left = Node(data)
            else:
                return self.insert(data, checkNode=checkNode.left)

        if data > checkNode.data:
            # repeat process above, but moving right
            if checkNode.right == None:
                checkNode.right = Node(data)
            else:
                return self.insert(data, checkNode=checkNode.right)

    def find(self, data):
        """
        Traverses tree from root to see if data exists in tree
        @data {*} data to check for
        @return {bool || Node}
            Bool (False) if the data was not found
            Node if the data was found
        """
        if self.root == None:
            return False

        # traverse iteratively
        found = False
        currentNode = self.root
        while currentNode and not found:
            if data < currentNode.data:
                currentNode = currentNode.left
            elif data > currentNode.data:
                currentNode = currentNode.right
            else:
                found = True
        if not found:
            return False
        return currentNode

    def breadth_first_search(self):
        """
        Breadth first search implementation
        O(n)
        @return list
        """
        if self.root is None:
            return []

        # initialize queue (list) and visited list
        queue = []
        visited = []

        queue.append(self.root)
        while len(queue) > 0:
            # pop the first node from the queue
            popped = queue.pop(0)
            # added the popped node data to visited
            visited.append(popped.data)

            # add left and right nodes to the queue if needed
            if popped.left != None:
                queue.append(popped.left)
            if popped.right != None:
                queue.append(popped.right)
        return visited

    def depth_first_pre_order_search(self):
        """
        Depth first pre order search implementation
        O(n)
        @return list
        """
        data = []

        def traverse(node):
            if node is None:
                return
            data.append(node.data)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data

    def depth_first_post_order_search(self):
        """
        Depth first post order search implementation
        O(n)
        @return list
        """
        data = []

        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.data)
        traverse(self.root)
        return data

    def depth_first_in_order_search(self):
        """
        Depth first in order search implementation
        O(n)
        @return list
        """
        data = []

        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            data.append(node.data)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data
