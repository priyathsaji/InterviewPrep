"""
Problem Statement:
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Input Format:
- n: int - Number of servers
- connections: List[List[int]] - List of connections [server1, server2]

Output Format:
- List[List[int]] - List of critical connections

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
The connection [1,3] is critical because if it is removed, server 3 will be disconnected from the network.

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
Explanation: The only connection is critical.

Constraints:
- 2 <= n <= 105
- n - 1 <= connections.length <= 105
- 0 <= ai < bi < n
- ai != bi
- There are no repeated connections.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Return all critical connections in the network.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 4
        connections = [[0,1],[1,2],[2,0],[1,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), [[1,3]])
    
    def test_example2(self):
        n = 2
        connections = [[0,1]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), [[0,1]])
    
    def test_cycle(self):
        n = 3
        connections = [[0,1],[1,2],[2,0]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), [])
    
    def test_line(self):
        n = 4
        connections = [[0,1],[1,2],[2,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[0,1],[1,2],[2,3]]))
    
    def test_star(self):
        n = 4
        connections = [[0,1],[0,2],[0,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[0,1],[0,2],[0,3]]))
    
    def test_disconnected(self):
        n = 4
        connections = [[0,1],[2,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[0,1],[2,3]]))
    
    def test_complex_network(self):
        n = 6
        connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[1,3]]))
    
    def test_minimum_size(self):
        n = 2
        connections = [[0,1]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), [[0,1]])
    
    def test_maximum_size(self):
        n = 100000
        connections = [[i,i+1] for i in range(n-1)]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted(connections))
    
    def test_multiple_cycles(self):
        n = 6
        connections = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[1,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[1,3]]))
    
    def test_bridge(self):
        n = 5
        connections = [[0,1],[1,2],[2,3],[3,4],[1,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[0,1],[3,4]]))
    
    def test_complete_graph(self):
        n = 4
        connections = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), [])
    
    def test_tree(self):
        n = 5
        connections = [[0,1],[1,2],[1,3],[3,4]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted(connections))
    
    def test_self_loop(self):
        n = 3
        connections = [[0,1],[1,1],[1,2]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[0,1],[1,2]]))
    
    def test_parallel_edges(self):
        n = 3
        connections = [[0,1],[0,1],[1,2]]
        self.assertEqual(sorted(self.solution.criticalConnections(n, connections)), 
                        sorted([[1,2]]))

if __name__ == '__main__':
    unittest.main() 