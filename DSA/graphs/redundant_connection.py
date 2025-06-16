"""
Problem Statement:
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Input Format:
- edges: List[List[int]] - List of edges [u, v] where u and v are node labels

Output Format:
- List[int] - The edge that can be removed to form a tree

Example:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \\
2 - 3
The edge [2,3] can be removed to form a tree.

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
The edge [1,4] can be removed to form a tree.

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

Time Complexity: O(n) where n is the number of edges
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Return the edge that can be removed to form a tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        edges = [[1,2],[1,3],[2,3]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [2,3])
    
    def test_example2(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [1,4])
    
    def test_triangle(self):
        edges = [[1,2],[2,3],[3,1]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [3,1])
    
    def test_square(self):
        edges = [[1,2],[2,3],[3,4],[4,1]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [4,1])
    
    def test_line_with_cycle(self):
        edges = [[1,2],[2,3],[3,4],[4,5],[5,2]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [5,2])
    
    def test_star_with_cycle(self):
        edges = [[1,2],[1,3],[1,4],[1,5],[2,3]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [2,3])
    
    def test_multiple_cycles(self):
        edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,1],[3,7]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [3,7])
    
    def test_minimum_size(self):
        edges = [[1,2],[2,3],[3,1]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [3,1])
    
    def test_maximum_size(self):
        edges = [[i,i+1] for i in range(1,1000)] + [[1,1000]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [1,1000])
    
    def test_disconnected_components(self):
        edges = [[1,2],[2,3],[4,5],[5,6],[6,4]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [6,4])
    
    def test_complex_graph(self):
        edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],
                [10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
                [17,18],[18,19],[19,20],[20,1],[5,15]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [5,15])
    
    def test_self_loop(self):
        edges = [[1,2],[2,3],[3,3]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [3,3])
    
    def test_parallel_edges(self):
        edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],
                [10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
                [17,18],[18,19],[19,20],[20,1],[1,20]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [1,20])

if __name__ == '__main__':
    unittest.main() 