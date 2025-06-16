"""
Quick Sort Algorithm

Quick Sort is a divide-and-conquer algorithm that picks an element as a pivot and partitions the array around the pivot.
The key process in quick sort is partition(). Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater
elements (greater than x) after x.

Time Complexity:
- Best: O(n log n) where n is the number of elements
- Average: O(n log n)
- Worst: O(n^2) when the array is already sorted or reverse sorted

Space Complexity:
- O(log n) for recursion stack

Characteristics:
1. In-place sorting algorithm
2. Not stable sorting algorithm
3. Works well with arrays
4. Performance depends on pivot selection
5. Cache-friendly due to good locality of reference
"""

from typing import List, TypeVar, Optional, Tuple
import unittest
import random

T = TypeVar('T')

def quick_sort(arr: List[T], key: Optional[callable] = None) -> List[T]:
    """
    Sort a list using the quick sort algorithm.
    
    Args:
        arr: List of elements to be sorted
        key: Optional function to extract comparison key from elements
        
    Returns:
        Sorted list
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> sorted_arr = quick_sort(arr)
        >>> sorted_arr == [11, 12, 22, 25, 34, 64, 90]
        True
    """
    if len(arr) <= 1:
        return arr
    
    arr = arr.copy()  # Create a copy to avoid modifying the original list
    _quick_sort(arr, 0, len(arr) - 1, key)
    return arr

def _quick_sort(arr: List[T], low: int, high: int, key: Optional[callable] = None) -> None:
    """
    Helper function for quick sort.
    
    Args:
        arr: List to be sorted
        low: Starting index of the subarray
        high: Ending index of the subarray
        key: Optional function to extract comparison key from elements
    """
    if low < high:
        # pi is partitioning index
        pi = _partition(arr, low, high, key)
        
        # Separately sort elements before and after partition
        _quick_sort(arr, low, pi - 1, key)
        _quick_sort(arr, pi + 1, high, key)

def _partition(arr: List[T], low: int, high: int, key: Optional[callable] = None) -> int:
    """
    Partition the array around a pivot.
    
    Args:
        arr: List to be partitioned
        low: Starting index of the subarray
        high: Ending index of the subarray
        key: Optional function to extract comparison key from elements
        
    Returns:
        Index of the pivot after partitioning
    """
    # Choose a random pivot
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]
    pivot_val = key(pivot) if key else pivot
    
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        curr_val = key(arr[j]) if key else arr[j]
        if curr_val <= pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_in_place(arr: List[T], key: Optional[callable] = None) -> None:
    """
    Sort a list in-place using the quick sort algorithm.
    
    Args:
        arr: List of elements to be sorted
        key: Optional function to extract comparison key from elements
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> quick_sort_in_place(arr)
        >>> arr == [11, 12, 22, 25, 34, 64, 90]
        True
    """
    if len(arr) <= 1:
        return
    
    _quick_sort(arr, 0, len(arr) - 1, key)

def quick_select(arr: List[T], k: int, key: Optional[callable] = None) -> T:
    """
    Find the k-th smallest element in an unsorted list using quick select algorithm.
    
    Args:
        arr: List of elements
        k: Index of the element to find (0-based)
        key: Optional function to extract comparison key from elements
        
    Returns:
        The k-th smallest element
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> quick_select(arr, 3)  # Find the 4th smallest element
        25
    """
    if not 0 <= k < len(arr):
        raise IndexError("k is out of range")
    
    arr = arr.copy()  # Create a copy to avoid modifying the original list
    return _quick_select(arr, 0, len(arr) - 1, k, key)

def _quick_select(arr: List[T], low: int, high: int, k: int, key: Optional[callable] = None) -> T:
    """
    Helper function for quick select.
    
    Args:
        arr: List of elements
        low: Starting index of the subarray
        high: Ending index of the subarray
        k: Index of the element to find
        key: Optional function to extract comparison key from elements
        
    Returns:
        The k-th smallest element
    """
    if low == high:
        return arr[low]
    
    pi = _partition(arr, low, high, key)
    
    if k == pi:
        return arr[k]
    elif k < pi:
        return _quick_select(arr, low, pi - 1, k, key)
    else:
        return _quick_select(arr, pi + 1, high, k, key)


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        # Test with integers
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [('banana', 3), ('apple', 1), ('cherry', 2), ('date', 4)]
        sorted_arr = quick_sort(arr, key=lambda x: x[1])
        self.assertEqual(sorted_arr, [('apple', 1), ('cherry', 2), ('banana', 3), ('date', 4)])
        
        # Test with empty list
        arr = []
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [])
        
        # Test with single element
        arr = [1]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [1])
        
        # Test with duplicate elements
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_quick_sort_in_place(self):
        # Test with integers
        arr = [64, 34, 25, 12, 22, 11, 90]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        quick_sort_in_place(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
        
        # Test with custom key
        arr = [('banana', 3), ('apple', 1), ('cherry', 2), ('date', 4)]
        quick_sort_in_place(arr, key=lambda x: x[1])
        self.assertEqual(arr, [('apple', 1), ('cherry', 2), ('banana', 3), ('date', 4)])
        
        # Test with empty list
        arr = []
        quick_sort_in_place(arr)
        self.assertEqual(arr, [])
        
        # Test with single element
        arr = [1]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1])
        
        # Test with duplicate elements
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quick_sort_in_place(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_quick_select(self):
        # Test with integers
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(quick_select(arr, 3), 25)  # 4th smallest element
        self.assertEqual(quick_select(arr, 0), 11)  # smallest element
        self.assertEqual(quick_select(arr, len(arr) - 1), 90)  # largest element
        
        # Test with strings
        arr = ['banana', 'apple', 'cherry', 'date']
        self.assertEqual(quick_select(arr, 1), 'banana')  # 2nd smallest element
        
        # Test with custom key
        arr = [('banana', 3), ('apple', 1), ('cherry', 2), ('date', 4)]
        self.assertEqual(quick_select(arr, 2, key=lambda x: x[1]), ('banana', 3))
        
        # Test with single element
        arr = [1]
        self.assertEqual(quick_select(arr, 0), 1)
        
        # Test with duplicate elements
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(quick_select(arr, 5), 4)  # 6th smallest element
    
    def test_edge_cases(self):
        # Test with None values
        arr = [3, None, 1, 4, None, 2]
        with self.assertRaises(TypeError):
            quick_sort(arr)
        
        # Test with mixed types
        arr = [3, 'apple', 1, 'banana', 2]
        with self.assertRaises(TypeError):
            quick_sort(arr)
        
        # Test with invalid key function
        arr = [3, 1, 4, 1, 5]
        with self.assertRaises(TypeError):
            quick_sort(arr, key=lambda x: x.nonexistent)
        
        # Test quick_select with invalid k
        arr = [1, 2, 3]
        with self.assertRaises(IndexError):
            quick_select(arr, -1)
        with self.assertRaises(IndexError):
            quick_select(arr, 3)
    
    def test_performance(self):
        # Test with large list
        arr = list(range(1000, 0, -1))
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, list(range(1, 1001)))
        
        # Test with large list (in-place)
        arr = list(range(1000, 0, -1))
        quick_sort_in_place(arr)
        self.assertEqual(arr, list(range(1, 1001)))
        
        # Test quick_select with large list
        arr = list(range(1000, 0, -1))
        self.assertEqual(quick_select(arr, 499), 500)  # middle element


if __name__ == '__main__':
    unittest.main() 