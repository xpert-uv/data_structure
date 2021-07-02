import unittest
from binary_tree_class import BinaryTree, BinaryTreeNode

class TestBinaryTreeClass(unittest.TestCase):
    def setUp(self):
        self.empty_tree = BinaryTree()

        sLeft = BinaryTreeNode(5)
        sRight = BinaryTreeNode(4)
        self.small_tree = BinaryTree(BinaryTreeNode(6, sLeft, sRight))

        n6 = BinaryTreeNode(1)
        n5 = BinaryTreeNode(1)
        n4 = BinaryTreeNode(2)
        n3 = BinaryTreeNode(3, n4, n6)
        n2 = BinaryTreeNode(5, n3, n5)
        n1 = BinaryTreeNode(6)
        root = BinaryTreeNode(8, n1, n2)
        self.large_tree = BinaryTree(root)

    def test_create(self):
        self.assertEqual(self.empty_tree.root, None)
        self.assertEqual(self.small_tree.root.val, 6)
        self.assertEqual(self.small_tree.root.left.val, 5)
        self.assertEqual(self.small_tree.root.right.val, 4)
        self.assertEqual(self.large_tree.root.val, 8)
        self.assertEqual(self.large_tree.root.left.val, 6)
        self.assertEqual(self.large_tree.root.right.val, 5)
        self.assertEqual(self.large_tree.root.right.right.val, 1)
        self.assertEqual(self.large_tree.root.right.left.val, 3)

    def test_min_depth_v1(self):
        self.assertEqual(self.empty_tree.min_depth_v1(), 0)
        self.assertEqual(self.small_tree.min_depth_v1(), 2)
        self.assertEqual(self.large_tree.min_depth_v1(), 2)

    def test_min_depth_v2(self):
        self.assertEqual(self.empty_tree.min_depth_v2(), 0)
        self.assertEqual(self.small_tree.min_depth_v2(), 2)
        self.assertEqual(self.large_tree.min_depth_v2(), 2)

    def test_max_depth(self):
        self.assertEqual(self.empty_tree.max_depth(), 0)
        self.assertEqual(self.small_tree.max_depth(), 2)
        self.assertEqual(self.large_tree.max_depth(), 4)

    def test_max_sum(self):
        self.assertEqual(self.empty_tree.max_sum(), 0)
        self.assertEqual(self.small_tree.max_sum(), 15)
        self.assertEqual(self.large_tree.max_sum(), 24)

    def test_max_sum_with_negative_nums(self):
        node100 = BinaryTreeNode(100)
        node8 = BinaryTreeNode(8)
        nodeNeg4 = BinaryTreeNode(-4)
        node2 = BinaryTreeNode(2, nodeNeg4)
        nodeNeg3 = BinaryTreeNode(-3, node8, node100)
        root = BinaryTreeNode(10, node2, nodeNeg3)
        tree = BinaryTree(root)

        self.assertEqual(tree.max_sum(), 109)