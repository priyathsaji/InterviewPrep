"""
Problem Statement:
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input Format:
- points: List[List[int]] - List of point coordinates [x, y]

Output Format:
- int - Minimum cost to connect all points

Example:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Explanation:
We can connect the points as shown above to get the minimum cost of 18.

Constraints:
- 1 <= points.length <= 1000
- -106 <= xi, yi <= 106
- All pairs (xi, yi) are unique

Time Complexity: O(E log E) where E is the number of edges
Space Complexity: O(V) where V is the number of vertices
"""

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Return the minimum cost to connect all points.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 20)
    
    def test_example2(self):
        points = [[3,12],[-2,5],[-4,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 18)
    
    def test_two_points(self):
        points = [[0,0],[1,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)
    
    def test_three_points_line(self):
        points = [[0,0],[1,0],[2,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)
    
    def test_three_points_triangle(self):
        points = [[0,0],[1,0],[0,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)
    
    def test_four_points_square(self):
        points = [[0,0],[0,1],[1,0],[1,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)
    
    def test_negative_coordinates(self):
        points = [[-1,-1],[1,1],[0,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 4)
    
    def test_large_coordinates(self):
        points = [[1000000,1000000],[-1000000,-1000000],[0,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 4000000)
    
    def test_single_point(self):
        points = [[0,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 0)
    
    def test_vertical_line(self):
        points = [[0,0],[0,1],[0,2],[0,3]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)
    
    def test_horizontal_line(self):
        points = [[0,0],[1,0],[2,0],[3,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)
    
    def test_diagonal_line(self):
        points = [[0,0],[1,1],[2,2],[3,3]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 6)
    
    def test_grid_pattern(self):
        points = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 5)
    
    def test_random_points(self):
        points = [[0,0],[2,2],[3,10],[5,2],[7,0],[8,8],[9,9]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 28)
    
    def test_maximum_constraints(self):
        points = [[i,i] for i in range(1000)]
        self.assertEqual(self.solution.minCostConnectPoints(points), 999)
    
    def test_duplicate_points(self):
        points = [[0,0],[0,0],[1,1],[1,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)

if __name__ == '__main__':
    unittest.main() 