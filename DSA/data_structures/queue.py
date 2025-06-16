"""
Queue Implementation

A queue is a linear data structure that follows the First In First Out (FIFO) principle.
Elements are added at the rear and removed from the front of the queue.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity: O(n) where n is the number of elements in the queue
"""

from typing import TypeVar, Generic
import unittest

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self):
        """Initialize an empty queue."""
        self._items: list[T] = []
    
    def enqueue(self, item: T) -> None:
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue
        """
        raise NotImplementedError("Queue implementation not completed")
    
    def dequeue(self) -> T:
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        raise NotImplementedError("Queue implementation not completed")
    
    def peek(self) -> T:
        """
        Return the front item from the queue without removing it.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        raise NotImplementedError("Queue implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise
        """
        raise NotImplementedError("Queue implementation not completed")
    
    def size(self) -> int:
        """
        Return the number of items in the queue.
        
        Returns:
            The number of items in the queue
        """
        raise NotImplementedError("Queue implementation not completed")


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue[int]()
    
    def test_empty_queue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()
    
    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())
    
    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 1)
    
    def test_generic_type(self):
        string_queue = Queue[str]()
        string_queue.enqueue("hello")
        string_queue.enqueue("world")
        self.assertEqual(string_queue.dequeue(), "hello")
        self.assertEqual(string_queue.dequeue(), "world")


if __name__ == '__main__':
    unittest.main() 