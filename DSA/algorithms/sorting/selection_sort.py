"""
Selection Sort Algorithm

Selection sort is a simple sorting algorithm that divides the input into a sorted and an unsorted region,
and iteratively shrinks the unsorted region by extracting the smallest element and moving it to the
sorted region.

Time Complexity:
- Best/Average/Worst: O(n²)

Space Complexity:
- O(1) for in-place sorting

Characteristics:
1. In-place sorting
2. Not stable
3. Minimum number of swaps
4. Simple implementation
"""

from typing import List, TypeVar, Callable, Optional
import unittest
import random

T = TypeVar('T')

def selection_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using selection sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> selection_sort(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Selection sort implementation not completed")

def selection_sort_in_place(arr: List[T], key: Optional[Callable[[T], any]] = None) -> None:
    """
    Sort a list in-place using selection sort algorithm.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> selection_sort_in_place(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("In-place selection sort implementation not completed")

def selection_sort_stable(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    Sort a list using stable selection sort algorithm.
    Maintains relative order of equal elements.
    
    Args:
        arr: List to be sorted
        key: Optional function to extract comparison key
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> selection_sort_stable(arr)
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    raise NotImplementedError("Stable selection sort implementation not completed")


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = selection_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = selection_sort(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = selection_sort(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_selection_sort_in_place(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        selection_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        selection_sort_in_place(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(arr, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_selection_sort_stable(self):
        # Test with integers
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = selection_sort_stable(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        result = selection_sort_stable(arr)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = selection_sort_stable(arr, key=lambda x: (x[0], x[1]))
        self.assertEqual(result, [(1, 'a'), (1, 'b'), (2, 'a')])
    
    def test_empty_list(self):
        arr = []
        result = selection_sort(arr)
        self.assertEqual(result, [])
        
        arr = []
        selection_sort_in_place(arr)
        self.assertEqual(arr, [])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [])
    
    def test_single_element(self):
        arr = [1]
        result = selection_sort(arr)
        self.assertEqual(result, [1])
        
        arr = [1]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [1])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [1])
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = selection_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [1, 2, 3, 4, 5]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = selection_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        arr = [5, 4, 3, 2, 1]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = selection_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        result = selection_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        arr = [-3, 1, -4, 1, -5, 9, -2, 6]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [-5, -4, -3, -2, 1, 1, 6, 9])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [-5, -4, -3, -2, 1, 1, 6, 9])
    
    def test_floating_point(self):
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        result = selection_sort(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        selection_sort_in_place(arr)
        self.assertEqual(arr, [0.58, 1.41, 1.73, 2.71, 3.14])
        
        result = selection_sort_stable(arr)
        self.assertEqual(result, [0.58, 1.41, 1.73, 2.71, 3.14])
    
    def test_stability(self):
        # Test stability with custom key
        arr = [(1, 'b'), (2, 'a'), (1, 'a')]
        result = selection_sort_stable(arr, key=lambda x: x[0])
        self.assertEqual(result, [(1, 'b'), (1, 'a'), (2, 'a')])  # Maintains relative order of equal elements


if __name__ == '__main__':
    unittest.main() 