import unittest
from binary_search_tree import BinarySearchTree, Node

class TestBinaryTreeClass(unittest.TestCase):
    def test_create(self):
        self.empty_tree = BinarySearchTree()
        self.assertEqual(self.empty_tree.root, None)

    def test_insert_iterative(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15)
        self.assertEqual(self.bst.root.val, 15)
        self.assertEqual(self.bst.root.left, None)
        self.assertEqual(self.bst.root.right, None)
        self.bst.insert(20).insert(10).insert(12)
        self.assertEqual(self.bst.root.left.val, 10)
        self.assertEqual(self.bst.root.right.val, 20)
        self.assertEqual(self.bst.root.left.right.val, 12)

    def test_insert_recursive(self):
        self.bst = BinarySearchTree()
        self.bst.insert_recursive(15)
        self.assertEqual(self.bst.root.val, 15)
        self.assertEqual(self.bst.root.left, None)
        self.assertEqual(self.bst.root.right, None)
        self.bst.insert_recursive(20).insert_recursive(10).insert_recursive(12)
        self.assertEqual(self.bst.root.left.val, 10)
        self.assertEqual(self.bst.root.right.val, 20)
        self.assertEqual(self.bst.root.left.right.val, 12)

    def test_find_exists(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        found = self.bst.find(20)
        self.assertEqual(found.val, 20)
        self.assertEqual(found.left, None)
        self.assertEqual(found.right, None)

    def test_find_not_exists(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        found = self.bst.find(200)
        self.assertEqual(found, None)

    def test_find_recursive_exists(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        found = self.bst.find_recursive(20)
        self.assertEqual(found.val, 20)
        self.assertEqual(found.left, None)
        self.assertEqual(found.right, None)

    def test_find_recursive_not_exists(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        found = self.bst.find_recursive(200)
        self.assertEqual(found, None)

    def test_dfs_pre_order(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        self.bst.insert(1).insert(5).insert(50)
        self.assertEqual(self.bst.dfs_pre_order(), [15, 10, 1, 5, 12, 20, 50])

    def test_dfs_in_order(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        self.bst.insert(1).insert(5).insert(50)
        self.assertEqual(self.bst.dfs_in_order(), [1, 5, 10, 12, 15, 20, 50])

    def test_dfs_post_order(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        self.bst.insert(1).insert(5).insert(50)
        self.assertEqual(self.bst.dfs_post_order(), [5, 1, 12, 10, 50, 20, 15])

    def test_bfs(self):
        self.bst = BinarySearchTree()
        self.bst.insert(15).insert(20).insert(10).insert(12)
        self.bst.insert(1).insert(5).insert(50)
        self.assertEqual(self.bst.bfs(), [15, 10, 20, 1, 12, 50, 5])