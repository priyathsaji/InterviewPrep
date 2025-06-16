"""
Problem Statement:
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Input Format:
- graph: List[List[int]] - Adjacency list representation of the graph

Output Format:
- int - Length of the shortest path that visits every node

Example:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:
- n == len(graph)
- 1 <= n <= 12
- 0 <= graph[i][j] < n
- graph[i][j] != i
- All the elements of graph[i] are unique
- The input graph is guaranteed to be connected

Time Complexity: O(n * 2^n) where n is the number of nodes
Space Complexity: O(n * 2^n) where n is the number of nodes
"""

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        """
        Find the length of the shortest path that visits every node.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        graph = [[1,2,3],[0],[0],[0]]
        self.assertEqual(self.solution.shortestPathLength(graph), 4)
    
    def test_example2(self):
        graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
        self.assertEqual(self.solution.shortestPathLength(graph), 4)
    
    def test_single_node(self):
        graph = [[]]
        self.assertEqual(self.solution.shortestPathLength(graph), 0)
    
    def test_two_nodes(self):
        graph = [[1],[0]]
        self.assertEqual(self.solution.shortestPathLength(graph), 1)
    
    def test_three_nodes_line(self):
        graph = [[1],[0,2],[1]]
        self.assertEqual(self.solution.shortestPathLength(graph), 2)
    
    def test_three_nodes_triangle(self):
        graph = [[1,2],[0,2],[0,1]]
        self.assertEqual(self.solution.shortestPathLength(graph), 2)
    
    def test_four_nodes_square(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertEqual(self.solution.shortestPathLength(graph), 3)
    
    def test_four_nodes_star(self):
        graph = [[1,2,3],[0],[0],[0]]
        self.assertEqual(self.solution.shortestPathLength(graph), 3)
    
    def test_five_nodes_complete(self):
        graph = [[1,2,3,4],[0,2,3,4],[0,1,3,4],[0,1,2,4],[0,1,2,3]]
        self.assertEqual(self.solution.shortestPathLength(graph), 4)
    
    def test_six_nodes_cycle(self):
        graph = [[1,5],[0,2],[1,3],[2,4],[3,5],[4,0]]
        self.assertEqual(self.solution.shortestPathLength(graph), 5)
    
    def test_seven_nodes_tree(self):
        graph = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]
        self.assertEqual(self.solution.shortestPathLength(graph), 6)
    
    def test_eight_nodes_grid(self):
        graph = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
        self.assertEqual(self.solution.shortestPathLength(graph), 8)

if __name__ == '__main__':
    unittest.main() 