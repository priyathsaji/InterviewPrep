"""
Problem Statement:
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected).
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Input Format:
- graph: List[List[int]] - Adjacency list representation of the graph

Output Format:
- bool - True if the graph is bipartite, False otherwise

Example:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:
- graph.length == n
- 1 <= n <= 100
- 0 <= graph[u].length < n
- 0 <= graph[u][i] <= n - 1
- graph[u] does not contain u.
- All the values of graph[u] are unique.
- If graph[u] contains v, then graph[v] contains u.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V)
"""

from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Return true if and only if the graph is bipartite.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        self.assertFalse(self.solution.isBipartite(graph))
    
    def test_example2(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_empty_graph(self):
        graph = []
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_single_node(self):
        graph = [[]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_two_nodes_connected(self):
        graph = [[1],[0]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_two_nodes_disconnected(self):
        graph = [[],[]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_three_nodes_cycle(self):
        graph = [[1,2],[0,2],[0,1]]
        self.assertFalse(self.solution.isBipartite(graph))
    
    def test_three_nodes_line(self):
        graph = [[1],[0,2],[1]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_four_nodes_square(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_four_nodes_complete(self):
        graph = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
        self.assertFalse(self.solution.isBipartite(graph))
    
    def test_disconnected_components(self):
        graph = [[1],[0],[3],[2]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_disconnected_components_with_cycle(self):
        graph = [[1],[0],[3,4],[2,4],[2,3]]
        self.assertFalse(self.solution.isBipartite(graph))
    
    def test_star_graph(self):
        graph = [[1,2,3],[0],[0],[0]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_maximum_size(self):
        graph = [[i+1] for i in range(99)] + [[]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_complex_graph(self):
        graph = [[1,2,3],[0,2],[0,1,3],[0,2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8]]
        self.assertFalse(self.solution.isBipartite(graph))
    
    def test_alternating_colors(self):
        graph = [[1],[0,2],[1,3],[2,4],[3,5],[4]]
        self.assertTrue(self.solution.isBipartite(graph))
    
    def test_odd_cycle(self):
        graph = [[1,2],[0,2],[0,1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,0]]
        self.assertFalse(self.solution.isBipartite(graph))

if __name__ == '__main__':
    unittest.main() 