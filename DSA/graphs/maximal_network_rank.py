"""
Problem Statement:
There is an infrastructure of n cities with some number of roads connecting them. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input Format:
- n: int - Number of cities
- roads: List[List[int]] - List of roads [city1, city2]

Output Format:
- int - Maximal network rank

Example:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1.
The network rank of cities 0 and 2 is 3 as there are 3 roads that are connected to either 0 or 2.
The network rank of cities 0 and 3 is 4 as there are 4 roads that are connected to either 0 or 3.
The network rank of cities 1 and 2 is 3 as there are 3 roads that are connected to either 1 or 2.
The network rank of cities 1 and 3 is 4 as there are 4 roads that are connected to either 1 or 3.
The network rank of cities 2 and 3 is 3 as there are 3 roads that are connected to either 2 or 3.
The maximal network rank is 4.

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: The network rank of cities 1 and 2 is 5 as there are 5 roads that are connected to either 1 or 2.

Constraints:
- 2 <= n <= 100
- 0 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 2
- 0 <= ai, bi <= n-1
- ai != bi
- Each pair of cities has at most one road connecting them.

Time Complexity: O(n^2) where n is the number of cities
Space Complexity: O(n^2)
"""

from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        Return the maximal network rank of the infrastructure.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 4
        roads = [[0,1],[0,3],[1,2],[1,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 4)
    
    def test_example2(self):
        n = 5
        roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 5)
    
    def test_no_roads(self):
        n = 3
        roads = []
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 0)
    
    def test_single_road(self):
        n = 2
        roads = [[0,1]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 1)
    
    def test_complete_graph(self):
        n = 4
        roads = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 3)
    
    def test_star_graph(self):
        n = 4
        roads = [[0,1],[0,2],[0,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_line_graph(self):
        n = 4
        roads = [[0,1],[1,2],[2,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_disconnected_graph(self):
        n = 4
        roads = [[0,1],[2,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 1)
    
    def test_minimum_size(self):
        n = 2
        roads = [[0,1]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 1)
    
    def test_maximum_size(self):
        n = 100
        roads = [[i,i+1] for i in range(n-1)]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_cycle(self):
        n = 4
        roads = [[0,1],[1,2],[2,3],[3,0]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_multiple_cycles(self):
        n = 6
        roads = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[1,3]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 4)
    
    def test_self_loop(self):
        n = 3
        roads = [[0,1],[1,1],[1,2]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_parallel_edges(self):
        n = 3
        roads = [[0,1],[0,1],[1,2]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 2)
    
    def test_complex_graph(self):
        n = 6
        roads = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3],[3,4],[4,5]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 5)
    
    def test_sparse_graph(self):
        n = 10
        roads = [[0,1],[2,3],[4,5],[6,7],[8,9]]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 1)
    
    def test_dense_graph(self):
        n = 5
        roads = [[i,j] for i in range(n) for j in range(i+1,n)]
        self.assertEqual(self.solution.maximalNetworkRank(n, roads), 3)

if __name__ == '__main__':
    unittest.main() 