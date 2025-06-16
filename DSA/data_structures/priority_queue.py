"""
Priority Queue Implementation

A priority queue is a data structure where each element has a priority associated with it.
Elements are served based on their priority (highest or lowest depending on implementation).

Time Complexity:
- Insert: O(log n)
- Extract Max/Min: O(log n)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity: O(n) where n is the number of elements in the priority queue
"""

from typing import TypeVar, Generic, Optional
import unittest

T = TypeVar('T')

class PriorityQueue(Generic[T]):
    def __init__(self, max_heap: bool = True):
        """
        Initialize an empty priority queue.
        
        Args:
            max_heap: If True, higher values have higher priority (max heap)
                     If False, lower values have higher priority (min heap)
        """
        self._items: list[T] = []
        self._max_heap = max_heap
    
    def insert(self, item: T) -> None:
        """
        Insert an item into the priority queue.
        
        Args:
            item: The item to be inserted
        """
        raise NotImplementedError("Priority Queue implementation not completed")
    
    def extract(self) -> T:
        """
        Remove and return the highest/lowest priority item.
        
        Returns:
            The highest/lowest priority item
            
        Raises:
            IndexError: If the priority queue is empty
        """
        raise NotImplementedError("Priority Queue implementation not completed")
    
    def peek(self) -> T:
        """
        Return the highest/lowest priority item without removing it.
        
        Returns:
            The highest/lowest priority item
            
        Raises:
            IndexError: If the priority queue is empty
        """
        raise NotImplementedError("Priority Queue implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.
        
        Returns:
            True if the priority queue is empty, False otherwise
        """
        raise NotImplementedError("Priority Queue implementation not completed")
    
    def size(self) -> int:
        """
        Return the number of items in the priority queue.
        
        Returns:
            The number of items in the priority queue
        """
        raise NotImplementedError("Priority Queue implementation not completed")


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.max_pq = PriorityQueue[int](max_heap=True)
        self.min_pq = PriorityQueue[int](max_heap=False)
    
    def test_empty_priority_queue(self):
        self.assertTrue(self.max_pq.is_empty())
        self.assertEqual(self.max_pq.size(), 0)
        with self.assertRaises(IndexError):
            self.max_pq.extract()
        with self.assertRaises(IndexError):
            self.max_pq.peek()
    
    def test_max_priority_queue(self):
        self.max_pq.insert(3)
        self.max_pq.insert(1)
        self.max_pq.insert(4)
        self.max_pq.insert(2)
        
        self.assertEqual(self.max_pq.size(), 4)
        self.assertEqual(self.max_pq.extract(), 4)
        self.assertEqual(self.max_pq.extract(), 3)
        self.assertEqual(self.max_pq.extract(), 2)
        self.assertEqual(self.max_pq.extract(), 1)
        self.assertTrue(self.max_pq.is_empty())
    
    def test_min_priority_queue(self):
        self.min_pq.insert(3)
        self.min_pq.insert(1)
        self.min_pq.insert(4)
        self.min_pq.insert(2)
        
        self.assertEqual(self.min_pq.size(), 4)
        self.assertEqual(self.min_pq.extract(), 1)
        self.assertEqual(self.min_pq.extract(), 2)
        self.assertEqual(self.min_pq.extract(), 3)
        self.assertEqual(self.min_pq.extract(), 4)
        self.assertTrue(self.min_pq.is_empty())
    
    def test_peek(self):
        self.max_pq.insert(1)
        self.max_pq.insert(2)
        self.assertEqual(self.max_pq.peek(), 2)
        self.assertEqual(self.max_pq.size(), 2)


if __name__ == '__main__':
    unittest.main() 