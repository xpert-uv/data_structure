import unittest
from queue_class import Queue

class TestQueueClass(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_create(self):
        self.assertEqual(self.queue.first, None)
        self.assertEqual(self.queue.last, None)
        self.assertEqual(self.queue.size, 0)

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.first.val, 10)
        self.assertEqual(self.queue.last.val, 10)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(100)
        self.assertEqual(self.queue.first.val, 10)
        self.assertEqual(self.queue.last.val, 100)
        self.assertEqual(self.queue.size, 2)
        self.queue.enqueue(1000)
        self.assertEqual(self.queue.first.val, 10)
        self.assertEqual(self.queue.last.val, 1000)
        self.assertEqual(self.queue.size, 3)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(100)
        self.queue.enqueue(1000)
        removed = self.queue.dequeue()
        self.assertEqual(removed, 10)
        self.assertEqual(self.queue.first.val, 100)
        self.assertEqual(self.queue.last.val, 1000)
        self.assertEqual(self.queue.size, 2)
        self.queue.dequeue()
        removed = self.queue.dequeue()
        self.assertEqual(removed, 1000)
        self.assertEqual(self.queue.size, 0)

    def test_dequeue_error(self):
        self.assertEqual(self.queue.size, 0)
        with self.assertRaises(AttributeError):
            self.queue.dequeue()

    def test_peek(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 3)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.peek(), 3)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.is_empty(), False)
        self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)
