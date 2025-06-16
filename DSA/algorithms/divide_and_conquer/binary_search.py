"""
Binary Search Algorithm

Binary Search is a divide-and-conquer algorithm that efficiently finds the position of a target value within a sorted array.
It compares the target value to the middle element of the array and eliminates half of the remaining elements in each step.

Time Complexity:
- Best: O(1) when the target is at the middle
- Average: O(log n) where n is the number of elements
- Worst: O(log n)

Space Complexity:
- Iterative: O(1)
- Recursive: O(log n) for recursion stack

Characteristics:
1. Requires sorted array
2. Very efficient for large datasets
3. Can be implemented iteratively or recursively
4. Works with any comparable data type
5. Can be modified to find first/last occurrence
"""

from typing import List, TypeVar, Optional, Tuple, Union
import unittest

T = TypeVar('T')

def binary_search(arr: List[T], target: T, key: Optional[callable] = None) -> Optional[int]:
    """
    Find the index of a target value in a sorted array using binary search.
    
    Args:
        arr: Sorted list of elements
        target: Value to find
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the target value if found, None otherwise
        
    Example:
        >>> arr = [1, 3, 5, 7, 9, 11]
        >>> binary_search(arr, 7)
        3
        >>> binary_search(arr, 6)
        None
    """
    raise NotImplementedError("Binary search implementation is not provided")

def binary_search_recursive(arr: List[T], target: T, key: Optional[callable] = None) -> Optional[int]:
    """
    Find the index of a target value in a sorted array using recursive binary search.
    
    Args:
        arr: Sorted list of elements
        target: Value to find
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the target value if found, None otherwise
        
    Example:
        >>> arr = [1, 3, 5, 7, 9, 11]
        >>> binary_search_recursive(arr, 7)
        3
        >>> binary_search_recursive(arr, 6)
        None
    """
    raise NotImplementedError("Recursive binary search implementation is not provided")

def find_first_occurrence(arr: List[T], target: T, key: Optional[callable] = None) -> Optional[int]:
    """
    Find the index of the first occurrence of a target value in a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Value to find
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the first occurrence if found, None otherwise
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4]
        >>> find_first_occurrence(arr, 2)
        1
    """
    raise NotImplementedError("First occurrence binary search implementation is not provided")

def find_last_occurrence(arr: List[T], target: T, key: Optional[callable] = None) -> Optional[int]:
    """
    Find the index of the last occurrence of a target value in a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Value to find
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the last occurrence if found, None otherwise
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4]
        >>> find_last_occurrence(arr, 2)
        3
    """
    raise NotImplementedError("Last occurrence binary search implementation is not provided")

def find_closest_element(arr: List[T], target: T, key: Optional[callable] = None) -> Optional[int]:
    """
    Find the index of the element closest to the target value in a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Value to find closest to
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the closest element
        
    Example:
        >>> arr = [1, 3, 5, 7, 9]
        >>> find_closest_element(arr, 6)
        3
    """
    raise NotImplementedError("Closest element binary search implementation is not provided")


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        # Test with integers
        arr = [1, 3, 5, 7, 9, 11]
        with self.assertRaises(NotImplementedError):
            binary_search(arr, 7)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        with self.assertRaises(NotImplementedError):
            binary_search(arr, 'cherry')
        
        # Test with custom key
        arr = [('apple', 1), ('banana', 2), ('cherry', 3)]
        with self.assertRaises(NotImplementedError):
            binary_search(arr, ('banana', 2), key=lambda x: x[1])
    
    def test_binary_search_recursive(self):
        # Test with integers
        arr = [1, 3, 5, 7, 9, 11]
        with self.assertRaises(NotImplementedError):
            binary_search_recursive(arr, 7)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        with self.assertRaises(NotImplementedError):
            binary_search_recursive(arr, 'cherry')
    
    def test_find_first_occurrence(self):
        # Test with duplicates
        arr = [1, 2, 2, 2, 3, 4]
        with self.assertRaises(NotImplementedError):
            find_first_occurrence(arr, 2)
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        with self.assertRaises(NotImplementedError):
            find_first_occurrence(arr, 'banana')
    
    def test_find_last_occurrence(self):
        # Test with duplicates
        arr = [1, 2, 2, 2, 3, 4]
        with self.assertRaises(NotImplementedError):
            find_last_occurrence(arr, 2)
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        with self.assertRaises(NotImplementedError):
            find_last_occurrence(arr, 'banana')
    
    def test_find_closest_element(self):
        # Test with integers
        arr = [1, 3, 5, 7, 9]
        with self.assertRaises(NotImplementedError):
            find_closest_element(arr, 6)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        with self.assertRaises(NotImplementedError):
            find_closest_element(arr, 'carrot')


if __name__ == '__main__':
    unittest.main() 