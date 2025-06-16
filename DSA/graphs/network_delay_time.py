"""
Problem Statement:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input Format:
- times: List[List[int]] - List of directed edges (ui, vi, wi)
- n: int - Number of nodes
- k: int - Starting node

Output Format:
- int - Minimum time for all nodes to receive signal, or -1 if impossible

Example:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation:
The network is:
2 -> 1 (time 1)
2 -> 3 (time 1)
3 -> 4 (time 1)
Starting from node 2, it takes 1 time unit to reach node 1, and 2 time units to reach node 4.

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Explanation:
The network is:
1 -> 2 (time 1)
Starting from node 1, it takes 1 time unit to reach node 2.

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique

Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices
Space Complexity: O(V) where V is the number of vertices
"""

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Return the minimum time it takes for all nodes to receive the signal.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)
    
    def test_example2(self):
        times = [[1,2,1]]
        n = 2
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 1)
    
    def test_single_node(self):
        times = []
        n = 1
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 0)
    
    def test_disconnected_graph(self):
        times = [[1,2,1]]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -1)
    
    def test_multiple_paths(self):
        times = [[1,2,1],[1,3,2],[2,4,2],[3,4,1]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 3)
    
    def test_cycle(self):
        times = [[1,2,1],[2,3,1],[3,1,1]]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)
    
    def test_large_weights(self):
        times = [[1,2,100],[2,3,100],[3,4,100]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 300)
    
    def test_multiple_edges(self):
        times = [[1,2,1],[1,2,2],[1,2,3]]
        n = 2
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 1)
    
    def test_complex_graph(self):
        times = [
            [1,2,1],[1,3,2],[2,4,2],[3,4,1],
            [4,5,1],[4,6,2],[5,7,1],[6,7,2]
        ]
        n = 7
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 4)
    
    def test_negative_weights(self):
        times = [[1,2,-1],[2,3,-2],[3,4,-3]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -6)
    
    def test_self_loop(self):
        times = [[1,1,1],[1,2,1]]
        n = 2
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 1)
    
    def test_maximum_constraints(self):
        times = [[i,i+1,1] for i in range(1,100)]
        n = 100
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 99)
    
    def test_zero_weight(self):
        times = [[1,2,0],[2,3,0],[3,4,0]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 0)
    
    def test_unreachable_node(self):
        times = [[1,2,1],[3,4,1]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -1)

if __name__ == '__main__':
    unittest.main() 