
class Node:
    """
    Node for the Linked_list class
    """

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_list:
    """
    Linked_list class.
    The tests are translated from the Javascript version of the this exercise
    """

    def __init__(self, head=None, tail=None, vals=[]):
        self.head = head
        self.tail = tail
        self.length = 0

        for val in vals:
            self.push(val)

    def push(self, val):
        """
        put new value at end of linked list

        >>> lst = Linked_list()
        >>> lst.push(5)
        >>> lst.length
        1
        >>> lst.head.val
        5
        >>> lst.tail.val
        5

        >>> lst.push(10)
        >>> lst.length
        2
        >>> lst.head.val
        5
        >>> lst.tail.val
        10

        >>> lst.push(15)
        >>> lst.length
        3
        >>> lst.head.val
        5
        >>> lst.tail.val
        15

        """
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def unshift(self, val):
        """
        adds new node with value val to beginning of list

        >>> lst = Linked_list()
        >>> lst.unshift(5)
        >>> lst.length
        1
        >>> lst.head.val
        5
        >>> lst.tail.val
        5

        >>> lst.unshift(10)
        >>> lst.length
        2
        >>> lst.head.val
        10
        >>> lst.tail.val
        5

        >>> lst.unshift(15)
        >>> lst.length
        3
        >>> lst.head.val
        15
        >>> lst.tail.val
        5
        """
        new_node = Node(val, self.head)
        if self.head == None:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def pop(self):
        """
        remove and return last item in list

        >>> lst = Linked_list(vals=[5, 10])
        >>> lst.pop()
        10
        >>> lst.head.val
        5
        >>> lst.tail.val
        5
        >>> lst.length
        1
        >>> lst.pop()
        5
        >>> lst.head
        >>> lst.tail
        >>> lst.length
        0

        """
        value = self.tail.val

        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            prev_node = self.head
            while prev_node.next != self.tail:
                prev_node = prev_node.next
            self.tail = prev_node
            self.tail.next = None
        self.length -= 1
        return value

    def shift(self):
        """
        removes node at head and returns value of head

        >>> lst = Linked_list(vals=[5, 10])
        >>> lst.shift()
        5
        >>> lst.head.val
        10
        >>> lst.tail.val
        10
        >>> lst.length
        1
        >>> lst.shift()
        10
        >>> lst.head
        >>> lst.tail
        >>> lst.length
        0
        """
        value = self.head.val
        if self.length == 1:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
        return value

    def get_at(self, idx):
        """
        returns value at index idx

        >>> lst = Linked_list(vals=[5, 10])
        >>> lst.get_at(0)
        5
        >>> lst.get_at(1)
        10

        """
        node = self.head
        index = 0
        while index != idx:
            node = node.next
            index += 1
        return node.val

    def set_at(self, idx, val):
        """
        set value of node at index position idx

        >>> lst = Linked_list(vals=[5, 10])
        >>> lst.set_at(0, 1)
        >>> lst.set_at(1, 2)
        >>> lst.head.val
        1
        >>> lst.head.next.val
        2
        """
        node = self.head
        index = 0
        while index != idx:
            node = node.next
            index += 1
        node.val = val

    def insert_at(self, idx, val):
        """
        insert new node at position idx with value val

        >>> lst = Linked_list(vals=[5, 10, 15, 20])
        >>> lst.insert_at(2, 12)
        >>> lst.length
        5
        >>> lst.head.val
        5
        >>> lst.head.next.val
        10
        >>> lst.head.next.next.val
        12
        >>> lst.head.next.next.next.val
        15
        >>> lst.head.next.next.next.next.val
        20
        >>> lst.insert_at(5, 25)
        >>> lst.head.next.next.next.next.next.val
        25
        >>> lst.tail.val
        25
        >>> lst2 = Linked_list()
        >>> lst2.insert_at(0, 3)
        >>> lst2.length
        1
        >>> lst2.head.val
        3
        >>> lst2.tail.val
        3

        """
        new_node = Node(val)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        elif idx == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            curr_node = self.head
            index = 0
            while index < idx - 1:
                curr_node = curr_node.next
                index += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
            if self.tail == curr_node:
                self.tail = new_node
        self.length += 1

    def remove_at(self, idx):
        """
        remove node at position idx and return its value
        >>> lst = Linked_list(vals=[5, 10, 15])
        >>> lst.remove_at(1)
        10
        >>> lst.head.val
        5
        >>> lst.head.next.val
        15
        >>> lst.tail.val
        15
        >>> lst.remove_at(1)
        15
        >>> lst.length
        1
        >>> lst.head.val
        5
        >>> lst.tail.val
        5
        >>> lst.remove_at(0)
        5
        >>> lst.length
        0
        >>> lst.head
        >>> lst.tail
        """
        node = self.head
        index = 0
        value = 0
        if idx == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            value = node.val
        else:
            while index < idx-1:
                node = node.next
                index += 1
            value = node.next.val
            if idx == self.length - 1:
                self.tail = node
            node.next = node.next.next
        self.length -= 1
        return value

    def list_average(self):
        """
        calculates and returns the avarage of all the values in the linked list

        >>> lst = Linked_list(vals=[1,2,3,4])
        >>> lst.list_average()
        2.5
        >>> lst2 = Linked_list()
        >>> lst2.list_average()
        0
        """
        if self.length == 0:
            return 0
        sum = 0
        curr_node = self.head
        while curr_node:
            sum += curr_node.val
            curr_node = curr_node.next
        return sum/self.length

    def traverse(self):
        """
        prints each item of list in order (from lecture video)
        """
        currentNode = self.head
        while(currentNode):
            print(currentNode.val)
            currentNode = currentNode.next

    def find(self, val):
        """
        searches for val in list, returns True if in list, otherwise False
        (from lecture video)
        """
        currentNode = self.head
        while(currentNode):
            if currentNode.val == val:
                return True
            currentNode = currentNode.next
        return False
