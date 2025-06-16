"""
Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest paths between nodes in a graph.
It works for graphs with non-negative edge weights.

Time Complexity:
- Using Binary Heap: O((V + E) log V)
- Using Fibonacci Heap: O(V log V + E)

Space Complexity:
- O(V) for distance and previous vertex arrays
- O(V) for priority queue

Applications:
1. GPS navigation systems
2. Network routing protocols
3. Social network analysis
4. Game development (pathfinding)
"""

from typing import Dict, List, Set, Tuple, Optional
import heapq
import unittest

def dijkstra(graph: Dict[int, List[Tuple[int, float]]], start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Find shortest paths from start vertex to all other vertices.
    
    Args:
        graph: Adjacency list representation with edge weights
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices)
        distances: Dictionary mapping vertices to their shortest distance from start
        previous_vertices: Dictionary mapping vertices to their previous vertex in shortest path
        
    Example:
        >>> graph = {0: [(1, 4), (2, 2)], 1: [(2, 1), (3, 5)], 2: [(1, 1), (3, 8)], 3: []}
        >>> distances, prev = dijkstra(graph, 0)
        >>> distances
        {0: 0, 1: 3, 2: 2, 3: 8}
    """
    raise NotImplementedError("Dijkstra's algorithm implementation not completed")

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

def dijkstra_with_target(graph: Dict[int, List[Tuple[int, float]]], start: int, end: int) -> Optional[Tuple[float, List[int]]]:
    """
    Find shortest path from start to end vertex.
    
    Args:
        graph: Adjacency list representation with edge weights
        start: Starting vertex
        end: Target vertex
        
    Returns:
        Tuple of (distance, path) if path exists, None otherwise
        distance: Shortest distance from start to end
        path: List of vertices forming the shortest path
        
    Example:
        >>> graph = {0: [(1, 4), (2, 2)], 1: [(2, 1), (3, 5)], 2: [(1, 1), (3, 8)], 3: []}
        >>> distance, path = dijkstra_with_target(graph, 0, 3)
        >>> distance
        8
        >>> path
        [0, 1, 3]
    """
    raise NotImplementedError("Dijkstra's algorithm with target implementation not completed")


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(2, 1), (3, 5)],
            2: [(1, 1), (3, 8)],
            3: []
        }
        distances, prev = dijkstra(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 3, 2: 2, 3: 8})
        self.assertEqual(prev, {0: None, 1: 2, 2: 0, 3: 1})
        
        graph = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 5)],
            2: [(3, 1)],
            3: []
        }
        distances, prev = dijkstra(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 1, 2: 3, 3: 4})
        self.assertEqual(prev, {0: None, 1: 0, 2: 1, 3: 2})
    
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
    
    def test_dijkstra_with_target(self):
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(2, 1), (3, 5)],
            2: [(1, 1), (3, 8)],
            3: []
        }
        distance, path = dijkstra_with_target(graph, 0, 3)
        self.assertEqual(distance, 8)
        self.assertEqual(path, [0, 1, 3])
        
        graph = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 5)],
            2: [(3, 1)],
            3: []
        }
        distance, path = dijkstra_with_target(graph, 0, 3)
        self.assertEqual(distance, 4)
        self.assertEqual(path, [0, 1, 2, 3])
    
    def test_empty_graph(self):
        graph = {}
        distances, prev = dijkstra(graph, 0)
        self.assertEqual(distances, {})
        self.assertEqual(prev, {})
        
        result = dijkstra_with_target(graph, 0, 1)
        self.assertIsNone(result)
    
    def test_single_vertex(self):
        graph = {0: []}
        distances, prev = dijkstra(graph, 0)
        self.assertEqual(distances, {0: 0})
        self.assertEqual(prev, {0: None})
        
        distance, path = dijkstra_with_target(graph, 0, 0)
        self.assertEqual(distance, 0)
        self.assertEqual(path, [0])
    
    def test_disconnected_graph(self):
        graph = {0: [(1, 1)], 1: [(0, 1)], 2: [(3, 1)], 3: [(2, 1)]}
        distances, prev = dijkstra(graph, 0)
        self.assertEqual(distances, {0: 0, 1: 1, 2: float('inf'), 3: float('inf')})
        
        result = dijkstra_with_target(graph, 0, 3)
        self.assertIsNone(result)
    
    def test_negative_weights(self):
        graph = {0: [(1, -1)], 1: [(2, -2)], 2: [(0, -3)]}
        with self.assertRaises(ValueError):
            dijkstra(graph, 0)
        with self.assertRaises(ValueError):
            dijkstra_with_target(graph, 0, 2)


if __name__ == '__main__':
    unittest.main() 