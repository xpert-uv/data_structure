"""
binary search tree
"""

class Node:
    """
    node for binary search tree
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    # these two functions created based on video, not tested
    # def find(self, sought):
    #     current_node = self
    #     while current_node:
    #         if current_node.val == sought:
    #             return current_node
    #         elif current_node.val > sought:
    #             current_node = current_node.left
    #         else:
    #             current_node = current_node.right

    # def traverse(node):
    #     if node.left:
    #         traverse(node.left)
    #     print(node.val):
    #     if node.right:
    #         traverse(node.right)


class BinarySearchTree:
    """
    binary search tree class.
    """
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        """
        insert iteratively
        """
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self

        current_node = self.root
        while current_node:
            if val < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return self
            elif val > current_node.val:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    return self
            else:
                return self

    def insert_recursive(self, val):
        """
        insert recursively
        """
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self

        def recursive_insert(current_node):
            if val < current_node.val:
                if current_node.left == None:
                    current_node.left = new_node
                    return
                else:
                    recursive_insert(current_node.left)
            elif val > current_node.val:
                if current_node.right == None:
                    current_node.right = new_node
                    return
                else:
                    recursive_insert(current_node.right)
            else:
                return

        current_node = self.root
        recursive_insert(current_node)
        return self

    def find(self, val):
        """
        find and return node with value val if exists, iterative approach
        """
        if self.root == None:
            return

        current_node = self.root
        while current_node:
            if current_node.val == val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return

    def find_recursive(self, val):
        """
        find and return node with value val if exists, recursive approach
        """
        if self.root == None:
            return

        def recursive_find(current_node):
            if current_node == None:
                return
            if current_node.val == val:
                return current_node
            if val < current_node.val:
                return recursive_find(current_node.left)
            if val > current_node.val:
                return recursive_find(current_node.right)

        current_node = self.root
        return recursive_find(current_node)

    def dfs_pre_order(self):
        """
        depth-first search with pre-order, returns array of each node's value
        """
        arr = []

        def traverse(current_node, arr):
            if current_node == None:
                return

            arr.append(current_node.val)
            traverse(current_node.left, arr)
            traverse(current_node.right, arr)

        traverse(self.root, arr)
        return arr

    def dfs_in_order(self):
        """
        depth-first search in order, returns array of each node's value
        """
        arr = []

        def traverse(current_node, arr):
            if current_node == None:
                return

            traverse(current_node.left, arr)
            arr.append(current_node.val)
            traverse(current_node.right, arr)

        traverse(self.root, arr)
        return arr

    def dfs_post_order(self):
        """
        depth-first search with post-order, returns array of each node's value
        """
        arr = []

        def traverse(current_node, arr):
            if current_node == None:
                return

            traverse(current_node.left, arr)
            traverse(current_node.right, arr)
            arr.append(current_node.val)

        traverse(self.root, arr)
        return arr

    def bfs(self):
        """
        depth-first search with post-order, returns array of each node's value
        """
        arr = []
        queue = []

        if self.root == None:
            return

        def traverse(current_node, queue, arr):
            arr.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            if len(queue) > 0:
                next_node = queue.pop(0)
                traverse(next_node, queue, arr)


        traverse(self.root, queue, arr)
        return arr

    

