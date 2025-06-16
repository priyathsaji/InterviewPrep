"""
Interpolation Search Algorithm

Interpolation search is an improvement over binary search for uniformly distributed
sorted arrays. It uses position formula to estimate the position of the target value.

Time Complexity:
- Best: O(1) when element is at first position
- Average: O(log log n) for uniformly distributed arrays
- Worst: O(n) for non-uniformly distributed arrays

Space Complexity:
- O(1) for both iterative and recursive implementations

Characteristics:
1. Works only on sorted arrays
2. More efficient than binary search for uniformly distributed arrays
3. Less efficient than binary search for non-uniformly distributed arrays
4. Requires numerical values for position calculation
"""

from typing import List, TypeVar, Callable, Optional
import unittest

T = TypeVar('T')

def interpolation_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using interpolation search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> interpolation_search(arr, 5)
        4
    """
    raise NotImplementedError("Interpolation search implementation not completed")

def interpolation_search_recursive(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using recursive interpolation search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> interpolation_search_recursive(arr, 5)
        4
    """
    raise NotImplementedError("Recursive interpolation search implementation not completed")

def interpolation_search_range(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> tuple[int, int]:
    """
    Find the range of indices where target appears in sorted array using interpolation search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Tuple of (leftmost_index, rightmost_index) if found, (-1, -1) if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> interpolation_search_range(arr, 2)
        (1, 3)
    """
    raise NotImplementedError("Interpolation search range implementation not completed")


class TestInterpolationSearch(unittest.TestCase):
    def test_interpolation_search(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(interpolation_search(arr, 5), 4)
        self.assertEqual(interpolation_search(arr, 1), 0)
        self.assertEqual(interpolation_search(arr, 9), 8)
        self.assertEqual(interpolation_search(arr, 10), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(interpolation_search(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_interpolation_search_recursive(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(interpolation_search_recursive(arr, 5), 4)
        self.assertEqual(interpolation_search_recursive(arr, 1), 0)
        self.assertEqual(interpolation_search_recursive(arr, 9), 8)
        self.assertEqual(interpolation_search_recursive(arr, 10), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(interpolation_search_recursive(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_interpolation_search_range(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(interpolation_search_range(arr, 2), (1, 3))
        self.assertEqual(interpolation_search_range(arr, 1), (0, 0))
        self.assertEqual(interpolation_search_range(arr, 5), (6, 6))
        self.assertEqual(interpolation_search_range(arr, 6), (-1, -1))
    
    def test_empty_list(self):
        arr = []
        self.assertEqual(interpolation_search(arr, 1), -1)
        self.assertEqual(interpolation_search_recursive(arr, 1), -1)
        self.assertEqual(interpolation_search_range(arr, 1), (-1, -1))
    
    def test_single_element(self):
        arr = [1]
        self.assertEqual(interpolation_search(arr, 1), 0)
        self.assertEqual(interpolation_search_recursive(arr, 1), 0)
        self.assertEqual(interpolation_search_range(arr, 1), (0, 0))
        
        self.assertEqual(interpolation_search(arr, 2), -1)
        self.assertEqual(interpolation_search_recursive(arr, 2), -1)
        self.assertEqual(interpolation_search_range(arr, 2), (-1, -1))
    
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
        self.assertEqual(interpolation_search_range(arr, 2), (1, 3))
        self.assertEqual(interpolation_search_range(arr, 3), (4, 5))
        self.assertEqual(interpolation_search_range(arr, 5), (7, 9))
    
    def test_negative_numbers(self):
        arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(interpolation_search(arr, -3), 2)
        self.assertEqual(interpolation_search(arr, 0), 5)
        self.assertEqual(interpolation_search(arr, 3), 8)
        self.assertEqual(interpolation_search(arr, 6), -1)
    
    def test_floating_point(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(interpolation_search(arr, 0.3), 2)
        self.assertEqual(interpolation_search(arr, 0.6), -1)
    
    def test_uniform_distribution(self):
        # Test with uniformly distributed array
        arr = list(range(0, 1000, 10))
        self.assertEqual(interpolation_search(arr, 500), 50)
        self.assertEqual(interpolation_search(arr, 0), 0)
        self.assertEqual(interpolation_search(arr, 990), 99)
        self.assertEqual(interpolation_search(arr, 1000), -1)
    
    def test_non_uniform_distribution(self):
        # Test with non-uniformly distributed array
        arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        self.assertEqual(interpolation_search(arr, 32), 5)
        self.assertEqual(interpolation_search(arr, 1), 0)
        self.assertEqual(interpolation_search(arr, 512), 9)
        self.assertEqual(interpolation_search(arr, 1000), -1)


if __name__ == '__main__':
    unittest.main() 