"""
Exponential Search Algorithm

Exponential search is a search algorithm for sorted arrays that works by finding
the range where the target element is present and then performing binary search
within that range.

Time Complexity:
- Best: O(1) when element is at first position
- Average: O(log n) when element is in middle
- Worst: O(log n) when element is at last position or not found

Space Complexity:
- O(1) for both iterative and recursive implementations

Characteristics:
1. Works only on sorted arrays
2. More efficient than binary search when target is near the beginning
3. Combines exponential and binary search
4. Useful for unbounded searches
"""

from typing import List, TypeVar, Callable, Optional
import unittest

T = TypeVar('T')

def exponential_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using exponential search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> exponential_search(arr, 5)
        4
    """
    raise NotImplementedError("Exponential search implementation not completed")

def exponential_search_recursive(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using recursive exponential search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> exponential_search_recursive(arr, 5)
        4
    """
    raise NotImplementedError("Recursive exponential search implementation not completed")

def exponential_search_range(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> tuple[int, int]:
    """
    Find the range of indices where target appears in sorted array using exponential search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Tuple of (leftmost_index, rightmost_index) if found, (-1, -1) if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> exponential_search_range(arr, 2)
        (1, 3)
    """
    raise NotImplementedError("Exponential search range implementation not completed")


class TestExponentialSearch(unittest.TestCase):
    def test_exponential_search(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(exponential_search(arr, 5), 4)
        self.assertEqual(exponential_search(arr, 1), 0)
        self.assertEqual(exponential_search(arr, 9), 8)
        self.assertEqual(exponential_search(arr, 10), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(exponential_search(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_exponential_search_recursive(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(exponential_search_recursive(arr, 5), 4)
        self.assertEqual(exponential_search_recursive(arr, 1), 0)
        self.assertEqual(exponential_search_recursive(arr, 9), 8)
        self.assertEqual(exponential_search_recursive(arr, 10), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(exponential_search_recursive(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_exponential_search_range(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(exponential_search_range(arr, 2), (1, 3))
        self.assertEqual(exponential_search_range(arr, 1), (0, 0))
        self.assertEqual(exponential_search_range(arr, 5), (6, 6))
        self.assertEqual(exponential_search_range(arr, 6), (-1, -1))
    
    def test_empty_list(self):
        arr = []
        self.assertEqual(exponential_search(arr, 1), -1)
        self.assertEqual(exponential_search_recursive(arr, 1), -1)
        self.assertEqual(exponential_search_range(arr, 1), (-1, -1))
    
    def test_single_element(self):
        arr = [1]
        self.assertEqual(exponential_search(arr, 1), 0)
        self.assertEqual(exponential_search_recursive(arr, 1), 0)
        self.assertEqual(exponential_search_range(arr, 1), (0, 0))
        
        self.assertEqual(exponential_search(arr, 2), -1)
        self.assertEqual(exponential_search_recursive(arr, 2), -1)
        self.assertEqual(exponential_search_range(arr, 2), (-1, -1))
    
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
        self.assertEqual(exponential_search_range(arr, 2), (1, 3))
        self.assertEqual(exponential_search_range(arr, 3), (4, 5))
        self.assertEqual(exponential_search_range(arr, 5), (7, 9))
    
    def test_negative_numbers(self):
        arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(exponential_search(arr, -3), 2)
        self.assertEqual(exponential_search(arr, 0), 5)
        self.assertEqual(exponential_search(arr, 3), 8)
        self.assertEqual(exponential_search(arr, 6), -1)
    
    def test_floating_point(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(exponential_search(arr, 0.3), 2)
        self.assertEqual(exponential_search(arr, 0.6), -1)
    
    def test_large_array(self):
        arr = list(range(1000))
        self.assertEqual(exponential_search(arr, 500), 500)
        self.assertEqual(exponential_search(arr, 0), 0)
        self.assertEqual(exponential_search(arr, 999), 999)
        self.assertEqual(exponential_search(arr, 1000), -1)
    
    def test_target_near_start(self):
        # Test when target is near the beginning of the array
        arr = list(range(1000))
        self.assertEqual(exponential_search(arr, 5), 5)
        self.assertEqual(exponential_search(arr, 10), 10)
        self.assertEqual(exponential_search(arr, 20), 20)
    
    def test_target_near_end(self):
        # Test when target is near the end of the array
        arr = list(range(1000))
        self.assertEqual(exponential_search(arr, 995), 995)
        self.assertEqual(exponential_search(arr, 990), 990)
        self.assertEqual(exponential_search(arr, 980), 980)


if __name__ == '__main__':
    unittest.main() 