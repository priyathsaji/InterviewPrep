"""
Problem Statement:
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would have:
(ABC)D = (AB)(CD) = A(BCD) = A(BC)D = ...

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,
(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a function that should return the minimum number of multiplications needed to multiply the chain.

Input Format:
- p: List[int] - Array representing dimensions of matrices

Output Format:
- int - Minimum number of multiplications needed

Example:
Input: p = [1, 2, 3, 4]
Output: 18
Explanation: The matrices are of dimensions 1×2, 2×3, and 3×4.
The minimum number of multiplications is obtained by putting parenthesis in following way:
((AB)C) = 1×2×3 + 1×3×4 = 6 + 12 = 18

Input: p = [40, 20, 30, 10, 30]
Output: 26000
Explanation: There are 4 matrices of dimensions 40×20, 20×30, 30×10 and 10×30.
The minimum number of multiplications is 26000.

Constraints:
- 2 <= len(p) <= 100
- 1 <= p[i] <= 100

Time Complexity: O(n³) where n is the number of matrices
Space Complexity: O(n²) where n is the number of matrices
"""

class Solution:
    def matrixChainOrder(self, p: list[int]) -> int:
        """
        Find the minimum number of multiplications needed to multiply the chain of matrices.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        p = [1, 2, 3, 4]
        self.assertEqual(self.solution.matrixChainOrder(p), 18)
    
    def test_example2(self):
        p = [40, 20, 30, 10, 30]
        self.assertEqual(self.solution.matrixChainOrder(p), 26000)
    
    def test_two_matrices(self):
        p = [1, 2, 3]
        self.assertEqual(self.solution.matrixChainOrder(p), 6)
    
    def test_three_matrices(self):
        p = [10, 20, 30, 40]
        self.assertEqual(self.solution.matrixChainOrder(p), 18000)
    
    def test_four_matrices(self):
        p = [5, 10, 15, 20, 25]
        self.assertEqual(self.solution.matrixChainOrder(p), 4375)
    
    def test_square_matrices(self):
        p = [2, 2, 2, 2]
        self.assertEqual(self.solution.matrixChainOrder(p), 16)
    
    def test_rectangular_matrices(self):
        p = [1, 5, 5, 1]
        self.assertEqual(self.solution.matrixChainOrder(p), 10)
    
    def test_large_dimensions(self):
        p = [100, 50, 25, 10, 5]
        self.assertEqual(self.solution.matrixChainOrder(p), 187500)
    
    def test_small_dimensions(self):
        p = [1, 1, 1, 1]
        self.assertEqual(self.solution.matrixChainOrder(p), 2)
    
    def test_alternating_dimensions(self):
        p = [2, 3, 2, 3, 2]
        self.assertEqual(self.solution.matrixChainOrder(p), 42)
    
    def test_increasing_dimensions(self):
        p = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.matrixChainOrder(p), 38)

if __name__ == '__main__':
    unittest.main() 