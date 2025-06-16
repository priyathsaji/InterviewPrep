"""
Topological Sort Algorithm

Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG)
such that for every directed edge (u, v), vertex u comes before v in the ordering.

Time Complexity:
- DFS-based: O(V + E)
- Kahn's algorithm: O(V + E)

Space Complexity:
- O(V) for visited set and recursion stack/queue

Applications:
1. Task scheduling
2. Build systems
3. Course prerequisites
4. Event scheduling
"""

from typing import Dict, List, Set, Optional
import unittest
from collections import deque

def topological_sort_dfs(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Perform topological sort using DFS.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        List of vertices in topological order if DAG, None if cycle exists
        
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> topological_sort_dfs(graph)
        [0, 2, 1, 3]
    """
    raise NotImplementedError("DFS-based topological sort implementation not completed")

def topological_sort_kahn(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Perform topological sort using Kahn's algorithm.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        List of vertices in topological order if DAG, None if cycle exists
        
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> topological_sort_kahn(graph)
        [0, 1, 2, 3]
    """
    raise NotImplementedError("Kahn's algorithm implementation not completed")

def find_all_topological_orders(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find all possible topological orders of the graph.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        List of all possible topological orders
        
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> find_all_topological_orders(graph)
        [[0, 1, 2, 3], [0, 2, 1, 3]]
    """
    raise NotImplementedError("All topological orders implementation not completed")


class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort_dfs(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort_dfs(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        # Verify ordering constraints
        self.assertLess(result.index(0), result.index(1))
        self.assertLess(result.index(0), result.index(2))
        self.assertLess(result.index(1), result.index(3))
        self.assertLess(result.index(2), result.index(3))
        
        # Graph with cycle
        graph = {0: [1], 1: [2], 2: [0]}
        result = topological_sort_dfs(graph)
        self.assertIsNone(result)
    
    def test_topological_sort_kahn(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort_kahn(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        # Verify ordering constraints
        self.assertLess(result.index(0), result.index(1))
        self.assertLess(result.index(0), result.index(2))
        self.assertLess(result.index(1), result.index(3))
        self.assertLess(result.index(2), result.index(3))
        
        # Graph with cycle
        graph = {0: [1], 1: [2], 2: [0]}
        result = topological_sort_kahn(graph)
        self.assertIsNone(result)
    
    def test_find_all_topological_orders(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        results = find_all_topological_orders(graph)
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertEqual(len(result), 4)
            self.assertEqual(set(result), {0, 1, 2, 3})
            # Verify ordering constraints
            self.assertLess(result.index(0), result.index(1))
            self.assertLess(result.index(0), result.index(2))
            self.assertLess(result.index(1), result.index(3))
            self.assertLess(result.index(2), result.index(3))
        
        # Graph with cycle
        graph = {0: [1], 1: [2], 2: [0]}
        results = find_all_topological_orders(graph)
        self.assertEqual(results, [])
    
    def test_empty_graph(self):
        graph = {}
        result = topological_sort_dfs(graph)
        self.assertEqual(result, [])
        
        result = topological_sort_kahn(graph)
        self.assertEqual(result, [])
        
        results = find_all_topological_orders(graph)
        self.assertEqual(results, [[]])
    
    def test_single_vertex(self):
        graph = {0: []}
        result = topological_sort_dfs(graph)
        self.assertEqual(result, [0])
        
        result = topological_sort_kahn(graph)
        self.assertEqual(result, [0])
        
        results = find_all_topological_orders(graph)
        self.assertEqual(results, [[0]])
    
    def test_disconnected_graph(self):
        graph = {0: [1], 1: [], 2: [3], 3: []}
        result = topological_sort_dfs(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        self.assertLess(result.index(0), result.index(1))
        self.assertLess(result.index(2), result.index(3))
        
        result = topological_sort_kahn(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        self.assertLess(result.index(0), result.index(1))
        self.assertLess(result.index(2), result.index(3))
        
        results = find_all_topological_orders(graph)
        self.assertEqual(len(results), 4)  # 2! * 2! = 4 possible orders


if __name__ == '__main__':
    unittest.main() 