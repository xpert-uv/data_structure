class Node:
    """
    Node for the Queue class
    """
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    """
    Queue class
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        """
        put value at back of queue
        """
        new_node = Node(val)
        if self.size == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.size += 1

    def dequeue(self):
        """
        remove and return value at head of queue
        """
        value = self.first.val
        if self.size == 1:
            self.first = None
        else:
            self.first = self.first.next
        self.size -= 1
        return value

    def peek(self):
        """
        return value at head of queue
        """
        return self.first.val

    def is_empty(self):
        """
        return true if queue is empty
        """
        return self.size == 0
