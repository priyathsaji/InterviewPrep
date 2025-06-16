"""
Problem Statement:
Given a directed weighted graph with n vertices, determine if it contains a negative weight cycle.
If no negative cycle exists, find the shortest path from a source vertex to all other vertices.

Input Format:
- n: int - Number of vertices
- edges: List[List[int]] - List of edges [u, v, w] where u and v are vertices and w is the weight
- source: int - Source vertex (0-based indexing)

Output Format:
- If negative cycle exists: return [-1]
- Otherwise: return List[int] where result[i] is the shortest path from source to vertex i
  If there is no path from source to i, return float('inf')

Example:
Input: n = 5, edges = [[0,1,-1],[1,2,2],[2,3,3],[3,1,-6],[3,4,4]], source = 0
Output: [-1]
Explanation: The graph contains a negative cycle 1->2->3->1 with total weight -1.

Input: n = 4, edges = [[0,1,1],[1,2,2],[2,3,3]], source = 0
Output: [0,1,3,6]
Explanation: No negative cycle exists. The shortest paths from 0 to all vertices are shown.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= 9900
- -1000 <= weight <= 1000
- 0 <= source < n

Time Complexity: O(VE) where V is the number of vertices and E is the number of edges
Space Complexity: O(V)
"""

from typing import List

class Solution:
    def bellmanFord(self, n: int, edges: List[List[int]], source: int) -> List[float]:
        """
        Find shortest paths from source to all vertices using Bellman-Ford algorithm.
        Return [-1] if a negative cycle is detected.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_negative_cycle(self):
        n = 5
        edges = [[0,1,-1],[1,2,2],[2,3,3],[3,1,-6],[3,4,4]]
        source = 0
        self.assertEqual(self.solution.bellmanFord(n, edges, source), [-1])
    
    def test_no_negative_cycle(self):
        n = 4
        edges = [[0,1,1],[1,2,2],[2,3,3]]
        source = 0
        expected = [0,1,3,6]
        self.assertEqual(self.solution.bellmanFord(n, edges, source), expected)
    
    def test_single_vertex(self):
        n = 1
        edges = []
        source = 0
        expected = [0]
        self.assertEqual(self.solution.bellmanFord(n, edges, source), expected)
    
    def test_disconnected_graph(self):
        n = 3
        edges = [[0,1,1]]
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], float('inf'))
    
    def test_negative_weights_no_cycle(self):
        n = 3
        edges = [[0,1,-1],[1,2,-2]]
        source = 0
        expected = [0,-1,-3]
        self.assertEqual(self.solution.bellmanFord(n, edges, source), expected)
    
    def test_self_loops(self):
        n = 2
        edges = [[0,0,1],[1,1,2]]
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        self.assertEqual(result[0], 0)  # Self-loops should be ignored
        self.assertEqual(result[1], float('inf'))
    
    def test_multiple_paths(self):
        n = 3
        edges = [[0,1,1],[1,2,2],[0,2,4]]
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        self.assertEqual(result[2], 3)  # Should take path 0->1->2
    
    def test_maximum_constraints(self):
        n = 100
        edges = [[i,i+1,1] for i in range(n-1)]
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        for i in range(n):
            self.assertEqual(result[i], i)
    
    def test_no_edges(self):
        n = 3
        edges = []
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], float('inf'))
        self.assertEqual(result[2], float('inf'))
    
    def test_cycle_no_negative(self):
        n = 4
        edges = [[0,1,1],[1,2,1],[2,3,1],[3,0,1]]
        source = 0
        result = self.solution.bellmanFord(n, edges, source)
        self.assertNotEqual(result, [-1])
        self.assertEqual(result[0], 0)
    
    def test_multiple_negative_cycles(self):
        n = 6
        edges = [[0,1,1],[1,2,-2],[2,0,-1],[3,4,-3],[4,5,-4],[5,3,-2]]
        source = 0
        self.assertEqual(self.solution.bellmanFord(n, edges, source), [-1])

if __name__ == '__main__':
    unittest.main() 