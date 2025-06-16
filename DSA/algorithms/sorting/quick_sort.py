"""
Quick Sort Algorithm

Quick sort is a highly efficient, comparison-based, in-place sorting algorithm.
It uses a divide-and-conquer strategy to sort elements.

Time Complexity:
- Best/Average: O(n log n)
- Worst: O(n²) when array is already sorted or reverse sorted

Space Complexity:
- O(log n) for recursion stack

Characteristics:
1. In-place sorting
2. Not stable
3. Cache-friendly
4. Works well with virtual memory
"""

from typing import List, TypeVar, Callable, Optional
import unittest
import random

T = TypeVar('T')

def quick_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using quick sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> quick_sort(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Quick sort implementation not completed")

def quick_sort_in_place(arr: List[T], key: Optional[Callable[[T], any]] = None) -> None:
    """
    Sort a list in-place using quick sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> quick_sort_in_place(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("In-place quick sort implementation not completed")

def quick_select(arr: List[T], k: int, key: Optional[Callable[[T], any]] = None) -> T:
    """
    Find the k-th smallest element in the list using quick select algorithm.
    
    Args:
        arr: List to search in
        k: Index of element to find (0-based)
        key: Optional function to extract comparison key
        
    Returns:
        k-th smallest element
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> quick_select(arr, 3)
        3
    """
    raise NotImplementedError("Quick select implementation not completed")


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = quick_sort(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = quick_sort(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_quick_sort_in_place(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        quick_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        quick_sort_in_place(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(arr, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_quick_select(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(quick_select(arr, 0), 1)  # 1st smallest
        self.assertEqual(quick_select(arr, 1), 1)  # 2nd smallest
        self.assertEqual(quick_select(arr, 2), 2)  # 3rd smallest
        self.assertEqual(quick_select(arr, 3), 3)  # 4th smallest
        self.assertEqual(quick_select(arr, 4), 4)  # 5th smallest
        self.assertEqual(quick_select(arr, 5), 5)  # 6th smallest
        self.assertEqual(quick_select(arr, 6), 6)  # 7th smallest
        self.assertEqual(quick_select(arr, 7), 9)  # 8th smallest
    
    def test_empty_list(self):
        arr = []
        result = quick_sort(arr)
        self.assertEqual(result, [])
        
        arr = []
        quick_sort_in_place(arr)
        self.assertEqual(arr, [])
        
        with self.assertRaises(IndexError):
            quick_select(arr, 0)
    
    def test_single_element(self):
        arr = [1]
        result = quick_sort(arr)
        self.assertEqual(result, [1])
        
        arr = [1]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1])
        
        self.assertEqual(quick_select(arr, 0), 1)
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [1, 2, 3, 4, 5]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [5, 4, 3, 2, 1]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        result = quick_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [-5, -4, -3, -2, 1, 1, 6, 9])
    
    def test_floating_point(self):
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        result = quick_sort(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [0.58, 1.41, 1.73, 2.71, 3.14])
    
    def test_large_random_array(self):
        arr = list(range(1000))
        random.shuffle(arr)
        result = quick_sort(arr)
        self.assertEqual(result, list(range(1000)))
        
        arr = list(range(1000))
        random.shuffle(arr)
        quick_sort_in_place(arr)
        self.assertEqual(arr, list(range(1000)))


if __name__ == '__main__':
    unittest.main() 