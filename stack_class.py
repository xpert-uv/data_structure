class Node:
    """
    Node for the Stack class
    """
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.last = new_node
        else:
            new_node.next = self.first
        self.first = new_node
        self.size += 1

    def pop(self):
        value = self.first.val
        if self.size == 1:
            self.first = None
        else:
            self.first = self.first.next
        self.size -= 1
        return value

    def peek(self):
        """
        return value at top of stack
        """
        return self.first.val

    def is_empty(self):
        """
        return true if stack is empty
        """
        return self.size == 0
