"""
Problem Statement:
Given a directed graph with n vertices, find all strongly connected components (SCCs).
A strongly connected component is a subgraph where every vertex is reachable from every other vertex.

Input Format:
- n: int - Number of vertices
- edges: List[List[int]] - List of edges [u, v] where u and v are vertices

Output Format:
- List[List[int]] - List of strongly connected components, where each component is a list of vertices
  The components should be sorted in descending order of their size

Example:
Input: n = 5, edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
Output: [[0,1,2],[3],[4]]
Explanation: The graph has three SCCs: {0,1,2}, {3}, and {4}.

Constraints:
- 1 <= n <= 1000
- 0 <= edges.length <= 5000
- 0 <= u, v < n
- No self-loops or parallel edges

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V + E)
"""

from typing import List

class Solution:
    def findSCCs(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Find all strongly connected components in the graph using Kosaraju's algorithm.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 5
        edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(result[0]), [0,1,2])
        self.assertEqual(result[1], [3])
        self.assertEqual(result[2], [4])
    
    def test_single_vertex(self):
        n = 1
        edges = []
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(result, [[0]])
    
    def test_disconnected_graph(self):
        n = 3
        edges = []
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted([x[0] for x in result]), [0,1,2])
    
    def test_cycle(self):
        n = 4
        edges = [[0,1],[1,2],[2,3],[3,0]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), [0,1,2,3])
    
    def test_multiple_cycles(self):
        n = 6
        edges = [[0,1],[1,0],[2,3],[3,2],[4,5],[5,4]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(result[0]), [0,1])
        self.assertEqual(sorted(result[1]), [2,3])
        self.assertEqual(sorted(result[2]), [4,5])
    
    def test_directed_path(self):
        n = 4
        edges = [[0,1],[1,2],[2,3]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 4)
        self.assertEqual([x[0] for x in result], [0,1,2,3])
    
    def test_maximum_constraints(self):
        n = 1000
        edges = [[i,i+1] for i in range(n-1)]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), n)
    
    def test_no_edges(self):
        n = 3
        edges = []
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted([x[0] for x in result]), [0,1,2])
    
    def test_self_loops(self):
        n = 2
        edges = [[0,0],[1,1]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 2)
        self.assertEqual(sorted([x[0] for x in result]), [0,1])
    
    def test_complex_graph(self):
        n = 7
        edges = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3],[5,6]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(result[0]), [0,1,2])
        self.assertEqual(sorted(result[1]), [3,4,5])
        self.assertEqual(result[2], [6])
    
    def test_bidirectional_edges(self):
        n = 4
        edges = [[0,1],[1,0],[2,3],[3,2]]
        result = self.solution.findSCCs(n, edges)
        self.assertEqual(len(result), 2)
        self.assertEqual(sorted(result[0]), [0,1])
        self.assertEqual(sorted(result[1]), [2,3])

if __name__ == '__main__':
    unittest.main() 