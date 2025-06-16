"""
Insertion Sort Algorithm

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort,
or merge sort.

Time Complexity:
- Best: O(n) when array is already sorted
- Average/Worst: O(n²)

Space Complexity:
- O(1) for in-place sorting

Characteristics:
1. In-place sorting
2. Stable
3. Adaptive (efficient for nearly sorted data)
4. Online (can sort as it receives data)
"""

from typing import List, TypeVar, Callable, Optional
import unittest
import random

T = TypeVar('T')

def insertion_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using insertion sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> insertion_sort(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Insertion sort implementation not completed")

def insertion_sort_in_place(arr: List[T], key: Optional[Callable[[T], any]] = None) -> None:
    """
    Sort a list in-place using insertion sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> insertion_sort_in_place(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("In-place insertion sort implementation not completed")

def binary_insertion_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using binary insertion sort algorithm.
    Uses binary search to find the insertion point.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> binary_insertion_sort(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Binary insertion sort implementation not completed")


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = insertion_sort(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = insertion_sort(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_insertion_sort_in_place(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        insertion_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        insertion_sort_in_place(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(arr, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_binary_insertion_sort(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = binary_insertion_sort(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = binary_insertion_sort(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_empty_list(self):
        arr = []
        result = insertion_sort(arr)
        self.assertEqual(result, [])
        
        arr = []
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [])
    
    def test_single_element(self):
        arr = [1]
        result = insertion_sort(arr)
        self.assertEqual(result, [1])
        
        arr = [1]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1])
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [1, 2, 3, 4, 5]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [5, 4, 3, 2, 1]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        result = insertion_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
    
    def test_floating_point(self):
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        result = insertion_sort(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
    
    def test_nearly_sorted(self):
        arr = [1, 2, 4, 3, 5, 6, 8, 7]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
        
        arr = [1, 2, 4, 3, 5, 6, 8, 7]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8])
        
        result = binary_insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main() 