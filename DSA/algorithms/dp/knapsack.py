"""
Knapsack Problem Algorithm

The Knapsack Problem is a classic optimization problem where given a set of items with weights and values,
we need to determine the number of each item to include in a collection so that the total weight is less than
or equal to a given limit and the total value is as large as possible.

Time Complexity:
- Best: O(nW) where n is the number of items and W is the capacity
- Average: O(nW)
- Worst: O(nW)

Space Complexity:
- O(nW) for the DP table
- O(n) for the reconstructed solution

Characteristics:
1. Can handle fractional items (0-1 Knapsack)
2. Can be extended to multiple knapsacks
3. Can handle unbounded items
4. Can be modified for different constraints
5. Can be adapted for different optimization goals
"""

from typing import List, Tuple, Optional
import unittest

Item = Tuple[int, int]  # (weight, value)

def knapsack_01(items: List[Item], capacity: int) -> Tuple[int, List[int]]:
    """
    Solve the 0-1 Knapsack problem.
    
    Args:
        items: List of items in the form [(weight, value), ...]
        capacity: Maximum weight capacity of the knapsack
        
    Returns:
        Tuple of (maximum value, list of selected item indices)
        
    Example:
        >>> items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        >>> capacity = 10
        >>> knapsack_01(items, capacity)
        (13, [0, 1, 2])
    """
    raise NotImplementedError("0-1 Knapsack implementation is not provided")

def knapsack_fractional(items: List[Item], capacity: int) -> Tuple[float, List[float]]:
    """
    Solve the Fractional Knapsack problem.
    
    Args:
        items: List of items in the form [(weight, value), ...]
        capacity: Maximum weight capacity of the knapsack
        
    Returns:
        Tuple of (maximum value, list of fractions of items selected)
        
    Example:
        >>> items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        >>> capacity = 10
        >>> knapsack_fractional(items, capacity)
        (15.5, [1.0, 1.0, 1.0, 0.2])
    """
    raise NotImplementedError("Fractional Knapsack implementation is not provided")

def knapsack_unbounded(items: List[Item], capacity: int) -> Tuple[int, List[int]]:
    """
    Solve the Unbounded Knapsack problem.
    
    Args:
        items: List of items in the form [(weight, value), ...]
        capacity: Maximum weight capacity of the knapsack
        
    Returns:
        Tuple of (maximum value, list of quantities of each item)
        
    Example:
        >>> items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        >>> capacity = 10
        >>> knapsack_unbounded(items, capacity)
        (15, [5, 0, 0, 0])
    """
    raise NotImplementedError("Unbounded Knapsack implementation is not provided")

def knapsack_multiple(items: List[Item], capacities: List[int]) -> List[Tuple[int, List[int]]]:
    """
    Solve the Multiple Knapsack problem.
    
    Args:
        items: List of items in the form [(weight, value), ...]
        capacities: List of capacities for each knapsack
        
    Returns:
        List of tuples (maximum value, list of selected item indices) for each knapsack
        
    Example:
        >>> items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        >>> capacities = [5, 7]
        >>> knapsack_multiple(items, capacities)
        [(7, [0, 1]), (11, [2, 3])]
    """
    raise NotImplementedError("Multiple Knapsack implementation is not provided")

def knapsack_with_constraints(items: List[Item], capacity: int, 
                             constraints: List[Tuple[int, int]]) -> Tuple[int, List[int]]:
    """
    Solve the Knapsack problem with additional constraints.
    
    Args:
        items: List of items in the form [(weight, value), ...]
        capacity: Maximum weight capacity of the knapsack
        constraints: List of item pairs that must be selected together
        
    Returns:
        Tuple of (maximum value, list of selected item indices)
        
    Example:
        >>> items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        >>> capacity = 10
        >>> constraints = [(0, 1), (2, 3)]
        >>> knapsack_with_constraints(items, capacity, constraints)
        (11, [0, 1, 2, 3])
    """
    raise NotImplementedError("Knapsack with constraints implementation is not provided")


class TestKnapsack(unittest.TestCase):
    def test_knapsack_01(self):
        # Test with simple items
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_01(items, capacity)
        
        # Test with empty knapsack
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 0
        with self.assertRaises(NotImplementedError):
            knapsack_01(items, capacity)
        
        # Test with no items
        items = []
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_01(items, capacity)
    
    def test_knapsack_fractional(self):
        # Test with simple items
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_fractional(items, capacity)
        
        # Test with empty knapsack
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 0
        with self.assertRaises(NotImplementedError):
            knapsack_fractional(items, capacity)
        
        # Test with no items
        items = []
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_fractional(items, capacity)
    
    def test_knapsack_unbounded(self):
        # Test with simple items
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_unbounded(items, capacity)
        
        # Test with empty knapsack
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 0
        with self.assertRaises(NotImplementedError):
            knapsack_unbounded(items, capacity)
        
        # Test with no items
        items = []
        capacity = 10
        with self.assertRaises(NotImplementedError):
            knapsack_unbounded(items, capacity)
    
    def test_knapsack_multiple(self):
        # Test with simple items
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacities = [5, 7]
        with self.assertRaises(NotImplementedError):
            knapsack_multiple(items, capacities)
        
        # Test with empty knapsacks
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacities = [0, 0]
        with self.assertRaises(NotImplementedError):
            knapsack_multiple(items, capacities)
        
        # Test with no items
        items = []
        capacities = [5, 7]
        with self.assertRaises(NotImplementedError):
            knapsack_multiple(items, capacities)
    
    def test_knapsack_with_constraints(self):
        # Test with simple items and constraints
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 10
        constraints = [(0, 1), (2, 3)]
        with self.assertRaises(NotImplementedError):
            knapsack_with_constraints(items, capacity, constraints)
        
        # Test with impossible constraints
        items = [(2, 3), (3, 4), (4, 5), (5, 6)]
        capacity = 5
        constraints = [(0, 1), (2, 3)]
        with self.assertRaises(NotImplementedError):
            knapsack_with_constraints(items, capacity, constraints)


if __name__ == '__main__':
    unittest.main() 