"""
Fractional Knapsack Problem

The Fractional Knapsack Problem is a classic greedy algorithm problem where we are given
a set of items with their weights and values, and we need to select items to maximize
the total value while keeping the total weight within a given capacity. Unlike the 0/1
Knapsack problem, we can take fractional parts of items.

Time Complexity:
- Best: O(n log n) for sorting
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity:
- O(n) for storing items and result

Characteristics:
1. Greedy approach works optimally
2. Items must be sorted by value/weight ratio
3. Can take fractional parts of items
4. Always selects items with highest value/weight ratio first
"""

from typing import List, Tuple
import unittest

def fractional_knapsack(items: List[Tuple[float, float]], capacity: float) -> List[Tuple[float, float, float]]:
    """
    Solve the fractional knapsack problem.
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity of knapsack
        
    Returns:
        List of tuples (weight, value, fraction) representing selected items
        and their fractions
        
    Example:
        >>> fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50)
        [(10, 60, 1.0), (20, 100, 1.0), (30, 120, 0.6666666666666666)]
    """
    raise NotImplementedError("Fractional knapsack implementation not completed")

def fractional_knapsack_with_constraints(items: List[Tuple[float, float, float]], capacity: float) -> List[Tuple[float, float, float, float]]:
    """
    Solve the fractional knapsack problem with minimum and maximum fraction constraints.
    
    Args:
        items: List of tuples (weight, value, min_fraction)
        capacity: Maximum weight capacity of knapsack
        
    Returns:
        List of tuples (weight, value, min_fraction, fraction) representing selected items
        and their fractions
        
    Example:
        >>> fractional_knapsack_with_constraints([(10, 60, 0.5), (20, 100, 0.3), (30, 120, 0.2)], 50)
        [(10, 60, 0.5, 1.0), (20, 100, 0.3, 1.0), (30, 120, 0.2, 0.6666666666666666)]
    """
    raise NotImplementedError("Fractional knapsack with constraints implementation not completed")

def fractional_knapsack_with_categories(items: List[Tuple[float, float, str]], capacity: float, category_limits: dict[str, float]) -> List[Tuple[float, float, str, float]]:
    """
    Solve the fractional knapsack problem with category-wise capacity limits.
    
    Args:
        items: List of tuples (weight, value, category)
        capacity: Maximum total weight capacity of knapsack
        category_limits: Dictionary mapping categories to their maximum weights
        
    Returns:
        List of tuples (weight, value, category, fraction) representing selected items
        and their fractions
        
    Example:
        >>> items = [(10, 60, "A"), (20, 100, "B"), (30, 120, "A")]
        >>> limits = {"A": 30, "B": 20}
        >>> fractional_knapsack_with_categories(items, 50, limits)
        [(10, 60, "A", 1.0), (20, 100, "B", 1.0), (30, 120, "A", 0.6666666666666666)]
    """
    raise NotImplementedError("Fractional knapsack with categories implementation not completed")


class TestFractionalKnapsack(unittest.TestCase):
    def test_fractional_knapsack(self):
        # Test with simple items
        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(sum(w * f for w, _, f in result), capacity)
        self.assertTrue(all(0 <= f <= 1 for _, _, f in result))
        
        # Test with zero capacity
        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 0
        result = fractional_knapsack(items, capacity)
        self.assertEqual(len(result), 0)
        
        # Test with infinite capacity
        items = [(10, 60), (20, 100), (30, 120)]
        capacity = float('inf')
        result = fractional_knapsack(items, capacity)
        self.assertTrue(all(f == 1.0 for _, _, f in result))
        
        # Test with no items
        items = []
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertEqual(len(result), 0)
        
        # Test with single item
        items = [(10, 60)]
        capacity = 5
        result = fractional_knapsack(items, capacity)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0][2], 0.5)
    
    def test_fractional_knapsack_with_constraints(self):
        # Test with simple items
        items = [(10, 60, 0.5), (20, 100, 0.3), (30, 120, 0.2)]
        capacity = 50
        result = fractional_knapsack_with_constraints(items, capacity)
        self.assertAlmostEqual(sum(w * f for w, _, _, f in result), capacity)
        self.assertTrue(all(mf <= f <= 1 for _, _, mf, f in result))
        
        # Test with zero capacity
        items = [(10, 60, 0.5), (20, 100, 0.3), (30, 120, 0.2)]
        capacity = 0
        result = fractional_knapsack_with_constraints(items, capacity)
        self.assertEqual(len(result), 0)
        
        # Test with no items
        items = []
        capacity = 50
        result = fractional_knapsack_with_constraints(items, capacity)
        self.assertEqual(len(result), 0)
        
        # Test with single item
        items = [(10, 60, 0.5)]
        capacity = 5
        result = fractional_knapsack_with_constraints(items, capacity)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0][3], 0.5)
    
    def test_fractional_knapsack_with_categories(self):
        # Test with simple items
        items = [(10, 60, "A"), (20, 100, "B"), (30, 120, "A")]
        capacity = 50
        category_limits = {"A": 30, "B": 20}
        result = fractional_knapsack_with_categories(items, capacity, category_limits)
        
        # Check total weight
        self.assertAlmostEqual(sum(w * f for w, _, _, f in result), capacity)
        
        # Check category limits
        category_weights = {}
        for w, _, c, f in result:
            category_weights[c] = category_weights.get(c, 0) + w * f
        for category, limit in category_limits.items():
            self.assertLessEqual(category_weights.get(category, 0), limit)
        
        # Test with zero capacity
        items = [(10, 60, "A"), (20, 100, "B"), (30, 120, "A")]
        capacity = 0
        category_limits = {"A": 30, "B": 20}
        result = fractional_knapsack_with_categories(items, capacity, category_limits)
        self.assertEqual(len(result), 0)
        
        # Test with no items
        items = []
        capacity = 50
        category_limits = {"A": 30, "B": 20}
        result = fractional_knapsack_with_categories(items, capacity, category_limits)
        self.assertEqual(len(result), 0)
        
        # Test with single item
        items = [(10, 60, "A")]
        capacity = 5
        category_limits = {"A": 30}
        result = fractional_knapsack_with_categories(items, capacity, category_limits)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0][3], 0.5)
    
    def test_edge_cases(self):
        # Test with zero weight items
        items = [(0, 60), (0, 100), (0, 120)]
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertTrue(all(f == 1.0 for _, _, f in result))
        
        # Test with zero value items
        items = [(10, 0), (20, 0), (30, 0)]
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertTrue(all(f == 0.0 for _, _, f in result))
        
        # Test with negative weights
        items = [(-10, 60), (-20, 100), (-30, 120)]
        capacity = 50
        with self.assertRaises(ValueError):
            fractional_knapsack(items, capacity)
        
        # Test with negative values
        items = [(10, -60), (20, -100), (30, -120)]
        capacity = 50
        with self.assertRaises(ValueError):
            fractional_knapsack(items, capacity)
    
    def test_performance(self):
        # Test with many items
        items = [(i, i * 2) for i in range(1000)]
        capacity = 5000
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(sum(w * f for w, _, f in result), capacity)
        
        # Test with many categories
        items = [(i, i * 2, chr(i % 26 + 65)) for i in range(1000)]
        capacity = 5000
        category_limits = {chr(i + 65): 200 for i in range(26)}
        result = fractional_knapsack_with_categories(items, capacity, category_limits)
        self.assertAlmostEqual(sum(w * f for w, _, _, f in result), capacity)


if __name__ == '__main__':
    unittest.main() 