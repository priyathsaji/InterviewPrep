"""
Problem Statement:
Given a directed graph with n vertices, determine if it has an Eulerian path or circuit.
An Eulerian path is a path that visits every edge exactly once.
An Eulerian circuit is an Eulerian path that starts and ends at the same vertex.

Input Format:
- n: int - Number of vertices
- edges: List[List[int]] - List of edges [u, v] where u and v are vertices

Output Format:
- List[int] - Eulerian path/circuit if it exists, empty list otherwise
  If multiple solutions exist, return any valid one

Example:
Input: n = 3, edges = [[0,1],[1,2],[2,0]]
Output: [0,1,2,0]
Explanation: The graph has an Eulerian circuit: 0->1->2->0

Input: n = 3, edges = [[0,1],[1,2]]
Output: [0,1,2]
Explanation: The graph has an Eulerian path: 0->1->2

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
    def findEulerianPath(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Find an Eulerian path or circuit in the graph if it exists.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_eulerian_circuit(self):
        n = 3
        edges = [[0,1],[1,2],[2,0]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
        self.assertEqual(result[0], result[-1])  # Circuit should start and end at same vertex
    
    def test_eulerian_path(self):
        n = 3
        edges = [[0,1],[1,2]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
        self.assertNotEqual(result[0], result[-1])  # Path should not be a circuit
    
    def test_no_eulerian_path(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_single_vertex(self):
        n = 1
        edges = []
        result = self.solution.findEulerianPath(n, edges)
        self.assertEqual(result, [0])
    
    def test_disconnected_graph(self):
        n = 3
        edges = [[0,1]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_cycle(self):
        n = 4
        edges = [[0,1],[1,2],[2,3],[3,0]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
        self.assertEqual(result[0], result[-1])
    
    def test_multiple_cycles(self):
        n = 6
        edges = [[0,1],[1,0],[2,3],[3,2],[4,5],[5,4]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_directed_path(self):
        n = 4
        edges = [[0,1],[1,2],[2,3]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
        self.assertEqual(result, [0,1,2,3])
    
    def test_maximum_constraints(self):
        n = 1000
        edges = [[i,i+1] for i in range(n-1)]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
    
    def test_no_edges(self):
        n = 3
        edges = []
        result = self.solution.findEulerianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_self_loops(self):
        n = 2
        edges = [[0,0],[1,1]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
    
    def test_complex_graph(self):
        n = 5
        edges = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,1]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
    
    def test_bidirectional_edges(self):
        n = 4
        edges = [[0,1],[1,0],[2,3],[3,2]]
        result = self.solution.findEulerianPath(n, edges)
        self.assertTrue(self._is_valid_eulerian_path(result, edges))
    
    def _is_valid_eulerian_path(self, path: List[int], edges: List[List[int]]) -> bool:
        """
        Helper method to validate if the path is a valid Eulerian path.
        """
        if not path:
            return False
        
        # Check if all edges are used exactly once
        used_edges = set()
        for i in range(len(path)-1):
            edge = (path[i], path[i+1])
            if edge in used_edges:
                return False
            used_edges.add(edge)
        
        # Check if all edges in the graph are used
        return len(used_edges) == len(edges)

if __name__ == '__main__':
    unittest.main() 