import unittest

from bst import BST, Node


class BSTTests(unittest.TestCase):

    def test_init_node(self):
        """
        Tests initialization of Node
        """
        n1 = Node('data')
        self.assertIsInstance(n1, Node)
        self.assertEqual(n1.data, 'data')
        self.assertIsNone(n1.left)
        self.assertIsNone(n1.right)
        # make sure 'value' is writeable
        n1.data = "new_val"
        self.assertEqual(n1.data, 'new_val')

    def test_init_bst(self):
        """
        Test initialization of BST
        """
        bst = BST()
        self.assertIsInstance(bst, BST)
        self.assertIsNone(bst.root)

    def test_interface(self):
        """
        Tests that the publically exposed methods are available
        """
        bst = BST()
        # test 'insert' attribute exists ad is a callable
        self.assertTrue(hasattr(bst, 'insert'))
        self.assertTrue(callable(getattr(bst, 'insert')))
        # test 'find' attribute exists and is a callable
        self.assertTrue(hasattr(bst, 'find'))
        self.assertTrue(callable(getattr(bst, 'find')))
        # test 'breadth_first_search' attribute exists and is a callable
        self.assertTrue(hasattr(bst, 'breadth_first_search'))
        self.assertTrue(callable(getattr(bst, 'breadth_first_search')))
        # test 'depth_first_pre_order_search' attribute exists and is a callable
        self.assertTrue(hasattr(bst, 'depth_first_pre_order_search'))
        self.assertTrue(callable(getattr(bst, 'depth_first_pre_order_search')))
        # test 'depth_first_post_order_search' attribute exists and is a callable
        self.assertTrue(hasattr(bst, 'depth_first_post_order_search'))
        self.assertTrue(
            callable(getattr(bst, 'depth_first_post_order_search')))
        # test 'depth_first_in_order_search' attribute exists and is a callable
        self.assertTrue(hasattr(bst, 'depth_first_in_order_search'))
        self.assertTrue(
            callable(getattr(bst, 'depth_first_in_order_search')))

    def test_insert(self):
        """
        Test the bst.insert(data) method
        """
        bst = BST()
        self.assertIsNone(bst.root)
        # 1st insert should become root
        bst.insert(50)
        self.assertIsInstance(bst.root, Node)
        self.assertEqual(bst.root.data, 50)

        # Working on depth = 1,
        # insert 25, this should go the left of 50
        bst.insert(25)
        leaf = bst.root.left
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 25)

        # Working on depth = 1
        # insert 75, this should go to the right of 50
        bst.insert(75)
        leaf = bst.root.right
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 75)

        # Working depth = 2
        # insert 13, this should go the left of 25
        bst.insert(13)
        leaf = bst.root.left.left
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 13)

        # Working depth = 2
        # insert 35, this should go the right of 25
        bst.insert(35)
        leaf = bst.root.left.right
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 35)

        # Working on depth = 2
        # insert 88, this should go to the right of 75
        bst.insert(88)
        leaf = bst.root.right.right
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 88)

        # Working on depth = 2
        # insert 80, this should go to the right of 75 and to the left of 88
        bst.insert(80)
        leaf = bst.root.right.right.left
        self.assertIsInstance(leaf, Node)
        self.assertEqual(leaf.data, 80)

    def test_find(self):
        """
        Tests the bst.find(data) method
        """
        bst = BST()
        # root does not exist, so no values should exist in tree
        self.assertFalse(bst.find(1))
        bst.insert(50)
        bst.insert(25)  # depth 1
        bst.insert(75)  # depth 1
        bst.insert(13)  # depth 2
        bst.insert(35)  # depth 2
        bst.insert(65)  # depth 2
        bst.insert(80)  # depth 2

        found = bst.find(50)
        self.assertEqual(found.data, 50)  # 50 exists in tree
        self.assertIsInstance(bst.find(50), Node)
        self.assertTrue(bst.find(35))  # 34 exists in tree
        self.assertFalse(bst.find(100))  # 100 does not exist in tree
        self.assertFalse(bst.find(-1))  # -1 does not exist in tree
        self.assertIsInstance(bst.find(-1), bool)

    def test_breadth_first_search(self):
        """
        Tests the breadth first search implementation
        """
        bst = BST()
        # root does not exist, so no values should exist in tree
        expected = []
        self.assertEqual(bst.breadth_first_search(), expected)
        bst.insert(50)
        expected = [50]
        self.assertEqual(bst.breadth_first_search(), expected)

        bst.insert(25)  # depth 1
        bst.insert(75)  # depth 1
        expected = [50, 25, 75]
        self.assertEqual(bst.breadth_first_search(), expected)

        bst.insert(13)  # depth 2
        bst.insert(35)  # depth 2
        bst.insert(88)  # depth 2
        bst.insert(65)  # depth 2
        expected = [50, 25, 75, 13, 35, 65, 88]
        self.assertEqual(bst.breadth_first_search(), expected)

    def test_depth_first_pre_order_search(self):
        """
        Tests the depth_first_pre_order_search implementation
        """
        bst = BST()
        # root does not exist, so no values should exist in tree
        expected = []
        self.assertEqual(bst.depth_first_pre_order_search(), expected)
        bst.insert(50)
        expected = [50]
        self.assertEqual(bst.depth_first_pre_order_search(), expected)

        bst.insert(25)  # depth 1
        bst.insert(75)  # depth 1
        expected = [50, 25, 75]
        self.assertEqual(bst.depth_first_pre_order_search(), expected)

        bst.insert(13)  # depth 2
        bst.insert(35)  # depth 2
        bst.insert(88)  # depth 2
        bst.insert(65)  # depth 2
        expected = [50, 25, 13, 35, 75, 65, 88]
        self.assertEqual(bst.depth_first_pre_order_search(), expected)

    def test_depth_first_post_order_search(self):
        """
        Tests the depth_first_post_order_search() implementation
        """
        bst = BST()
        # root does not exist, so no values should exist in tree
        expected = []
        self.assertEqual(bst.depth_first_post_order_search(), expected)
        bst.insert(50)
        expected = [50]
        self.assertEqual(bst.depth_first_post_order_search(), expected)

        bst.insert(25)  # depth 1
        bst.insert(75)  # depth 1
        expected = [25, 75, 50]
        self.assertEqual(bst.depth_first_post_order_search(), expected)

        bst.insert(13)  # depth 2
        bst.insert(35)  # depth 2
        bst.insert(88)  # depth 2
        bst.insert(65)  # depth 2
        expected = [13, 35, 25, 65, 88, 75, 50]
        self.assertEqual(bst.depth_first_post_order_search(), expected)

    def test_depth_first_in_order_search(self):
        """
        Tests the depth_first_in_order_search() implementation
        """
        bst = BST()
        # root does not exist, so no values should exist in tree
        expected = []
        self.assertEqual(bst.depth_first_in_order_search(), expected)
        bst.insert(50)
        expected = [50]
        self.assertEqual(bst.depth_first_in_order_search(), expected)

        bst.insert(25)  # depth 1
        bst.insert(75)  # depth 1
        expected = [25, 50, 75]
        self.assertEqual(bst.depth_first_in_order_search(), expected)

        bst.insert(13)  # depth 2
        bst.insert(35)  # depth 2
        bst.insert(88)  # depth 2
        bst.insert(65)  # depth 2
        expected = [13, 25, 35, 50, 65, 75, 88]
        self.assertEqual(bst.depth_first_in_order_search(), expected)


if __name__ == "__main__":
    unittest.main()
