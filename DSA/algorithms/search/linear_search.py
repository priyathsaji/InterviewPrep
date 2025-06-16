"""
Linear Search Algorithm

Linear search is a simple algorithm that checks each element in a list sequentially
until the target element is found or the end of the list is reached.

Time Complexity:
- Best: O(1) when element is at first position
- Average: O(n/2) when element is in middle
- Worst: O(n) when element is at last position or not found

Space Complexity:
- O(1) for both iterative and recursive implementations

Characteristics:
1. Works on unsorted arrays
2. Simple to implement
3. Inefficient for large datasets
4. Can be implemented iteratively or recursively
"""

from typing import List, TypeVar, Callable, Optional
import unittest

T = TypeVar('T')

def linear_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in array using linear search.
    
    Args:
        arr: List to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5]
        >>> linear_search(arr, 3)
        2
    """
    raise NotImplementedError("Linear search implementation not completed")

def linear_search_recursive(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    Find the index of target in array using recursive linear search.
    
    Args:
        arr: List to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> arr = [1, 2, 3, 4, 5]
        >>> linear_search_recursive(arr, 3)
        2
    """
    raise NotImplementedError("Recursive linear search implementation not completed")

def linear_search_all(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> List[int]:
    """
    Find all indices of target in array using linear search.
    
    Args:
        arr: List to search in
        target: Element to find
        key: Optional function to extract comparison key
        
    Returns:
        List of indices where target is found, empty list if not found
        
    Example:
        >>> arr = [1, 2, 2, 2, 3]
        >>> linear_search_all(arr, 2)
        [1, 2, 3]
    """
    raise NotImplementedError("Linear search all implementation not completed")


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 3), 2)
        self.assertEqual(linear_search(arr, 1), 0)
        self.assertEqual(linear_search(arr, 5), 4)
        self.assertEqual(linear_search(arr, 6), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(linear_search(arr, 'cherry'), 2)
        self.assertEqual(linear_search(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(linear_search(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_linear_search_recursive(self):
        # Test with integers
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search_recursive(arr, 3), 2)
        self.assertEqual(linear_search_recursive(arr, 1), 0)
        self.assertEqual(linear_search_recursive(arr, 5), 4)
        self.assertEqual(linear_search_recursive(arr, 6), -1)
        
        # Test with strings
        arr = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(linear_search_recursive(arr, 'cherry'), 2)
        self.assertEqual(linear_search_recursive(arr, 'grape'), -1)
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (3, 'c')]
        self.assertEqual(linear_search_recursive(arr, (2, 'a'), key=lambda x: x[0]), 1)
    
    def test_linear_search_all(self):
        # Test with integers
        arr = [1, 2, 2, 2, 3]
        self.assertEqual(linear_search_all(arr, 2), [1, 2, 3])
        self.assertEqual(linear_search_all(arr, 1), [0])
        self.assertEqual(linear_search_all(arr, 3), [4])
        self.assertEqual(linear_search_all(arr, 4), [])
        
        # Test with strings
        arr = ['apple', 'banana', 'banana', 'cherry']
        self.assertEqual(linear_search_all(arr, 'banana'), [1, 2])
        self.assertEqual(linear_search_all(arr, 'grape'), [])
        
        # Test with custom key
        arr = [(1, 'b'), (2, 'a'), (2, 'c'), (3, 'd')]
        self.assertEqual(linear_search_all(arr, (2, 'a'), key=lambda x: x[0]), [1, 2])
    
    def test_empty_list(self):
        arr = []
        self.assertEqual(linear_search(arr, 1), -1)
        self.assertEqual(linear_search_recursive(arr, 1), -1)
        self.assertEqual(linear_search_all(arr, 1), [])
    
    def test_single_element(self):
        arr = [1]
        self.assertEqual(linear_search(arr, 1), 0)
        self.assertEqual(linear_search_recursive(arr, 1), 0)
        self.assertEqual(linear_search_all(arr, 1), [0])
        
        self.assertEqual(linear_search(arr, 2), -1)
        self.assertEqual(linear_search_recursive(arr, 2), -1)
        self.assertEqual(linear_search_all(arr, 2), [])
    
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
        self.assertEqual(linear_search_all(arr, 2), [1, 2, 3])
        self.assertEqual(linear_search_all(arr, 3), [4, 5])
        self.assertEqual(linear_search_all(arr, 5), [7, 8, 9])
    
    def test_negative_numbers(self):
        arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, -3), 2)
        self.assertEqual(linear_search(arr, 0), 5)
        self.assertEqual(linear_search(arr, 3), 8)
        self.assertEqual(linear_search(arr, 6), -1)
    
    def test_floating_point(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(linear_search(arr, 0.3), 2)
        self.assertEqual(linear_search(arr, 0.6), -1)


if __name__ == '__main__':
    unittest.main() 