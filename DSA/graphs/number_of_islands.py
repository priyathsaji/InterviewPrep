"""
Problem Statement:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input Format:
- grid: List[List[str]] - 2D grid of '1's and '0's

Output Format:
- int - Number of islands

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Explanation: There is one island in the grid.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
Explanation: There are three islands in the grid.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

Time Complexity: O(m * n) where m and n are the dimensions of the grid
Space Complexity: O(m * n) in worst case for the recursion stack
"""

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Return the number of islands in the grid.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_example2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)
    
    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_single_cell_land(self):
        grid = [["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_single_cell_water(self):
        grid = [["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_single_row_land(self):
        grid = [["1","1","1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_single_row_water(self):
        grid = [["0","0","0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_single_column_land(self):
        grid = [["1"],["1"],["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_single_column_water(self):
        grid = [["0"],["0"],["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_checkerboard(self):
        grid = [
            ["1","0","1","0"],
            ["0","1","0","1"],
            ["1","0","1","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 6)
    
    def test_surrounded_island(self):
        grid = [
            ["0","0","0","0","0"],
            ["0","1","1","1","0"],
            ["0","1","1","1","0"],
            ["0","1","1","1","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_diagonal_islands(self):
        grid = [
            ["1","0","0","0"],
            ["0","1","0","0"],
            ["0","0","1","0"],
            ["0","0","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 4)
    
    def test_maximum_size(self):
        grid = [["1" for _ in range(300)] for _ in range(300)]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_complex_pattern(self):
        grid = [
            ["1","1","0","0","0","1","1"],
            ["1","0","0","0","0","0","1"],
            ["0","0","1","0","1","0","0"],
            ["0","0","0","1","0","0","0"],
            ["0","0","1","0","1","0","0"],
            ["1","0","0","0","0","0","1"],
            ["1","1","0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 7)
    
    def test_spiral_pattern(self):
        grid = [
            ["1","1","1","1","1"],
            ["0","0","0","0","1"],
            ["1","1","0","0","1"],
            ["1","0","0","0","1"],
            ["1","1","1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 2)
    
    def test_hollow_square(self):
        grid = [
            ["1","1","1","1"],
            ["1","0","0","1"],
            ["1","0","0","1"],
            ["1","1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

if __name__ == '__main__':
    unittest.main() 