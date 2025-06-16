"""
Problem Statement:
Given a directed graph with n vertices, determine if it has a Hamiltonian path or cycle.
A Hamiltonian path is a path that visits every vertex exactly once.
A Hamiltonian cycle is a Hamiltonian path that starts and ends at the same vertex.

Input Format:
- n: int - Number of vertices
- edges: List[List[int]] - List of edges [u, v] where u and v are vertices

Output Format:
- List[int] - Hamiltonian path/cycle if it exists, empty list otherwise
  If multiple solutions exist, return any valid one

Example:
Input: n = 4, edges = [[0,1],[1,2],[2,3],[3,0]]
Output: [0,1,2,3,0]
Explanation: The graph has a Hamiltonian cycle: 0->1->2->3->0

Input: n = 3, edges = [[0,1],[1,2]]
Output: [0,1,2]
Explanation: The graph has a Hamiltonian path: 0->1->2

Constraints:
- 1 <= n <= 20
- 0 <= edges.length <= 400
- 0 <= u, v < n
- No self-loops or parallel edges

Time Complexity: O(n!) in worst case
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findHamiltonianPath(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Find a Hamiltonian path or cycle in the graph if it exists.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_hamiltonian_cycle(self):
        n = 4
        edges = [[0,1],[1,2],[2,3],[3,0]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
        self.assertEqual(result[0], result[-1])  # Cycle should start and end at same vertex
    
    def test_hamiltonian_path(self):
        n = 3
        edges = [[0,1],[1,2]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
        self.assertNotEqual(result[0], result[-1])  # Path should not be a cycle
    
    def test_no_hamiltonian_path(self):
        n = 3
        edges = [[0,1],[0,2]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_single_vertex(self):
        n = 1
        edges = []
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [0])
    
    def test_disconnected_graph(self):
        n = 3
        edges = [[0,1]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_complete_graph(self):
        n = 4
        edges = [[i,j] for i in range(n) for j in range(n) if i != j]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
    
    def test_directed_path(self):
        n = 4
        edges = [[0,1],[1,2],[2,3]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
        self.assertEqual(result, [0,1,2,3])
    
    def test_maximum_constraints(self):
        n = 20
        edges = [[i,i+1] for i in range(n-1)]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
    
    def test_no_edges(self):
        n = 3
        edges = []
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_self_loops(self):
        n = 2
        edges = [[0,0],[1,1]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [])
    
    def test_complex_graph(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[3,4],[4,0],[0,2],[2,4]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertTrue(self._is_valid_hamiltonian_path(result, n, edges))
    
    def test_bidirectional_edges(self):
        n = 4
        edges = [[0,1],[1,0],[2,3],[3,2]]
        result = self.solution.findHamiltonianPath(n, edges)
        self.assertEqual(result, [])
    
    def _is_valid_hamiltonian_path(self, path: List[int], n: int, edges: List[List[int]]) -> bool:
        """
        Helper method to validate if the path is a valid Hamiltonian path.
        """
        if not path:
            return False
        
        # Check if all vertices are visited exactly once
        if len(set(path)) != n:
            return False
        
        # Check if all edges in the path exist in the graph
        edge_set = set(tuple(edge) for edge in edges)
        for i in range(len(path)-1):
            if (path[i], path[i+1]) not in edge_set:
                return False
        
        return True

if __name__ == '__main__':
    unittest.main() 