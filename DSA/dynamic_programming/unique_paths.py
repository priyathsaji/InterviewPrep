"""
Problem Statement:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Input Format:
- m: int - Number of rows in the grid
- n: int - Number of columns in the grid

Output Format:
- int - Number of unique paths

Example:
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
- 1 <= m, n <= 100

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Find the number of unique paths from top-left to bottom-right corner.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        m, n = 3, 7
        self.assertEqual(self.solution.uniquePaths(m, n), 28)
    
    def test_example2(self):
        m, n = 3, 2
        self.assertEqual(self.solution.uniquePaths(m, n), 3)
    
    def test_single_row(self):
        m, n = 1, 5
        self.assertEqual(self.solution.uniquePaths(m, n), 1)
    
    def test_single_column(self):
        m, n = 5, 1
        self.assertEqual(self.solution.uniquePaths(m, n), 1)
    
    def test_square_grid(self):
        m, n = 2, 2
        self.assertEqual(self.solution.uniquePaths(m, n), 2)
    
    def test_minimum_size(self):
        m, n = 1, 1
        self.assertEqual(self.solution.uniquePaths(m, n), 1)
    
    def test_medium_grid(self):
        m, n = 4, 4
        self.assertEqual(self.solution.uniquePaths(m, n), 20)
    
    def test_rectangular_grid(self):
        m, n = 3, 4
        self.assertEqual(self.solution.uniquePaths(m, n), 10)
    
    def test_large_grid(self):
        m, n = 7, 3
        self.assertEqual(self.solution.uniquePaths(m, n), 28)

if __name__ == '__main__':
    unittest.main() 