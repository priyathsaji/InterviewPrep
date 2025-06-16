"""
Fibonacci Sequence Implementation

The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, usually starting with 0 and 1.

Time Complexity:
- Naive Recursive: O(2^n)
- Memoization: O(n)
- Tabulation: O(n)
- Matrix Exponentiation: O(log n)

Space Complexity:
- Naive Recursive: O(n) for call stack
- Memoization: O(n) for memo table and call stack
- Tabulation: O(n) for dp table
- Matrix Exponentiation: O(1)

Applications:
1. Population growth modeling
2. Financial market analysis
3. Computer algorithms (e.g., Fibonacci heap)
4. Art and architecture (golden ratio)
"""

from typing import Dict, List
import unittest

def fibonacci_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using naive recursion.
    
    Args:
        n: The position in the Fibonacci sequence (0-based)
        
    Returns:
        The nth Fibonacci number
        
    Example:
        >>> fibonacci_recursive(5)
        5
        >>> fibonacci_recursive(10)
        55
    """
    raise NotImplementedError("Recursive Fibonacci implementation not completed")

def fibonacci_memoization(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculate the nth Fibonacci number using memoization.
    
    Args:
        n: The position in the Fibonacci sequence (0-based)
        memo: Dictionary to store previously calculated values
        
    Returns:
        The nth Fibonacci number
        
    Example:
        >>> fibonacci_memoization(5)
        5
        >>> fibonacci_memoization(10)
        55
    """
    raise NotImplementedError("Memoization Fibonacci implementation not completed")

def fibonacci_tabulation(n: int) -> int:
    """
    Calculate the nth Fibonacci number using tabulation (bottom-up approach).
    
    Args:
        n: The position in the Fibonacci sequence (0-based)
        
    Returns:
        The nth Fibonacci number
        
    Example:
        >>> fibonacci_tabulation(5)
        5
        >>> fibonacci_tabulation(10)
        55
    """
    raise NotImplementedError("Tabulation Fibonacci implementation not completed")

def fibonacci_matrix(n: int) -> int:
    """
    Calculate the nth Fibonacci number using matrix exponentiation.
    
    Args:
        n: The position in the Fibonacci sequence (0-based)
        
    Returns:
        The nth Fibonacci number
        
    Example:
        >>> fibonacci_matrix(5)
        5
        >>> fibonacci_matrix(10)
        55
    """
    raise NotImplementedError("Matrix Fibonacci implementation not completed")


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(10), 55)
    
    def test_fibonacci_memoization(self):
        self.assertEqual(fibonacci_memoization(0), 0)
        self.assertEqual(fibonacci_memoization(1), 1)
        self.assertEqual(fibonacci_memoization(2), 1)
        self.assertEqual(fibonacci_memoization(5), 5)
        self.assertEqual(fibonacci_memoization(10), 55)
        self.assertEqual(fibonacci_memoization(20), 6765)
    
    def test_fibonacci_tabulation(self):
        self.assertEqual(fibonacci_tabulation(0), 0)
        self.assertEqual(fibonacci_tabulation(1), 1)
        self.assertEqual(fibonacci_tabulation(2), 1)
        self.assertEqual(fibonacci_tabulation(5), 5)
        self.assertEqual(fibonacci_tabulation(10), 55)
        self.assertEqual(fibonacci_tabulation(20), 6765)
    
    def test_fibonacci_matrix(self):
        self.assertEqual(fibonacci_matrix(0), 0)
        self.assertEqual(fibonacci_matrix(1), 1)
        self.assertEqual(fibonacci_matrix(2), 1)
        self.assertEqual(fibonacci_matrix(5), 5)
        self.assertEqual(fibonacci_matrix(10), 55)
        self.assertEqual(fibonacci_matrix(20), 6765)
    
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_memoization(-1)
        with self.assertRaises(ValueError):
            fibonacci_tabulation(-1)
        with self.assertRaises(ValueError):
            fibonacci_matrix(-1)
    
    def test_large_input(self):
        # Test that all implementations can handle larger inputs
        n = 30
        expected = 832040
        self.assertEqual(fibonacci_memoization(n), expected)
        self.assertEqual(fibonacci_tabulation(n), expected)
        self.assertEqual(fibonacci_matrix(n), expected)


if __name__ == '__main__':
    unittest.main() 