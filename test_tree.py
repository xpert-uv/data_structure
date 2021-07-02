import unittest
from tree_class import Tree, TreeNode

class TestTreeClass(unittest.TestCase):
    def setUp(self):
        self.small_tree = Tree(TreeNode(1, [TreeNode(2)]))

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n8 = TreeNode(8)

        n1.children = [n2, n3, n4]
        n4.children = [n5, n6]
        n6.children = [n7]
        n7.children = [n8]

        self.large_tree = Tree(n1)

        self.empty_tree = Tree()

    def test_create(self):
        self.assertEqual(self.empty_tree.root, None)
        self.assertEqual(self.small_tree.root.val, 1)
        self.assertEqual(self.small_tree.root.children[0].val, 2)
        self.assertEqual(self.large_tree.root.val, 1)
        self.assertEqual(self.large_tree.root.children[1].val, 3)

    def test_sum_values(self):
        self.assertEqual(self.small_tree.sum_values(), 3)
        self.assertEqual(self.large_tree.sum_values(), 36)
        self.assertEqual(self.empty_tree.sum_values(), 0)

    def test_count_evens(self):
        self.assertEqual(self.small_tree.count_evens(), 1)
        self.assertEqual(self.large_tree.count_evens(), 4) 
        self.assertEqual(self.empty_tree.count_evens(), 0)  

    def test_num_greater(self):
        self.assertEqual(self.small_tree.num_greater(0), 2)
        self.assertEqual(self.small_tree.num_greater(1), 1)
        self.assertEqual(self.small_tree.num_greater(2), 0)
        self.assertEqual(self.small_tree.num_greater(3), 0)
        self.assertEqual(self.large_tree.num_greater(0), 8) 
        self.assertEqual(self.large_tree.num_greater(4), 4)
        self.assertEqual(self.large_tree.num_greater(8), 0)
        self.assertEqual(self.empty_tree.num_greater(0), 0)