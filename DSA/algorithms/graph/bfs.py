"""
Breadth-First Search (BFS) Implementation

BFS is a graph traversal algorithm that explores all vertices at the present depth
before moving on to vertices at the next depth level.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V) for the queue and visited set

Applications:
1. Shortest path finding in unweighted graphs
2. Web crawling
3. Social networking (finding connections)
4. GPS navigation systems
5. Peer-to-peer networks
"""

from typing import Dict, List, Set, Optional
from collections import deque
import unittest

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Perform breadth-first search on a graph starting from a given vertex.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex for BFS
        
    Returns:
        List of vertices in the order they were visited
        
    Example:
        >>> graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        >>> bfs(graph, 0)
        [0, 1, 2, 3]
    """
    raise NotImplementedError("BFS implementation not completed")

def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between two vertices using BFS.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        end: Target vertex
        
    Returns:
        List of vertices representing the shortest path from start to end,
        or None if no path exists
        
    Example:
        >>> graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        >>> bfs_shortest_path(graph, 0, 3)
        [0, 2, 3]
    """
    raise NotImplementedError("BFS shortest path implementation not completed")

def bfs_levels(graph: Dict[int, List[int]], start: int) -> Dict[int, int]:
    """
    Find the level (distance from start) of each vertex using BFS.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        
    Returns:
        Dictionary mapping each vertex to its level (distance from start)
        
    Example:
        >>> graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        >>> bfs_levels(graph, 0)
        {0: 0, 1: 1, 2: 1, 3: 2}
    """
    raise NotImplementedError("BFS levels implementation not completed")


class TestBFS(unittest.TestCase):
    def setUp(self):
        # Create a sample graph for testing
        self.graph = {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [1, 2, 4],
            4: [3]
        }
    
    def test_bfs_traversal(self):
        result = bfs(self.graph, 0)
        # Check that all vertices are visited
        self.assertEqual(set(result), set(self.graph.keys()))
        # Check that the first vertex is the start vertex
        self.assertEqual(result[0], 0)
        # Check that vertices at the same level are visited in order
        self.assertIn(result[1:3], [[1, 2], [2, 1]])
    
    def test_bfs_shortest_path(self):
        path = bfs_shortest_path(self.graph, 0, 4)
        self.assertEqual(path, [0, 1, 3, 4])
        
        # Test when no path exists
        disconnected_graph = {0: [1], 2: [3]}
        self.assertIsNone(bfs_shortest_path(disconnected_graph, 0, 3))
    
    def test_bfs_levels(self):
        levels = bfs_levels(self.graph, 0)
        self.assertEqual(levels[0], 0)  # Start vertex
        self.assertEqual(levels[1], 1)  # First level
        self.assertEqual(levels[2], 1)  # First level
        self.assertEqual(levels[3], 2)  # Second level
        self.assertEqual(levels[4], 3)  # Third level
    
    def test_empty_graph(self):
        empty_graph = {}
        self.assertEqual(bfs(empty_graph, 0), [])
        self.assertIsNone(bfs_shortest_path(empty_graph, 0, 1))
        self.assertEqual(bfs_levels(empty_graph, 0), {})
    
    def test_single_vertex(self):
        single_vertex = {0: []}
        self.assertEqual(bfs(single_vertex, 0), [0])
        self.assertEqual(bfs_shortest_path(single_vertex, 0, 0), [0])
        self.assertEqual(bfs_levels(single_vertex, 0), {0: 0})


if __name__ == '__main__':
    unittest.main() 