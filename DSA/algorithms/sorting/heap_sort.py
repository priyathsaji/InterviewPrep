"""
Heap Sort Algorithm

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure.
It divides the input into a sorted and an unsorted region, and iteratively shrinks the
unsorted region by extracting the largest element and moving it to the sorted region.

Time Complexity:
- Best/Average/Worst: O(n log n)

Space Complexity:
- O(1) for in-place sorting

Characteristics:
1. In-place sorting
2. Not stable
3. Guaranteed O(n log n) performance
4. Good for external sorting
"""

from typing import List, TypeVar, Callable, Optional
import unittest
import random

T = TypeVar('T')

def heap_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using heap sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> heap_sort(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Heap sort implementation not completed")

def heap_sort_in_place(arr: List[T], key: Optional[Callable[[T], any]] = None) -> None:
    """
    Sort a list in-place using heap sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> heap_sort_in_place(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("In-place heap sort implementation not completed")

def heapify(arr: List[T], n: int, i: int, key: Optional[Callable[[T], any]] = None) -> None:
    """
    Heapify subtree rooted at index i.
    
    Args:
        arr: List to heapify
        n: Size of heap
        i: Index of root node
        key: Optional function to extract comparison key
    """
    raise NotImplementedError("Heapify implementation not completed")


class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = heap_sort(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = heap_sort(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_heap_sort_in_place(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        heap_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        heap_sort_in_place(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(arr, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_empty_list(self):
        arr = []
        result = heap_sort(arr)
        self.assertEqual(result, [])
        
        arr = []
        heap_sort_in_place(arr)
        self.assertEqual(arr, [])
    
    def test_single_element(self):
        arr = [1]
        result = heap_sort(arr)
        self.assertEqual(result, [1])
        
        arr = [1]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [1])
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [1, 2, 3, 4, 5]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [5, 4, 3, 2, 1]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        result = heap_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [-5, -4, -3, -2, 1, 1, 6, 9])
    
    def test_floating_point(self):
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        result = heap_sort(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        heap_sort_in_place(arr)
        self.assertEqual(arr, [0.58, 1.41, 1.73, 2.71, 3.14])
    
    def test_large_random_array(self):
        arr = list(range(1000))
        random.shuffle(arr)
        result = heap_sort(arr)
        self.assertEqual(result, list(range(1000)))
        
        arr = list(range(1000))
        random.shuffle(arr)
        heap_sort_in_place(arr)
        self.assertEqual(arr, list(range(1000)))


if __name__ == '__main__':
    unittest.main() 