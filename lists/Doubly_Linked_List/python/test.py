import unittest
from doublyLinkedList import DoublyLinkedList, Node


class TestDoublyLinkedList(unittest.TestCase):

    def test_node_init(self):
        """
        Tests new Node initialization
        """
        node = Node('node_zero')
        self.assertIsInstance(node, Node)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        self.assertEqual(node.data, 'node_zero')

    def test_list_init(self):
        """
        Test new DoublyLinked List initialization
        """
        dll = DoublyLinkedList()
        self.assertIsInstance(dll, DoublyLinkedList)
        self.assertEqual(dll.length, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_to_list(self):
        """
        Tests the to_list() method
        """
        dll = DoublyLinkedList()
        self.assertEqual(dll.to_list(), [])

    def test_push(self):
        """
        Tests the push(data) method
        """
        dll = DoublyLinkedList()
        dll.push('node zero')
        self.assertEqual(dll.length, 1)
        self.assertIsNotNone(dll.head)
        self.assertIsNotNone(dll.tail)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.tail.prev)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll.head.data, 'node zero')
        self.assertEqual(dll.tail.data, 'node zero')
        dll.push('node one')
        self.assertEqual(dll.length, 2)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll.head.data, 'node zero')
        self.assertEqual(dll.tail.data, 'node one')
        self.assertEqual(dll.head.next.data, 'node one')
        self.assertEqual(dll.tail.prev.data, 'node zero')

    def test_pop(self):
        """
        Tests the pop() method
        """
        dll = DoublyLinkedList()

        # test with no nodes
        self.assertIsNone(dll.pop())

        # test with one node
        dll.push('node zero')
        self.assertEqual(dll.length, 1)
        popped = dll.pop()
        self.assertEqual(dll.length, 0)
        self.assertEqual(popped.data, "node zero")

        # test with two nodes
        dll.push('node zero')
        dll.push('node one')
        self.assertEqual(dll.head.data, 'node zero')
        self.assertEqual(dll.tail.data, 'node one')
        self.assertEqual(dll.length, 2)
        popped = dll.pop()
        self.assertEqual(popped.data, 'node one')
        self.assertEqual(dll.length, 1)

        # test pop prev, next are None
        self.assertIsNone(popped.prev)
        self.assertIsNone(popped.next)

    def test_unshift(self):
        """
        Tests the unshift(data) method
        """
        # test empty list
        dll = DoublyLinkedList()
        self.assertEqual(dll.length, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        dll.unshift('node zero')
        self.assertEqual(dll.length, 1)
        self.assertEqual(dll.head.data, 'node zero')

        # test one node
        expected_list = ['node zero']
        self.assertEqual(dll.to_list(), expected_list)
        unshifted = dll.unshift('node subzero')
        self.assertIsInstance(unshifted, DoublyLinkedList)
        self.assertEqual(dll.length, 2)
        expected_list = ['node subzero', 'node zero']
        self.assertEqual(dll.to_list(), expected_list)

        # test with two nodes
        unshifted = dll.unshift('node subsubzero')
        self.assertIsInstance(unshifted, DoublyLinkedList)
        self.assertEqual(dll.length, 3)
        expected_list = ['node subsubzero', 'node subzero', 'node zero']
        self.assertEqual(dll.to_list(), expected_list)

    def test_shift(self):
        """
        Tests the shift() method
        """
        dll = DoublyLinkedList()

        # test shifting empty list
        self.assertIsNone(dll.shift())

        # test one node
        dll.push('node zero')
        self.assertEqual(dll.length, 1)
        shifted = dll.shift()
        self.assertEqual(dll.length, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(shifted.data, 'node zero')
        self.assertIsNone(shifted.next)
        self.assertIsNone(shifted.prev)

        # test two nodes
        dll.push('node one')
        dll.push('node two')
        self.assertEqual(dll.length, 2)
        shifted = dll.shift()
        self.assertEqual(dll.length, 1)
        expected_list = ['node two']
        self.assertEqual(dll.to_list(), expected_list)
        self.assertIsNone(shifted.next)
        self.assertIsNone(shifted.prev)

        # test three nodes
        dll = DoublyLinkedList()
        dll.push('node one')
        dll.push('node two')
        dll.push('node three')
        self.assertEqual(dll.length, 3)
        shifted = dll.shift()
        self.assertEqual(dll.length, 2)
        expected_list = ['node two', 'node three']
        self.assertEqual(dll.to_list(), expected_list)
        self.assertIsNone(shifted.next)
        self.assertIsNone(shifted.prev)

    def test_get(self):
        """
        Tests the get(index) method
        """
        dll = DoublyLinkedList()
        dll.push(0)  # index 0
        dll.push(1)  # index 1
        dll.push(2)  # index 2
        dll.push(3)  # index 3
        dll.push(4)  # index 4
        dll.push(5)  # index 5
        self.assertEqual(dll.length, 6)

        # test out of bounds
        self.assertIsNone(dll.get(-1))
        self.assertIsNone(dll.get(99))
        self.assertIsNone(dll.get(6))

        self.assertEqual(dll.get(0).data, 0)
        self.assertEqual(dll.get(3).data, 3)
        self.assertEqual(dll.get(4).data, 4)
        self.assertEqual(dll.get(5).data, 5)

    def test_set(self):
        """
        Tests the set(index, data) method
        """
        dll = DoublyLinkedList()

        # test empty list
        self.assertIsNone(dll.set(0, 'data'))

        # test out of bounds
        self.assertIsNone(dll.set(-1, 'data'))
        self.assertIsNone(dll.set(1, 'data'))

        dll.push(0)  # index 0
        dll.push(1)  # index 1
        dll.push(2)  # index 2
        dll.push(3)  # index 3
        dll.push(4)  # index 4
        dll.push(5)  # index 5
        self.assertEqual(dll.length, 6)

        self.assertIsInstance(dll.set(2, "index 2"), Node)
        expected_list = [0, 1, 'index 2', 3, 4, 5]
        self.assertEqual(dll.to_list(), expected_list)

    def test_insert(self):
        """
        Tests the insert(index, data) method
        """
        dll = DoublyLinkedList()

        # test out of bounds
        self.assertIsNone(dll.insert(-1, 'data'))
        self.assertIsNone(dll.insert(1, 'data'))

        # test inserting at index zero in open list (should use unshift(data))
        dll.insert(0, 'node zero')
        self.assertEqual(dll.length, 1)
        self.assertEqual(dll.head.data, 'node zero')

        dll.clear()
        dll.push(0)  # index 0
        dll.push(1)  # index 1
        dll.push(2)  # index 2

        # insert at index 1
        expected_list = [0, 'insert one', 1, 2]
        self.assertIsInstance(dll.insert(1, 'insert one'), DoublyLinkedList)
        self.assertEqual(dll.length, 4)
        self.assertEqual(dll.to_list(), expected_list)

        # insert at tail, index 4
        expected_list = [0, 'insert one', 1, 2, 'insert tail']
        self.assertIsInstance(dll.insert(4, 'insert tail'), DoublyLinkedList)
        self.assertEqual(dll.length, 5)
        self.assertEqual(dll.to_list(), expected_list)

    def test_delete(self):
        """
        tests the delete(index) method
        """
        dll = DoublyLinkedList()

        # test out of bounds
        self.assertIsNone(dll.delete(-1))
        self.assertIsNone(dll.delete(1))

        dll.push(0)  # index 0
        dll.push(1)  # index 1
        dll.push(2)  # index 2

        # test can delete head (index 0)
        deleted = dll.delete(0)
        self.assertIsInstance(deleted, Node)
        self.assertEqual(deleted.data, 0)
        self.assertEqual(dll.length, 2)

        # unshift the node back, then test delete at tail (index 2)
        dll.unshift(0)
        self.assertEqual(dll.to_list(), [0, 1, 2])
        self.assertEqual(dll.length, 3)
        deleted = dll.delete(dll.length - 1)  # index 2
        self.assertIsInstance(deleted, Node)
        self.assertEqual(deleted.data, 2)
        self.assertEqual(dll.length, 2)

        # push the node back, then test delete from middle (index 1)
        dll.push(2)
        self.assertEqual(dll.to_list(), [0, 1, 2])
        self.assertEqual(dll.length, 3)
        deleted = dll.delete(1)
        self.assertIsInstance(deleted, Node)
        self.assertEqual(deleted.data, 1)
        self.assertEqual(dll.length, 2)

    def test_clear(self):
        """
        Tests the clear() method
        """
        dll = DoublyLinkedList()
        dll.push('node one')
        dll.push('node two')
        dll.push('node three')
        self.assertEqual(dll.length, 3)
        self.assertIsInstance(dll.clear(), DoublyLinkedList)
        self.assertEqual(dll.length, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)


if __name__ == "__main__":
    unittest.main()
