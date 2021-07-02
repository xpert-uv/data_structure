import unittest
from stack_class import Stack

class TestStackClass(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_create(self):
        self.assertEqual(self.stack.first, None)
        self.assertEqual(self.stack.last, None)
        self.assertEqual(self.stack.size, 0)

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.first.val, 10)
        self.assertEqual(self.stack.last.val, 10)
        self.assertEqual(self.stack.size, 1)
        self.stack.push(100)
        self.assertEqual(self.stack.first.val, 100)
        self.assertEqual(self.stack.last.val, 10)
        self.assertEqual(self.stack.size, 2)
        self.stack.push(1000)
        self.assertEqual(self.stack.first.val, 1000)
        self.assertEqual(self.stack.last.val, 10)
        self.assertEqual(self.stack.size, 3)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(100)
        self.stack.push(1000)
        removed = self.stack.pop()
        self.assertEqual(removed, 1000)
        self.assertEqual(self.stack.first.val, 100)
        self.assertEqual(self.stack.last.val, 10)
        self.assertEqual(self.stack.size, 2)
        self.stack.pop()
        removed = self.stack.pop()
        self.assertEqual(removed, 10)
        self.assertEqual(self.stack.size, 0)

    def test_pop_error(self):
        self.assertEqual(self.stack.size, 0)
        with self.assertRaises(AttributeError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(3)
        self.assertEqual(self.stack.is_empty(), False)
        self.stack.pop()
        self.assertEqual(self.stack.is_empty(), True)
