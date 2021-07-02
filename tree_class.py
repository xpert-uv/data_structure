"""
general tree class
"""

class TreeNode:
    """
    Node for tree class
    """
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Tree:
    """
    General tree class
    """
    def __init__(self, root=None):
        self.root = root

    def sum_values(self):
        """
        return the sum of the values of all the nodes in the tree
        """
        if not self.root:
            return 0

        def recursive_sum(node):
            if len(node.children) == 0:
                return node.val

            return node.val + sum([recursive_sum(child) for child in node.children])
        return recursive_sum(self.root)

    def count_evens(self):
        """
        return the number of evenly-values nodes in the given tree
        """
        if not self.root:
            return 0

        def recursive_count(node):
            if len(node.children) == 0:
                return (node.val + 1) % 2

            return (node.val + 1) % 2 + sum([recursive_count(child) for child in node.children])
        return recursive_count(self.root)

    def num_greater(self, num):
        """
        return the number of nodes with a value greater than the given number num
        """
        if not self.root:
            return 0
            
        def count(val):
            return 1 if val > num else 0

        def recursive_count(node):
            if len(node.children) == 0:
                return count(node.val)

            return count(node.val) + sum([recursive_count(child) for child in node.children])

        return recursive_count(self.root)