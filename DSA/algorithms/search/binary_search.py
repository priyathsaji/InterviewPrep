"""
Binary Search Algorithm

Binary search is an efficient algorithm for finding an element in a sorted array.
It works by repeatedly dividing the search interval in half.

Time Complexity:
- Best/Average/Worst: O(log n)

Space Complexity:
- Iterative: O(1)
- Recursive: O(log n) for recursion stack

Characteristics:
1. Requires sorted array
2. Efficient for large datasets
3. Can be implemented iteratively or recursively
4. Can be modified for various search conditions
"""

from typing import List, TypeVar, Callable, Optional, Tuple
import unittest

T = TypeVar('T')

def binary_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using binary search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> binary_search(arr, 5)
        4
    """
    raise NotImplementedError("Binary search implementation not completed")

def binary_search_recursive(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using recursive binary search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> binary_search_recursive(arr, 5)
        4
    """
    raise NotImplementedError("Recursive binary search implementation not completed")

def binary_search_leftmost(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the leftmost index of target in sorted array using binary search.
    If target appears multiple times, returns the first occurrence.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Leftmost index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> binary_search_leftmost(arr, 2)
        1
    """
    raise NotImplementedError("Leftmost binary search implementation not completed")

def binary_search_rightmost(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the rightmost index of target in sorted array using binary search.
    If target appears multiple times, returns the last occurrence.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Rightmost index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> binary_search_rightmost(arr, 2)
        3
    """
    raise NotImplementedError("Rightmost binary search implementation not completed")

def binary_search_range(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> Tuple[int, int]:
    """
    Find the range of indices where target appears in sorted array.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Tuple of (leftmost_index, rightmost_index) if found, (-1, -1) if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> binary_search_range(arr, 2)
        (1, 3)
    """
    raise NotImplementedError("Binary search range implementation not completed")


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 5), 4)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 8)
        self.assertEqual(binary_search(arr, 10), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(binary_search(arr, 'cherry'), 2)
        self.assertEqual(binary_search(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(binary_search(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_binary_search_recursive(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search_recursive(arr, 5), 4)
        self.assertEqual(binary_search_recursive(arr, 1), 0)
        self.assertEqual(binary_search_recursive(arr, 9), 8)
        self.assertEqual(binary_search_recursive(arr, 10), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(binary_search_recursive(arr, 'cherry'), 2)
        self.assertEqual(binary_search_recursive(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(binary_search_recursive(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_binary_search_leftmost(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(binary_search_leftmost(arr, 2), 1)
        self.assertEqual(binary_search_leftmost(arr, 1), 0)
        self.assertEqual(binary_search_leftmost(arr, 5), 6)
        self.assertEqual(binary_search_leftmost(arr, 6), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        self.assertEqual(binary_search_leftmost(arr, 'banana'), 1)
        self.assertEqual(binary_search_leftmost(arr, 'grape'), -1)
    
    def test_binary_search_rightmost(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(binary_search_rightmost(arr, 2), 3)
        self.assertEqual(binary_search_rightmost(arr, 1), 0)
        self.assertEqual(binary_search_rightmost(arr, 5), 6)
        self.assertEqual(binary_search_rightmost(arr, 6), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        self.assertEqual(binary_search_rightmost(arr, 'banana'), 2)
        self.assertEqual(binary_search_rightmost(arr, 'grape'), -1)
    
    def test_binary_search_range(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(binary_search_range(arr, 2), (1, 3))
        self.assertEqual(binary_search_range(arr, 1), (0, 0))
        self.assertEqual(binary_search_range(arr, 5), (6, 6))
        self.assertEqual(binary_search_range(arr, 6), (-1, -1))
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        self.assertEqual(binary_search_range(arr, 'banana'), (1, 2))
        self.assertEqual(binary_search_range(arr, 'grape'), (-1, -1))
    
    def test_empty_list(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)
        self.assertEqual(binary_search_recursive(arr, 1), -1)
        self.assertEqual(binary_search_leftmost(arr, 1), -1)
        self.assertEqual(binary_search_rightmost(arr, 1), -1)
        self.assertEqual(binary_search_range(arr, 1), (-1, -1))
    
    def test_single_element(self):
        arr = [1]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search_recursive(arr, 1), 0)
        self.assertEqual(binary_search_leftmost(arr, 1), 0)
        self.assertEqual(binary_search_rightmost(arr, 1), 0)
        self.assertEqual(binary_search_range(arr, 1), (0, 0))
        
        self.assertEqual(binary_search(arr, 2), -1)
        self.assertEqual(binary_search_recursive(arr, 2), -1)
        self.assertEqual(binary_search_leftmost(arr, 2), -1)
        self.assertEqual(binary_search_rightmost(arr, 2), -1)
        self.assertEqual(binary_search_range(arr, 2), (-1, -1))
    
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
        self.assertEqual(binary_search_leftmost(arr, 2), 1)
        self.assertEqual(binary_search_rightmost(arr, 2), 3)
        self.assertEqual(binary_search_range(arr, 2), (1, 3))
        
        self.assertEqual(binary_search_leftmost(arr, 3), 4)
        self.assertEqual(binary_search_rightmost(arr, 3), 5)
        self.assertEqual(binary_search_range(arr, 3), (4, 5))
        
        self.assertEqual(binary_search_leftmost(arr, 5), 7)
        self.assertEqual(binary_search_rightmost(arr, 5), 9)
        self.assertEqual(binary_search_range(arr, 5), (7, 9))
    
    def test_negative_numbers(self):
        arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, -3), 2)
        self.assertEqual(binary_search(arr, 0), 5)
        self.assertEqual(binary_search(arr, 3), 8)
        self.assertEqual(binary_search(arr, 6), -1)
    
    def test_floating_point(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(binary_search(arr, 0.3), 2)
        self.assertEqual(binary_search(arr, 0.6), -1)


if __name__ == '__main__':
    unittest.main() 