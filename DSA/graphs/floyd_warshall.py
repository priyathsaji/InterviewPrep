"""
Problem Statement:
Given a directed weighted graph with n vertices, find the shortest path between every pair of vertices.
The graph may contain negative weight edges, but no negative weight cycles.

Input Format:
- n: int - Number of vertices
- edges: List[List[int]] - List of edges [u, v, w] where u and v are vertices and w is the weight

Output Format:
- List[List[int]] - n x n matrix where matrix[i][j] represents the shortest path from vertex i to j
  If there is no path from i to j, return float('inf')

Example:
Input: n = 4, edges = [[0,1,3],[1,2,1],[2,3,4],[3,0,2],[0,2,5]]
Output: [[0,3,4,8],[6,0,1,5],[2,5,0,4],[2,5,6,0]]
Explanation: The output matrix shows the shortest path between every pair of vertices.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= 9900
- -1000 <= weight <= 1000
- No negative weight cycles

Time Complexity: O(V^3) where V is the number of vertices
Space Complexity: O(V^2)
"""

from typing import List

class Solution:
    def floydWarshall(self, n: int, edges: List[List[int]]) -> List[List[float]]:
        """
        Find shortest paths between all pairs of vertices using Floyd-Warshall algorithm.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 4
        edges = [[0,1,3],[1,2,1],[2,3,4],[3,0,2],[0,2,5]]
        expected = [[0,3,4,8],[6,0,1,5],[2,5,0,4],[2,5,6,0]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result, expected)
    
    def test_single_vertex(self):
        n = 1
        edges = []
        expected = [[0]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result, expected)
    
    def test_disconnected_graph(self):
        n = 3
        edges = [[0,1,1]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[1][0], float('inf'))
        self.assertEqual(result[0][2], float('inf'))
    
    def test_negative_weights(self):
        n = 3
        edges = [[0,1,-1],[1,2,-2],[2,0,-3]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result[0][1], -1)
        self.assertEqual(result[1][2], -2)
        self.assertEqual(result[2][0], -3)
    
    def test_self_loops(self):
        n = 2
        edges = [[0,0,1],[1,1,2]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result[0][0], 0)  # Self-loops should be ignored
        self.assertEqual(result[1][1], 0)
    
    def test_multiple_paths(self):
        n = 3
        edges = [[0,1,1],[1,2,2],[0,2,4]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result[0][2], 3)  # Should take path 0->1->2
    
    def test_maximum_constraints(self):
        n = 100
        edges = [[i,j,1] for i in range(n) for j in range(n) if i != j]
        result = self.solution.floydWarshall(n, edges)
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.assertEqual(result[i][j], 1)
    
    def test_no_edges(self):
        n = 3
        edges = []
        result = self.solution.floydWarshall(n, edges)
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.assertEqual(result[i][j], 0)
                else:
                    self.assertEqual(result[i][j], float('inf'))
    
    def test_cycle(self):
        n = 4
        edges = [[0,1,1],[1,2,1],[2,3,1],[3,0,1]]
        result = self.solution.floydWarshall(n, edges)
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.assertLess(result[i][j], float('inf'))
    
    def test_directed_path(self):
        n = 4
        edges = [[0,1,1],[1,2,1],[2,3,1]]
        result = self.solution.floydWarshall(n, edges)
        self.assertEqual(result[0][3], 3)
        self.assertEqual(result[3][0], float('inf'))

if __name__ == '__main__':
    unittest.main() 