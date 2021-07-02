"""
binary tree class
"""

class BinaryTreeNode:
    """
    Node for binary tree class
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    """
    Binary tree class
    """
    def __init__(self, root=None):
        self.root = root

    def min_depth_v1(self):
        """
        returns the minimum depth of the tree: the shortest number of nodes from root to a leaf
        """
        if self.root == None:
            return 0

        def recursive_count(node):
            if node.right == None and node.left == None:
                return 1

            if node.right == None:
                return 1 + recursive_count(node.left)

            if node.left == None:
                return 1 + recursive_count(node.right)

            return 1 + min(recursive_count(node.left), recursive_count(node.right))

        return recursive_count(self.root)

    def min_depth_v2(self):
        """
        returns the minimum depth of the tree: the shortest number of nodes from root to a leaf
        this version avoids checking siblings of leaf nodes
        """

        def is_leaf(node):
            return node.right == None and node.left == None

        def recursive_count(node):
            if is_leaf(node.right) or is_leaf(node.left):
                return 2

            if node.right == None:
                return 1 + recursive_count(node.left)

            if node.left == None:
                return 1 + recursive_count(node.right)

            return 1 + min(recursive_count(node.left), recursive_count(node.right))

        if self.root == None:
            return 0

        if is_leaf(self.root):
            return 1

        return recursive_count(self.root)

    def max_depth(self):
        """
        returns the maximum depth of the tree: the highest number of nodes from root to a leaf
        """
        if self.root == None:
            return 0

        def recursive_count(node):
            if node.right == None and node.left == None:
                return 1

            if node.right == None:
                return 1 + recursive_count(node.left)

            if node.left == None:
                return 1 + recursive_count(node.right)

            return 1 + max(recursive_count(node.left), recursive_count(node.right))

        return recursive_count(self.root)

    def max_sum(self):
        """
        returns the maximum sum of any path in the tree
        """

        def is_leaf(node):
            return node.right == None and node.left == None

        def recursive_max_sum(node):
            if is_leaf(node):
                return (node.val, node.val)

            if node.right == None or node.left == None:
                if node.right == None:
                    (child_max, desc_max) = recursive_max_sum(node.left)

                if node.left == None:
                    (child_max, desc_max) = recursive_max_sum(node.right)

                new_desc_max = max(desc_max, child_max, child_max + node.val, node.val)
                return (node.val + max(child_max, 0), new_desc_max)

            (child_max_left, desc_max_left) = recursive_max_sum(node.left)
            (child_max_right, desc_max_right) = recursive_max_sum(node.right)
            
            node_max = node.val + max(child_max_left, child_max_right, 0)
            desc_max = max(node_max, child_max_left, child_max_right, 
                            desc_max_left, desc_max_right, 
                            child_max_right + child_max_left + node.val)
            return (node_max, desc_max)

        if self.root == None:
            return 0

        return max(recursive_max_sum(self.root))
