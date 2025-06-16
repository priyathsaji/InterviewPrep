"""
Activity Selection Problem

The Activity Selection Problem is a classic greedy algorithm problem where we are given
a set of activities with their start and finish times, and we need to select the maximum
number of activities that can be performed by a single person, assuming that a person
can only work on a single activity at a time.

Time Complexity:
- Best: O(n log n) for sorting
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity:
- O(n) for storing the activities and result

Characteristics:
1. Greedy approach works optimally
2. Activities must be sorted by finish time
3. No two activities can overlap
4. Always selects the activity with earliest finish time
"""

from typing import List, Tuple
import unittest

def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.
    
    Args:
        activities: List of tuples (start_time, finish_time)
        
    Returns:
        List of selected activities
        
    Example:
        >>> activity_selection([(1, 4), (2, 6), (3, 9), (5, 7), (8, 10)])
        [(1, 4), (5, 7), (8, 10)]
    """
    raise NotImplementedError("Activity selection implementation not completed")

def activity_selection_with_weights(activities: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]:
    """
    Select activities with maximum total weight where no two activities overlap.
    
    Args:
        activities: List of tuples (start_time, finish_time, weight)
        
    Returns:
        List of selected activities with maximum total weight
        
    Example:
        >>> activity_selection_with_weights([(1, 4, 2), (2, 6, 4), (3, 9, 3), (5, 7, 1), (8, 10, 5)])
        [(2, 6, 4), (8, 10, 5)]
    """
    raise NotImplementedError("Weighted activity selection implementation not completed")

def activity_selection_with_deadlines(activities: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Select activities that must be completed before their deadlines.
    
    Args:
        activities: List of tuples (start_time, duration, deadline)
        
    Returns:
        List of selected activities that meet their deadlines
        
    Example:
        >>> activity_selection_with_deadlines([(1, 2, 4), (2, 3, 6), (3, 4, 9), (5, 2, 7), (8, 2, 10)])
        [(1, 2, 4), (5, 2, 7), (8, 2, 10)]
    """
    raise NotImplementedError("Activity selection with deadlines implementation not completed")


class TestActivitySelection(unittest.TestCase):
    def test_activity_selection(self):
        # Test with simple activities
        activities = [(1, 4), (2, 6), (3, 9), (5, 7), (8, 10)]
        expected = [(1, 4), (5, 7), (8, 10)]
        self.assertEqual(activity_selection(activities), expected)
        
        # Test with overlapping activities
        activities = [(1, 3), (2, 4), (3, 5), (4, 6)]
        expected = [(1, 3), (4, 6)]
        self.assertEqual(activity_selection(activities), expected)
        
        # Test with no activities
        activities = []
        expected = []
        self.assertEqual(activity_selection(activities), expected)
        
        # Test with single activity
        activities = [(1, 4)]
        expected = [(1, 4)]
        self.assertEqual(activity_selection(activities), expected)
        
        # Test with all overlapping activities
        activities = [(1, 4), (2, 5), (3, 6)]
        expected = [(1, 4)]
        self.assertEqual(activity_selection(activities), expected)
    
    def test_activity_selection_with_weights(self):
        # Test with simple activities
        activities = [(1, 4, 2), (2, 6, 4), (3, 9, 3), (5, 7, 1), (8, 10, 5)]
        expected = [(2, 6, 4), (8, 10, 5)]
        self.assertEqual(activity_selection_with_weights(activities), expected)
        
        # Test with equal weights
        activities = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1)]
        expected = [(1, 3, 1), (4, 6, 1)]
        self.assertEqual(activity_selection_with_weights(activities), expected)
        
        # Test with no activities
        activities = []
        expected = []
        self.assertEqual(activity_selection_with_weights(activities), expected)
        
        # Test with single activity
        activities = [(1, 4, 2)]
        expected = [(1, 4, 2)]
        self.assertEqual(activity_selection_with_weights(activities), expected)
        
        # Test with all overlapping activities
        activities = [(1, 4, 2), (2, 5, 4), (3, 6, 3)]
        expected = [(2, 5, 4)]
        self.assertEqual(activity_selection_with_weights(activities), expected)
    
    def test_activity_selection_with_deadlines(self):
        # Test with simple activities
        activities = [(1, 2, 4), (2, 3, 6), (3, 4, 9), (5, 2, 7), (8, 2, 10)]
        expected = [(1, 2, 4), (5, 2, 7), (8, 2, 10)]
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
        
        # Test with activities that can't meet deadlines
        activities = [(1, 3, 2), (2, 3, 3), (3, 3, 4)]
        expected = [(1, 3, 2)]
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
        
        # Test with no activities
        activities = []
        expected = []
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
        
        # Test with single activity
        activities = [(1, 2, 4)]
        expected = [(1, 2, 4)]
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
        
        # Test with all activities meeting deadlines
        activities = [(1, 2, 4), (3, 2, 6), (5, 2, 8)]
        expected = [(1, 2, 4), (3, 2, 6), (5, 2, 8)]
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
    
    def test_edge_cases(self):
        # Test with zero duration activities
        activities = [(1, 0, 4), (2, 0, 6), (3, 0, 9)]
        expected = [(1, 0, 4), (2, 0, 6), (3, 0, 9)]
        self.assertEqual(activity_selection_with_deadlines(activities), expected)
        
        # Test with negative times
        activities = [(-1, 4), (-2, 6), (-3, 9)]
        expected = [(-3, 9)]
        self.assertEqual(activity_selection(activities), expected)
        
        # Test with very large times
        activities = [(1, 1000000), (2, 2000000), (3, 3000000)]
        expected = [(1, 1000000)]
        self.assertEqual(activity_selection(activities), expected)
    
    def test_performance(self):
        # Test with many activities
        activities = [(i, i + 1) for i in range(1000)]
        result = activity_selection(activities)
        self.assertEqual(len(result), 1000)
        
        # Test with many overlapping activities
        activities = [(1, 1000) for _ in range(1000)]
        result = activity_selection(activities)
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main() 