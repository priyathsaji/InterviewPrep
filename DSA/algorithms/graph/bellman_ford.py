"""
Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a source vertex to all other
vertices in a weighted graph. Unlike Dijkstra's algorithm, it can handle negative
edge weights and detect negative cycles.

Time Complexity:
- O(VE) where V is number of vertices and E is number of edges

Space Complexity:
- O(V) for distance and previous vertex arrays

Applications:
1. Network routing with negative costs
2. Currency arbitrage detection
3. Game theory
4. Negative cycle detection
"""

from typing import Dict, List, Set, Tuple, Optional
import unittest

def bellman_ford(graph: Dict[int, List[Tuple[int, float]]], start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]], bool]:
    """
    Find shortest paths from start vertex to all other vertices.
    
    Args:
        graph: Adjacency list representation with edge weights
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices, has_negative_cycle)
        distances: Dictionary mapping vertices to their shortest distance from start
        previous_vertices: Dictionary mapping vertices to their previous vertex in shortest path
        has_negative_cycle: True if graph contains negative cycle, False otherwise
        
    Example:
        >>> graph = {0: [(1, 4), (2, 2)], 1: [(2, 1), (3, 5)], 2: [(1, 1), (3, 8)], 3: []}
        >>> distances, prev, has_cycle = bellman_ford(graph, 0)
        >>> distances
        {0: 0, 1: 3, 2: 2, 3: 8}
        >>> has_cycle
        False
    """
    raise NotImplementedError("Bellman-Ford algorithm implementation not completed")

def get_shortest_path(previous_vertices: Dict[int, Optional[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Reconstruct the shortest path from start to end using previous_vertices.
    
    Args:
        previous_vertices: Dictionary mapping vertices to their previous vertex
        start: Starting vertex
        end: Target vertex
        
    Returns:
        List of vertices forming the shortest path if found, None otherwise
        
    Example:
        >>> prev = {0: None, 1: 0, 2: 1, 3: 1}
        >>> get_shortest_path(prev, 0, 3)
        [0, 1, 3]
    """
    raise NotImplementedError("Shortest path reconstruction implementation not completed")

def detect_negative_cycle(graph: Dict[int, List[Tuple[int, float]]]) -> bool:
    """
    Detect if the graph contains a negative cycle.
    
    Args:
        graph: Adjacency list representation with edge weights
        
    Returns:
        True if negative cycle exists, False otherwise
        
    Example:
        >>> graph = {0: [(1, 1)], 1: [(2, 2)], 2: [(0, -4)]}
        >>> detect_negative_cycle(graph)
        True
    """
    raise NotImplementedError("Negative cycle detection implementation not completed")


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(2, 1), (3, 5)],
            2: [(1, 1), (3, 8)],
            3: []
        }
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 3, 2: 2, 3: 8})
        self.assertEqual(prev, {0: None, 1: 2, 2: 0, 3: 1})
        self.assertFalse(has_cycle)
        
        graph = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 5)],
            2: [(3, 1)],
            3: []
        }
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 1, 2: 3, 3: 4})
        self.assertEqual(prev, {0: None, 1: 0, 2: 1, 3: 2})
        self.assertFalse(has_cycle)
    
    def test_get_shortest_path(self):
        prev = {0: None, 1: 0, 2: 1, 3: 1}
        path = get_shortest_path(prev, 0, 3)
        self.assertEqual(path, [0, 1, 3])
        
        prev = {0: None, 1: 0, 2: 1, 3: 2}
        path = get_shortest_path(prev, 0, 3)
        self.assertEqual(path, [0, 1, 2, 3])
        
        prev = {0: None, 1: None, 2: None, 3: None}
        path = get_shortest_path(prev, 0, 3)
        self.assertIsNone(path)
    
    def test_detect_negative_cycle(self):
        # Graph with negative cycle
        graph = {
            0: [(1, 1)],
            1: [(2, 2)],
            2: [(0, -4)]
        }
        self.assertTrue(detect_negative_cycle(graph))
        
        # Graph without negative cycle
        graph = {
            0: [(1, 1)],
            1: [(2, 2)],
            2: [(0, 1)]
        }
        self.assertFalse(detect_negative_cycle(graph))
        
        # Graph with negative edges but no negative cycle
        graph = {
            0: [(1, -1)],
            1: [(2, -2)],
            2: [(3, -3)],
            3: []
        }
        self.assertFalse(detect_negative_cycle(graph))
    
    def test_empty_graph(self):
        graph = {}
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {})
        self.assertEqual(prev, {})
        self.assertFalse(has_cycle)
        
        self.assertFalse(detect_negative_cycle(graph))
    
    def test_single_vertex(self):
        graph = {0: []}
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {0: 0})
        self.assertEqual(prev, {0: None})
        self.assertFalse(has_cycle)
        
        self.assertFalse(detect_negative_cycle(graph))
    
    def test_disconnected_graph(self):
        graph = {0: [(1, 1)], 1: [(0, 1)], 2: [(3, 1)], 3: [(2, 1)]}
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 1, 2: float('inf'), 3: float('inf')})
        self.assertFalse(has_cycle)
        
        self.assertFalse(detect_negative_cycle(graph))
    
    def test_negative_weights_no_cycle(self):
        graph = {
            0: [(1, -1)],
            1: [(2, -2)],
            2: [(3, -3)],
            3: []
        }
        distances, prev, has_cycle = bellman_ford(graph, 0)
        self.assertEqual(distances, {0: 0, 1: -1, 2: -3, 3: -6})
        self.assertFalse(has_cycle)
        
        self.assertFalse(detect_negative_cycle(graph))


if __name__ == '__main__':
    unittest.main() 