"""
Bellman-Ford Algorithm for Shortest Path

The Bellman-Ford Algorithm is a dynamic programming algorithm that finds the shortest
paths from a source vertex to all other vertices in a weighted graph. Unlike Dijkstra's
algorithm, it can handle negative edge weights and detect negative cycles.

Time Complexity:
- Best: O(VE) where V is the number of vertices and E is the number of edges
- Average: O(VE)
- Worst: O(VE)

Space Complexity:
- O(V) where V is the number of vertices

Characteristics:
1. Dynamic programming approach
2. Can handle negative edge weights
3. Can detect negative cycles
4. Works with directed and undirected graphs
"""

from typing import List, Tuple, Dict, Set, Optional
import unittest

def bellman_ford_shortest_path(vertices: int, edges: List[Tuple[int, int, float]], start: int) -> Tuple[List[float], List[int], bool]:
    """
    Find the shortest paths from a start vertex to all other vertices using Bellman-Ford algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices, has_negative_cycle) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        >>> distances[3] == 5
        True
    """
    raise NotImplementedError("Bellman-Ford algorithm implementation not completed")

def bellman_ford_shortest_path_with_constraints(vertices: int, edges: List[Tuple[int, int, float]],
                                              required_edges: List[Tuple[int, int]], start: int) -> Tuple[List[float], List[int], bool]:
    """
    Find the shortest paths with required edges using Bellman-Ford algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        required_edges: List of edges that must be included in the path
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices, has_negative_cycle) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> required = [(0, 1)]
        >>> distances, prev, has_cycle = bellman_ford_shortest_path_with_constraints(vertices, edges, required, 0)
        >>> distances[1] == 10
        True
    """
    raise NotImplementedError("Bellman-Ford algorithm with constraints implementation not completed")

def bellman_ford_shortest_path_with_capacity(vertices: int, edges: List[Tuple[int, int, float, float]],
                                           capacity_constraints: Dict[int, float], start: int) -> Tuple[List[float], List[int], bool]:
    """
    Find the shortest paths with vertex capacity constraints using Bellman-Ford algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight, capacity) tuples
        capacity_constraints: Dictionary mapping vertices to their maximum capacity
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices, has_negative_cycle) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        >>> constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        >>> distances, prev, has_cycle = bellman_ford_shortest_path_with_capacity(vertices, edges, constraints, 0)
        >>> distances[3] == 5
        True
    """
    raise NotImplementedError("Bellman-Ford algorithm with capacity constraints implementation not completed")

def find_negative_cycle(vertices: int, edges: List[Tuple[int, int, float]]) -> Optional[List[int]]:
    """
    Find a negative cycle in the graph using Bellman-Ford algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        
    Returns:
        List of vertices in the negative cycle if found, None otherwise
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        >>> cycle = find_negative_cycle(vertices, edges)
        >>> cycle is not None
        True
    """
    raise NotImplementedError("Negative cycle detection implementation not completed")


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford_shortest_path(self):
        # Test with simple graph
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[3], 5)
        self.assertFalse(has_cycle)
        
        # Test with negative edge weights
        vertices = 4
        edges = [(0, 1, -10), (0, 2, -6), (0, 3, -5), (1, 3, -15), (2, 3, -4)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[3], -5)
        self.assertFalse(has_cycle)
        
        # Test with negative cycle
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertTrue(has_cycle)
        
        # Test with disconnected graph
        vertices = 4
        edges = [(0, 1, 10), (2, 3, 5)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[2], float('inf'))
        self.assertEqual(distances[3], float('inf'))
        self.assertFalse(has_cycle)
    
    def test_bellman_ford_shortest_path_with_constraints(self):
        # Test with simple graph and required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1)]
        distances, prev, has_cycle = bellman_ford_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[1], 10)
        self.assertFalse(has_cycle)
        
        # Test with conflicting required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1), (0, 2), (0, 3), (1, 3)]  # Forms a cycle
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path_with_constraints(vertices, edges, required, 0)
        
        # Test with no required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = []
        distances, prev, has_cycle = bellman_ford_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[3], 5)
        self.assertFalse(has_cycle)
    
    def test_bellman_ford_shortest_path_with_capacity(self):
        # Test with simple graph and capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        distances, prev, has_cycle = bellman_ford_shortest_path_with_capacity(vertices, edges, constraints, 0)
        self.assertEqual(distances[3], 5)
        self.assertFalse(has_cycle)
        
        # Test with insufficient capacity
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 1, 1: 1, 2: 1, 3: 1}  # Too restrictive
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path_with_capacity(vertices, edges, constraints, 0)
        
        # Test with missing capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5}  # Missing constraints for vertices 2 and 3
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path_with_capacity(vertices, edges, constraints, 0)
    
    def test_find_negative_cycle(self):
        # Test with no negative cycle
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        cycle = find_negative_cycle(vertices, edges)
        self.assertIsNone(cycle)
        
        # Test with negative cycle
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        cycle = find_negative_cycle(vertices, edges)
        self.assertIsNotNone(cycle)
        self.assertTrue(len(cycle) > 0)
        
        # Test with multiple negative cycles
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7), (1, 3, -5)]
        cycle = find_negative_cycle(vertices, edges)
        self.assertIsNotNone(cycle)
        self.assertTrue(len(cycle) > 0)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, -1), (1, 1, -2), (2, 2, -3), (3, 3, -4)]
        cycle = find_negative_cycle(vertices, edges)
        self.assertIsNotNone(cycle)
        self.assertEqual(len(cycle), 1)
    
    def test_edge_cases(self):
        # Test with zero edge weights
        vertices = 4
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (1, 3, 0), (2, 3, 0)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[3], 0)
        self.assertFalse(has_cycle)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, 10), (1, 1, 5), (2, 2, 6), (3, 3, 4)]
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path(vertices, edges, 0)
        
        # Test with duplicate edges
        vertices = 4
        edges = [(0, 1, 10), (1, 0, 10), (0, 2, 6), (2, 0, 6)]
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path(vertices, edges, 0)
    
    def test_performance(self):
        # Test with large graph
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        distances, prev, has_cycle = bellman_ford_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        self.assertFalse(has_cycle)
        
        # Test with many required edges
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        required = [(i, i + 1) for i in range(vertices - 1)]
        distances, prev, has_cycle = bellman_ford_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[0], 0)
        self.assertFalse(has_cycle)
        
        # Test with many capacity constraints
        vertices = 1000
        edges = [(i, j, i + j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        constraints = {i: i + 1 for i in range(vertices)}
        distances, prev, has_cycle = bellman_ford_shortest_path_with_capacity(vertices, edges, constraints, 0)
        self.assertEqual(distances[0], 0)
        self.assertFalse(has_cycle)


if __name__ == '__main__':
    unittest.main() 