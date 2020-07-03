import unittest

from queue import Queue, Node


class QueueTests(unittest.TestCase):

    def test_init_node(self):
        """
        Tests initialization of Node
        """
        n1 = Node('data')
        self.assertIsInstance(n1, Node)
        self.assertEqual(n1.data, 'data')
        self.assertIsNone(n1.next)
        # make sure 'value' is writeable
        n1.data = "new_val"
        self.assertEqual(n1.data, 'new_val')
        # make sure 'next' is writeable
        n2 = Node('new_node')
        n1.next = n2

    def test_init_queue(self):
        """
        Test initialization of Queue
        """
        q = Queue()
        self.assertIsInstance(q, Queue)
        self.assertIsNone(q.first)
        self.assertIsNone(q.last)
        self.assertEqual(q.size, 0)

    def test_interface(self):
        """
        Tests that the publically exposed methods are available
        """
        q = Queue()
        # test 'to_list' attribute exists an is a callable
        self.assertTrue(hasattr(q, 'to_list'))
        self.assertTrue(callable(getattr(q, 'to_list')))

        # test 'enqueue' attribute exists an is a callable
        self.assertTrue(hasattr(q, 'enqueue'))
        self.assertTrue(callable(getattr(q, 'enqueue')))

        # test 'dequeue' attribute exists an is a callable
        self.assertTrue(hasattr(q, 'dequeue'))
        self.assertTrue(callable(getattr(q, 'dequeue')))

    def test_enqueue(self):
        """
        Tests the queue.enqueue(data) method
        """
        q = Queue()
        self.assertEqual(q.to_list(), [])
        self.assertEqual(q.size, 0)

        result = q.enqueue('first')
        self.assertEqual(q.to_list(), ['first'])
        self.assertEqual(q.size, 1)
        self.assertEqual(result, 1)  # should return size of list

        result = q.enqueue('second')
        self.assertEqual(q.to_list(), ['first', 'second'])
        self.assertEqual(q.size, 2)
        self.assertEqual(result, 2)  # should return size of list

        result = q.enqueue('third')
        self.assertEqual(q.to_list(), ['first', 'second', 'third'])
        self.assertEqual(q.size, 3)
        self.assertEqual(result, 3)  # should return size of list

    def test_dequeue(self):
        """
        Tests the queue.dequeue() method
        """
        q = Queue()
        self.assertEqual(q.to_list(), [])
        self.assertEqual(q.size, 0)

        result = q.enqueue('first')
        result = q.enqueue('second')
        result = q.enqueue('third')
        self.assertEqual(q.to_list(), ['first', 'second', 'third'])
        self.assertEqual(q.size, 3)

        result = q.dequeue()
        self.assertEqual(result, 'first')  # should return data of first node
        self.assertEqual(q.to_list(), ['second', 'third'])
        self.assertEqual(q.size, 2)

        result = q.dequeue()
        self.assertEqual(result, 'second')
        self.assertEqual(q.to_list(), ['third'])
        self.assertEqual(q.size, 1)

        result = q.dequeue()
        self.assertEqual(result, 'third')
        self.assertEqual(q.to_list(), [])
        self.assertEqual(q.size, 0)

        result = q.dequeue()
        self.assertEqual(result, None)
        self.assertEqual(q.to_list(), [])
        self.assertEqual(q.size, 0)


if __name__ == "__main__":
    unittest.main()
