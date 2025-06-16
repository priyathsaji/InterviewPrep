"""
Heap Implementation

A binary heap is a complete binary tree that satisfies the heap property.
In a max heap, for any given node N, the value of N is greater than or equal to the values of its children.
In a min heap, for any given node N, the value of N is less than or equal to the values of its children.

Time Complexity:
- Insert: O(log n)
- Extract Max/Min: O(log n)
- Peek: O(1)
- Heapify: O(n)

Space Complexity: O(n) where n is the number of elements in the heap
"""

from typing import TypeVar, Generic, List, Optional
import unittest

T = TypeVar('T')

class Heap(Generic[T]):
    def __init__(self, max_heap: bool = True):
        """
        Initialize an empty heap.
        
        Args:
            max_heap: If True, implement a max heap
                     If False, implement a min heap
        """
        self._items: List[T] = []
        self._max_heap = max_heap
    
    def insert(self, item: T) -> None:
        """
        Insert an item into the heap.
        
        Args:
            item: The item to be inserted
        """
        raise NotImplementedError("Heap implementation not completed")
    
    def extract(self) -> T:
        """
        Remove and return the root element (max or min depending on heap type).
        
        Returns:
            The root element
            
        Raises:
            IndexError: If the heap is empty
        """
        raise NotImplementedError("Heap implementation not completed")
    
    def peek(self) -> T:
        """
        Return the root element without removing it.
        
        Returns:
            The root element
            
        Raises:
            IndexError: If the heap is empty
        """
        raise NotImplementedError("Heap implementation not completed")
    
    def heapify(self, items: List[T]) -> None:
        """
        Build a heap from a list of items.
        
        Args:
            items: List of items to build the heap from
        """
        raise NotImplementedError("Heap implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the heap is empty.
        
        Returns:
            True if the heap is empty, False otherwise
        """
        raise NotImplementedError("Heap implementation not completed")
    
    def size(self) -> int:
        """
        Return the number of items in the heap.
        
        Returns:
            The number of items in the heap
        """
        raise NotImplementedError("Heap implementation not completed")


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.max_heap = Heap[int](max_heap=True)
        self.min_heap = Heap[int](max_heap=False)
    
    def test_empty_heap(self):
        self.assertTrue(self.max_heap.is_empty())
        self.assertEqual(self.max_heap.size(), 0)
        with self.assertRaises(IndexError):
            self.max_heap.extract()
        with self.assertRaises(IndexError):
            self.max_heap.peek()
    
    def test_max_heap(self):
        self.max_heap.insert(3)
        self.max_heap.insert(1)
        self.max_heap.insert(4)
        self.max_heap.insert(2)
        
        self.assertEqual(self.max_heap.size(), 4)
        self.assertEqual(self.max_heap.extract(), 4)
        self.assertEqual(self.max_heap.extract(), 3)
        self.assertEqual(self.max_heap.extract(), 2)
        self.assertEqual(self.max_heap.extract(), 1)
        self.assertTrue(self.max_heap.is_empty())
    
    def test_min_heap(self):
        self.min_heap.insert(3)
        self.min_heap.insert(1)
        self.min_heap.insert(4)
        self.min_heap.insert(2)
        
        self.assertEqual(self.min_heap.size(), 4)
        self.assertEqual(self.min_heap.extract(), 1)
        self.assertEqual(self.min_heap.extract(), 2)
        self.assertEqual(self.min_heap.extract(), 3)
        self.assertEqual(self.min_heap.extract(), 4)
        self.assertTrue(self.min_heap.is_empty())
    
    def test_heapify(self):
        items = [3, 1, 4, 2]
        self.max_heap.heapify(items)
        self.assertEqual(self.max_heap.size(), 4)
        self.assertEqual(self.max_heap.extract(), 4)
        self.assertEqual(self.max_heap.extract(), 3)
        self.assertEqual(self.max_heap.extract(), 2)
        self.assertEqual(self.max_heap.extract(), 1)


if __name__ == '__main__':
    unittest.main() 