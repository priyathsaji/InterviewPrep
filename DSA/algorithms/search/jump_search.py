"""
Jump Search Algorithm

Jump search is a search algorithm for sorted arrays that works by jumping ahead
by fixed steps and then performing a linear search in the identified block.

Time Complexity:
- Best: O(1) when element is at first position
- Average: O(√n) when element is in middle
- Worst: O(√n) when element is at last position or not found

Space Complexity:
- O(1) for both iterative and recursive implementations

Characteristics:
1. Works only on sorted arrays
2. More efficient than linear search
3. Less efficient than binary search
4. Optimal jump size is √n
"""

from typing import List, TypeVar, Callable, Optional
import unittest
import math

T = TypeVar('T')

def jump_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using jump search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> jump_search(arr, 5)
        4
    """
    raise NotImplementedError("Jump search implementation not completed")

def jump_search_optimized(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in sorted array using optimized jump search.
    Uses binary search within the identified block.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> jump_search_optimized(arr, 5)
        4
    """
    raise NotImplementedError("Optimized jump search implementation not completed")

def jump_search_range(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> tuple[int, int]:
    """
    Find the range of indices where target appears in sorted array using jump search.
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Tuple of (leftmost_index, rightmost_index) if found, (-1, -1) if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3, 4, 5]
        >>> jump_search_range(arr, 2)
        (1, 3)
    """
    raise NotImplementedError("Jump search range implementation not completed")


class TestJumpSearch(unittest.TestCase):
    def test_jump_search(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(jump_search(arr, 5), 4)
        self.assertEqual(jump_search(arr, 1), 0)
        self.assertEqual(jump_search(arr, 9), 8)
        self.assertEqual(jump_search(arr, 10), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(jump_search(arr, 'cherry'), 2)
        self.assertEqual(jump_search(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(jump_search(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_jump_search_optimized(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(jump_search_optimized(arr, 5), 4)
        self.assertEqual(jump_search_optimized(arr, 1), 0)
        self.assertEqual(jump_search_optimized(arr, 9), 8)
        self.assertEqual(jump_search_optimized(arr, 10), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(jump_search_optimized(arr, 'cherry'), 2)
        self.assertEqual(jump_search_optimized(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(jump_search_optimized(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_jump_search_range(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3, 4, 5]
        self.assertEqual(jump_search_range(arr, 2), (1, 3))
        self.assertEqual(jump_search_range(arr, 1), (0, 0))
        self.assertEqual(jump_search_range(arr, 5), (6, 6))
        self.assertEqual(jump_search_range(arr, 6), (-1, -1))
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        self.assertEqual(jump_search_range(arr, 'banana'), (1, 2))
        self.assertEqual(jump_search_range(arr, 'grape'), (-1, -1))
    
    def test_empty_list(self):
        arr = []
        self.assertEqual(jump_search(arr, 1), -1)
        self.assertEqual(jump_search_optimized(arr, 1), -1)
        self.assertEqual(jump_search_range(arr, 1), (-1, -1))
    
    def test_single_element(self):
        arr = [1]
        self.assertEqual(jump_search(arr, 1), 0)
        self.assertEqual(jump_search_optimized(arr, 1), 0)
        self.assertEqual(jump_search_range(arr, 1), (0, 0))
        
        self.assertEqual(jump_search(arr, 2), -1)
        self.assertEqual(jump_search_optimized(arr, 2), -1)
        self.assertEqual(jump_search_range(arr, 2), (-1, -1))
    
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
        self.assertEqual(jump_search_range(arr, 2), (1, 3))
        self.assertEqual(jump_search_range(arr, 3), (4, 5))
        self.assertEqual(jump_search_range(arr, 5), (7, 9))
    
    def test_negative_numbers(self):
        arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(jump_search(arr, -3), 2)
        self.assertEqual(jump_search(arr, 0), 5)
        self.assertEqual(jump_search(arr, 3), 8)
        self.assertEqual(jump_search(arr, 6), -1)
    
    def test_floating_point(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(jump_search(arr, 0.3), 2)
        self.assertEqual(jump_search(arr, 0.6), -1)
    
    def test_large_array(self):
        arr = list(range(1000))
        self.assertEqual(jump_search(arr, 500), 500)
        self.assertEqual(jump_search(arr, 0), 0)
        self.assertEqual(jump_search(arr, 999), 999)
        self.assertEqual(jump_search(arr, 1000), -1)


if __name__ == '__main__':
    unittest.main() 