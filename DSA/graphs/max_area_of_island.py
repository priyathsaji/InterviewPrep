"""
Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input Format:
- grid: List[List[int]] - 2D binary matrix where 1 represents land and 0 represents water

Output Format:
- int - Maximum area of an island

Example:
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
Explanation: There is no island, so return 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

Time Complexity: O(m * n) where m and n are the dimensions of the grid
Space Complexity: O(m * n) in worst case for the recursion stack
"""

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Return the maximum area of an island in the grid.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 6)
    
    def test_example2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_single_cell_land(self):
        grid = [[1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_single_cell_water(self):
        grid = [[0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_single_row_land(self):
        grid = [[1,1,1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 3)
    
    def test_single_row_water(self):
        grid = [[0,0,0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_single_column_land(self):
        grid = [[1],[1],[1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 3)
    
    def test_single_column_water(self):
        grid = [[0],[0],[0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_checkerboard(self):
        grid = [
            [1,0,1,0],
            [0,1,0,1],
            [1,0,1,0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_surrounded_island(self):
        grid = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 9)
    
    def test_diagonal_islands(self):
        grid = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_maximum_size(self):
        grid = [[1 for _ in range(50)] for _ in range(50)]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 2500)
    
    def test_complex_pattern(self):
        grid = [
            [1,1,0,0,0,1,1],
            [1,0,0,0,0,0,1],
            [0,0,1,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,1,0,0],
            [1,0,0,0,0,0,1],
            [1,1,0,0,0,1,1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)
    
    def test_spiral_pattern(self):
        grid = [
            [1,1,1,1,1],
            [0,0,0,0,1],
            [1,1,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 16)
    
    def test_hollow_square(self):
        grid = [
            [1,1,1,1],
            [1,0,0,1],
            [1,0,0,1],
            [1,1,1,1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 12)
    
    def test_multiple_islands(self):
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)

if __name__ == '__main__':
    unittest.main() 