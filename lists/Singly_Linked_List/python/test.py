import unittest
from singlyLinkedList import SinglyLinkedList, Node


class TestSinglyLinkedList(unittest.TestCase):

    def test_node_init(self):
        """
        Tests new Node initialization
        """
        node = Node('node_zero')
        self.assertIsInstance(node, Node)
        self.assertIsNone(node.next)
        self.assertEqual(node.data, 'node_zero')

    def test_list_init(self):
        """
        Test new SinglyLinkedList initialization
        """
        linkedList = SinglyLinkedList()
        self.assertIsInstance(linkedList, SinglyLinkedList)
        self.assertEqual(linkedList.length, 0)
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

    def test_push(self):
        """
        Tests the SinglyLinkedList.push(data) method
        """
        linkedList = SinglyLinkedList()

        # push first Node
        linkedList.push('node zero')
        self.assertEqual(linkedList.length, 1)
        self.assertIsInstance(linkedList.head, Node)
        self.assertIsInstance(linkedList.tail, Node)

        # push second Node
        linkedList.push('node one')
        self.assertEqual(linkedList.length, 2)
        self.assertEqual(linkedList.head.data, 'node zero')
        self.assertEqual(linkedList.tail.data, 'node one')
        self.assertEqual(linkedList.head.next.data, 'node one')

    def test_pop(self):
        """
        Tests the SinglyListedList.pop() method
        """
        linkedList = SinglyLinkedList()
        linkedList.push('node zero')
        linkedList.push('node one')
        linkedList.push('node two')
        self.assertEqual(linkedList.length, 3)
        popped = linkedList.pop()
        self.assertEqual(popped.data, 'node two')
        self.assertEqual(linkedList.length, 2)
        popped = linkedList.pop()
        self.assertEqual(popped.data, 'node one')
        self.assertEqual(linkedList.length, 1)
        popped = linkedList.pop()
        self.assertEqual(popped.data, 'node zero')
        self.assertEqual(linkedList.length, 0)
        popped = linkedList.pop()
        self.assertIsNone(popped)
        self.assertEqual(linkedList.length, 0)

    def test_unshift(self):
        """
        Tests the SinglyListedList.unshift(data) method
        """
        linkedList = SinglyLinkedList()
        linkedList.unshift('node last')
        self.assertEqual(linkedList.length, 1)
        self.assertEqual(linkedList.head.data, 'node last')
        self.assertEqual(linkedList.tail.data, 'node last')
        linkedList.unshift('node middle')
        self.assertEqual(linkedList.length, 2)
        self.assertEqual(linkedList.head.data, 'node middle')
        self.assertEqual(linkedList.tail.data, 'node last')
        linkedList.unshift('node first')
        self.assertEqual(linkedList.length, 3)
        self.assertEqual(linkedList.head.data, 'node first')
        self.assertEqual(linkedList.tail.data, 'node last')

    def test_shift(self):
        """
        Tests the SinglyListedList.shift() method
        """
        linkedList = SinglyLinkedList()
        linkedList.push(0)
        linkedList.push(1)
        linkedList.push(2)

        # shift node with data 0 from [0, 1, 2]
        shifted = linkedList.shift()
        self.assertIsInstance(shifted, Node)
        self.assertIsNone(shifted.next)
        self.assertEqual(shifted.data, 0)
        self.assertEqual(linkedList.head.data, 1)
        self.assertEqual(linkedList.tail.data, 2)
        self.assertEqual(linkedList.length, 2)

        # shift node with data 1 from [1, 2]
        shifted = linkedList.shift()
        self.assertIsInstance(shifted, Node)
        self.assertIsNone(shifted.next)
        self.assertEqual(shifted.data, 1)
        self.assertEqual(linkedList.head.data, 2)
        self.assertIsNone(linkedList.head.next)
        self.assertEqual(linkedList.tail.data, 2)
        self.assertIsNone(linkedList.tail.next)
        self.assertEqual(linkedList.length, 1)

        # shift node with data 2 from [2]
        shifted = linkedList.shift()
        self.assertIsInstance(shifted, Node)
        self.assertIsNone(shifted.next)
        self.assertEqual(shifted.data, 2)
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)
        self.assertEqual(linkedList.length, 0)

        # shift empty list
        shifted = linkedList.shift()
        self.assertIsNone(shifted)
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

    def test_get(self):
        """
        Tests the SinglyListedList.get(index) method
        """
        linkedList = SinglyLinkedList()
        linkedList.push(0)
        linkedList.push(1)
        linkedList.push(2)

        # check index of out bounds returns None
        self.assertIsNone(linkedList.get(-1))
        self.assertIsNone(linkedList.get(3))

        # test indices
        self.assertEqual(linkedList.get(0).data, 0)
        self.assertEqual(linkedList.get(1).data, 1)
        self.assertEqual(linkedList.get(2).data, 2)

        # last
        self.assertEqual(linkedList.get(linkedList.length - 1).data, 2)

    def test_insert(self):
        """
        Tests the SinglyListedList.insert(index, data) method
        successful insert returns true, else false
        """
        linkedList = SinglyLinkedList()

        # can insert index 0 of empty list
        self.assertFalse(linkedList.insert(1, 'false'))
        self.assertTrue(linkedList.insert(0, 'true'))

        # can insert at tail
        self.assertTrue(linkedList.insert(1, 'true'))

        # can not insert any index out of bounds
        self.assertFalse(linkedList.insert(999, 'node out of bounds'))
        self.assertFalse(linkedList.insert(-1, 'node out of bounds'))

        # can insert into middle of list
        # current list = ['true', 'true']
        self.assertTrue(linkedList.insert(1, 'middle node'))
        self.assertEqual(linkedList.to_list(), ['true', 'middle node', 'true'])

    def test_delete(self):
        """
        Tests the SinglyListedList.delete(index) method
        successful delete returns true, else false
        """
        linkedList = SinglyLinkedList()

        # can not delete from empty list
        self.assertFalse(linkedList.delete(0))

        # can delete from list with single item
        linkedList.push(1)
        self.assertEqual(linkedList.to_list(), [1])
        self.assertTrue(linkedList.delete(0))
        self.assertEqual(linkedList.to_list(), [])

        linkedList.push(1)
        linkedList.push(2)
        linkedList.push(3)

        # can not delete index out of bounds
        self.assertEqual(False, linkedList.delete(-1))
        self.assertEqual(False, linkedList.delete(999))

        # can delete tail, index 2
        self.assertEqual(linkedList.to_list(), [1, 2, 3])
        self.assertTrue(linkedList.delete(2))
        self.assertEqual(linkedList.to_list(), [1, 2])

        linkedList.push(3)
        self.assertEqual(linkedList.to_list(), [1, 2, 3])

        # can delete middle, index 1
        self.assertTrue(linkedList.delete(1))
        self.assertEqual(linkedList.to_list(), [1, 3])

        # can delete tail
        self.assertTrue(linkedList.delete(1))
        self.assertEqual(linkedList.to_list(), [1])

        # can not delete out bounds
        self.assertFalse(linkedList.delete(1))
        self.assertEqual(linkedList.to_list(), [1])

        # can delete index 0
        self.assertTrue(linkedList.delete(0))
        self.assertEqual(linkedList.to_list(), [])

    def test_reverse(self):
        """
        Tests the SinglyListedList.reverse() method
        """
        linkedList = SinglyLinkedList()
        linkedList.push(0)
        linkedList.push(1)
        self.assertEqual(linkedList.to_list(), [0, 1])

        linkedList.reverse()
        self.assertEqual(linkedList.to_list(), [1, 0])

        linkedList.reverse()  # back to [0, 1]
        linkedList.push(2)  # now [0, 1, 2]
        self.assertEqual(linkedList.to_list(), [0, 1, 2])
        linkedList.reverse()
        self.assertEqual(linkedList.to_list(), [2, 1, 0])

        linkedList = SinglyLinkedList()
        linkedList.push(0)
        linkedList.push(1)
        linkedList.push(2)
        linkedList.push(3)
        linkedList.push(4)
        linkedList.push(5)
        self.assertEqual(linkedList.to_list(), [0, 1, 2, 3, 4, 5])
        linkedList.reverse()
        self.assertEqual(linkedList.to_list(), [5, 4, 3, 2, 1, 0])

    def test_clear(self):
        """
        Tests the SinglyListedList.reverse() method
        """
        linkedList = SinglyLinkedList()
        linkedList.push(0)
        linkedList.push(1)
        linkedList.push(2)
        linkedList.push(3)
        linkedList.push(4)
        linkedList.push(5)
        self.assertEqual(linkedList.to_list(), [0, 1, 2, 3, 4, 5])
        self.assertIsInstance(linkedList.clear(), SinglyLinkedList)
        self.assertEqual(linkedList.to_list(), [])


if __name__ == "__main__":
    unittest.main()
