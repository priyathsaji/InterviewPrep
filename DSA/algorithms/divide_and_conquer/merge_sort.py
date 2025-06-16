"""
Merge Sort Algorithm

Merge Sort is a divide-and-conquer algorithm that recursively breaks down a problem into two or more sub-problems
of the same or related type, until these become simple enough to be solved directly.

Time Complexity:
- Best: O(n log n) where n is the number of elements
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity:
- O(n) where n is the number of elements

Characteristics:
1. Stable sorting algorithm
2. Not in-place sorting algorithm
3. Works well with linked lists
4. Guaranteed O(n log n) performance
5. Requires additional space for merging
"""

from typing import List, TypeVar, Optional
import unittest

T = TypeVar('T')

def merge_sort(arr: List[T], key: Optional[callable] = None) -> List[T]:
    """
    Sort a list using the merge sort algorithm.
    
    Args:
        arr: List of elements to be sorted
        key: Optional function to extract comparison key from elements
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> sorted_arr = merge_sort(arr)
        >>> sorted_arr == [11, 12, 22, 25, 34, 64, 90]
        True
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    
    return merge(left, right, key)

def merge(left: List[T], right: List[T], key: Optional[callable] = None) -> List[T]:
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left: First sorted list
        right: Second sorted list
        key: Optional function to extract comparison key from elements
        
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_val = key(left[i]) if key else left[i]
        right_val = key(right[j]) if key else right[j]
        
        if left_val <= right_val:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort_in_place(arr: List[T], key: Optional[callable] = None) -> None:
    """
    Sort a list in-place using the merge sort algorithm.
    
    Args:
        arr: List of elements to be sorted
        key: Optional function to extract comparison key from elements
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> merge_sort_in_place(arr)
        >>> arr == [11, 12, 22, 25, 34, 64, 90]
        True
    """
    if len(arr) <= 1:
        return
    
    temp = [None] * len(arr)
    _merge_sort_in_place(arr, 0, len(arr) - 1, temp, key)

def _merge_sort_in_place(arr: List[T], left: int, right: int, temp: List[T], key: Optional[callable] = None) -> None:
    """
    Helper function for in-place merge sort.
    
    Args:
        arr: List to be sorted
        left: Left index of current subarray
        right: Right index of current subarray
        temp: Temporary array for merging
        key: Optional function to extract comparison key from elements
    """
    if left >= right:
        return
    
    mid = (left + right) // 2
    _merge_sort_in_place(arr, left, mid, temp, key)
    _merge_sort_in_place(arr, mid + 1, right, temp, key)
    _merge_in_place(arr, left, mid, right, temp, key)

def _merge_in_place(arr: List[T], left: int, mid: int, right: int, temp: List[T], key: Optional[callable] = None) -> None:
    """
    Merge two sorted subarrays in-place.
    
    Args:
        arr: List containing the subarrays
        left: Left index of first subarray
        mid: Right index of first subarray
        right: Right index of second subarray
        temp: Temporary array for merging
        key: Optional function to extract comparison key from elements
    """
    i = left
    j = mid + 1
    k = left
    
    while i <= mid and j <= right:
        left_val = key(arr[i]) if key else arr[i]
        right_val = key(arr[j]) if key else arr[j]
        
        if left_val <= right_val:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        # Test with integers
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [('banana', 3), ('apple', 1), ('cherry', 2), ('date', 4)]
        sorted_arr = merge_sort(arr, key=lambda x: x[1])
        self.assertEqual(sorted_arr, [('apple', 1), ('cherry', 2), ('banana', 3), ('date', 4)])
        
        # Test with empty list
        arr = []
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [])
        
        # Test with single element
        arr = [1]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1])
        
        # Test with duplicate elements
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_merge_sort_in_place(self):
        # Test with integers
        arr = [64, 34, 25, 12, 22, 11, 90]
        merge_sort_in_place(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        merge_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [('banana', 3), ('apple', 1), ('cherry', 2), ('date', 4)]
        merge_sort_in_place(arr, key=lambda x: x[1])
        self.assertEqual(arr, [('apple', 1), ('cherry', 2), ('banana', 3), ('date', 4)])
        
        # Test with empty list
        arr = []
        merge_sort_in_place(arr)
        self.assertEqual(arr, [])
        
        # Test with single element
        arr = [1]
        merge_sort_in_place(arr)
        self.assertEqual(arr, [1])
        
        # Test with duplicate elements
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        merge_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_edge_cases(self):
        # Test with None values
        arr = [3, None, 1, 4, None, 2]
        with self.assertRaises(TypeError):
            merge_sort(arr)
        
        # Test with mixed types
        arr = [3, 'apple', 1, 'banana', 2]
        with self.assertRaises(TypeError):
            merge_sort(arr)
        
        # Test with invalid key function
        arr = [3, 1, 4, 1, 5]
        with self.assertRaises(TypeError):
            merge_sort(arr, key=lambda x: x.nonexistent)
    
    def test_performance(self):
        # Test with large list
        arr = list(range(1000, 0, -1))
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, list(range(1, 1001)))
        
        # Test with large list (in-place)
        arr = list(range(1000, 0, -1))
        merge_sort_in_place(arr)
        self.assertEqual(arr, list(range(1, 1001)))


if __name__ == '__main__':
    unittest.main() 