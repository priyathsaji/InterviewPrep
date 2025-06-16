"""
Merge Sort Implementation

Merge sort is a divide-and-conquer algorithm that recursively breaks down a problem
into two or more sub-problems of the same or related type, until these become simple
enough to be solved directly.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Space Complexity: O(n) for the temporary array used in merging

Stability: Stable
"""

from typing import List, TypeVar, Generic
import unittest

T = TypeVar('T')

def merge_sort(arr: List[T]) -> List[T]:
    """
    Sort a list using the merge sort algorithm.
    
    Args:
        arr: The list to be sorted
        
    Returns:
        A new sorted list
        
    Examples:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        >>> merge_sort([])
        []
        >>> merge_sort([1])
        [1]
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left: List[T], right: List[T]) -> List[T]:
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        A new sorted list containing all elements from both input lists
    """
    result = []
    i = j = 0
    
    # Compare elements from both lists and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left list
    result.extend(left[i:])
    
    # Add remaining elements from right list
    result.extend(right[j:])
    
    return result


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])
    
    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(merge_sort(arr), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [-5, 3, -1, 0, 7, -9, 2]
        self.assertEqual(merge_sort(arr), [-9, -5, -1, 0, 2, 3, 7])
    
    def test_floating_point_numbers(self):
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        self.assertEqual(merge_sort(arr), [0.58, 1.41, 1.73, 2.71, 3.14])
    
    def test_strings(self):
        arr = ["banana", "apple", "cherry", "date"]
        self.assertEqual(merge_sort(arr), ["apple", "banana", "cherry", "date"])
    
    def test_stability(self):
        # Test stability by sorting a list of tuples
        arr = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
        sorted_arr = merge_sort(arr)
        # Check that the relative order of elements with equal keys is preserved
        self.assertEqual(sorted_arr, [(1, 'a'), (1, 'c'), (2, 'b'), (3, 'd')])


if __name__ == '__main__':
    unittest.main() 