import unittest

from stack import Stack, Node


class StackTests(unittest.TestCase):

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

    def test_init_stack(self):
        """
        Test initialization of Stack
        """
        s = Stack()
        self.assertIsInstance(s, Stack)
        self.assertIsNone(s.first)
        self.assertIsNone(s.last)
        self.assertEqual(s.size, 0)

    def test_interface(self):
        """
        Tests that the publically exposed methods are available
        """
        s = Stack()
        # test 'to_list' attribute exists an is a callable
        self.assertTrue(hasattr(s, 'to_list'))
        self.assertTrue(callable(getattr(s, 'to_list')))

        # test 'to_list' attribute exists an is a callable
        self.assertTrue(hasattr(s, 'peek'))
        self.assertTrue(callable(getattr(s, 'peek')))

        # test 'push' attribute exists an is a callable
        self.assertTrue(hasattr(s, 'push'))
        self.assertTrue(callable(getattr(s, 'push')))

        # test 'pop' attribute exists an is a callable
        self.assertTrue(hasattr(s, 'pop'))
        self.assertTrue(callable(getattr(s, 'pop')))

    def test_push(self):
        """
        Tests the stack.push(data) method
        """
        s = Stack()
        self.assertEqual(s.to_list(), [])
        self.assertEqual(s.size, 0)

        # push
        pushval = s.push('a')
        self.assertEqual(s.size, 1)
        self.assertEqual(pushval, 1)  # returns size of stack
        self.assertEqual(s.to_list(), ['a'])

        # push
        pushval = s.push('b')
        self.assertEqual(s.size, 2)
        self.assertEqual(pushval, 2)  # returns size of stack
        self.assertEqual(s.to_list(), ['b', 'a'])

    def test_peek(self):
        """
        Tests the stack.peek() method
        """
        s = Stack()
        # peek on empty list should return None
        self.assertIsNone(s.peek())

        s.push('a')
        self.assertEqual(s.peek(), 'a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
        s.push('c')
        self.assertEqual(s.peek(), 'c')

    def test_pop(self):
        """
        Tests the stack.pop() method
        """
        s = Stack()
        # pop on empty list should return None
        self.assertIsNone(s.pop())

        # setup stack
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size, 3)
        self.assertEqual(s.to_list(), ['c', 'b', 'a'])

        # start popping
        popped = s.pop()
        self.assertEqual(popped, 'c')
        self.assertEqual(s.size, 2)
        self.assertEqual(s.to_list(), ['b', 'a'])
        popped = s.pop()
        self.assertEqual(popped, 'b')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.to_list(), ['a'])
        popped = s.pop()
        self.assertEqual(popped, 'a')
        self.assertEqual(s.size, 0)
        self.assertEqual(s.to_list(), [])
        popped = s.pop()
        self.assertEqual(popped, None)
        self.assertEqual(s.size, 0)
        self.assertEqual(s.to_list(), [])


if __name__ == "__main__":
    unittest.main()
