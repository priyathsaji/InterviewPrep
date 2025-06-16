"""
Floyd-Warshall Algorithm for All-Pairs Shortest Paths

The Floyd-Warshall Algorithm is a dynamic programming algorithm that finds the shortest
paths between all pairs of vertices in a weighted graph. It can handle negative edge
weights and detect negative cycles.

Time Complexity:
- Best: O(V^3) where V is the number of vertices
- Average: O(V^3)
- Worst: O(V^3)

Space Complexity:
- O(V^2) where V is the number of vertices

Characteristics:
1. Dynamic programming approach
2. Can handle negative edge weights
3. Can detect negative cycles
4. Works with directed and undirected graphs
5. Finds shortest paths between all pairs of vertices
"""

from typing import List, Tuple, Dict, Set, Optional
import unittest

def floyd_warshall_shortest_paths(vertices: int, edges: List[Tuple[int, int, float]]) -> Tuple[List[List[float]], List[List[int]], bool]:
    """
    Find the shortest paths between all pairs of vertices using Floyd-Warshall algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        
    Returns:
        Tuple of (distances, next_vertices, has_negative_cycle) where:
        - distances[i][j] is the shortest distance from vertex i to vertex j
        - next_vertices[i][j] is the next vertex in the shortest path from i to j
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        >>> distances[0][3] == 5
        True
    """
    raise NotImplementedError("Floyd-Warshall algorithm implementation not completed")

def floyd_warshall_shortest_paths_with_constraints(vertices: int, edges: List[Tuple[int, int, float]],
                                                 required_edges: List[Tuple[int, int]]) -> Tuple[List[List[float]], List[List[int]], bool]:
    """
    Find the shortest paths between all pairs of vertices with required edges using Floyd-Warshall algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        required_edges: List of edges that must be included in the path
        
    Returns:
        Tuple of (distances, next_vertices, has_negative_cycle) where:
        - distances[i][j] is the shortest distance from vertex i to vertex j
        - next_vertices[i][j] is the next vertex in the shortest path from i to j
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> required = [(0, 1)]
        >>> distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_constraints(vertices, edges, required)
        >>> distances[0][1] == 10
        True
    """
    raise NotImplementedError("Floyd-Warshall algorithm with constraints implementation not completed")

def floyd_warshall_shortest_paths_with_capacity(vertices: int, edges: List[Tuple[int, int, float, float]],
                                              capacity_constraints: Dict[int, float]) -> Tuple[List[List[float]], List[List[int]], bool]:
    """
    Find the shortest paths between all pairs of vertices with vertex capacity constraints using Floyd-Warshall algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight, capacity) tuples
        capacity_constraints: Dictionary mapping vertices to their maximum capacity
        
    Returns:
        Tuple of (distances, next_vertices, has_negative_cycle) where:
        - distances[i][j] is the shortest distance from vertex i to vertex j
        - next_vertices[i][j] is the next vertex in the shortest path from i to j
        - has_negative_cycle is True if a negative cycle is detected
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        >>> constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        >>> distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_capacity(vertices, edges, constraints)
        >>> distances[0][3] == 5
        True
    """
    raise NotImplementedError("Floyd-Warshall algorithm with capacity constraints implementation not completed")

def find_negative_cycles(vertices: int, edges: List[Tuple[int, int, float]]) -> List[List[int]]:
    """
    Find all negative cycles in the graph using Floyd-Warshall algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        
    Returns:
        List of lists, where each inner list represents a negative cycle
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        >>> cycles = find_negative_cycles(vertices, edges)
        >>> len(cycles) > 0
        True
    """
    raise NotImplementedError("Negative cycle detection implementation not completed")


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_shortest_paths(self):
        # Test with simple graph
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertEqual(distances[0][0], 0)
        self.assertEqual(distances[0][3], 5)
        self.assertFalse(has_cycle)
        
        # Test with negative edge weights
        vertices = 4
        edges = [(0, 1, -10), (0, 2, -6), (0, 3, -5), (1, 3, -15), (2, 3, -4)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertEqual(distances[0][0], 0)
        self.assertEqual(distances[0][3], -5)
        self.assertFalse(has_cycle)
        
        # Test with negative cycle
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertTrue(has_cycle)
        
        # Test with disconnected graph
        vertices = 4
        edges = [(0, 1, 10), (2, 3, 5)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertEqual(distances[0][2], float('inf'))
        self.assertEqual(distances[0][3], float('inf'))
        self.assertFalse(has_cycle)
    
    def test_floyd_warshall_shortest_paths_with_constraints(self):
        # Test with simple graph and required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_constraints(vertices, edges, required)
        self.assertEqual(distances[0][1], 10)
        self.assertFalse(has_cycle)
        
        # Test with conflicting required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1), (0, 2), (0, 3), (1, 3)]  # Forms a cycle
        with self.assertRaises(ValueError):
            floyd_warshall_shortest_paths_with_constraints(vertices, edges, required)
        
        # Test with no required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = []
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_constraints(vertices, edges, required)
        self.assertEqual(distances[0][3], 5)
        self.assertFalse(has_cycle)
    
    def test_floyd_warshall_shortest_paths_with_capacity(self):
        # Test with simple graph and capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_capacity(vertices, edges, constraints)
        self.assertEqual(distances[0][3], 5)
        self.assertFalse(has_cycle)
        
        # Test with insufficient capacity
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 1, 1: 1, 2: 1, 3: 1}  # Too restrictive
        with self.assertRaises(ValueError):
            floyd_warshall_shortest_paths_with_capacity(vertices, edges, constraints)
        
        # Test with missing capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5}  # Missing constraints for vertices 2 and 3
        with self.assertRaises(ValueError):
            floyd_warshall_shortest_paths_with_capacity(vertices, edges, constraints)
    
    def test_find_negative_cycles(self):
        # Test with no negative cycle
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        cycles = find_negative_cycles(vertices, edges)
        self.assertEqual(len(cycles), 0)
        
        # Test with negative cycle
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7)]
        cycles = find_negative_cycles(vertices, edges)
        self.assertTrue(len(cycles) > 0)
        
        # Test with multiple negative cycles
        vertices = 4
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, -7), (1, 3, -5)]
        cycles = find_negative_cycles(vertices, edges)
        self.assertTrue(len(cycles) > 1)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, -1), (1, 1, -2), (2, 2, -3), (3, 3, -4)]
        cycles = find_negative_cycles(vertices, edges)
        self.assertEqual(len(cycles), 4)
    
    def test_edge_cases(self):
        # Test with zero edge weights
        vertices = 4
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (1, 3, 0), (2, 3, 0)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertEqual(distances[0][3], 0)
        self.assertFalse(has_cycle)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, 10), (1, 1, 5), (2, 2, 6), (3, 3, 4)]
        with self.assertRaises(ValueError):
            floyd_warshall_shortest_paths(vertices, edges)
        
        # Test with duplicate edges
        vertices = 4
        edges = [(0, 1, 10), (1, 0, 10), (0, 2, 6), (2, 0, 6)]
        with self.assertRaises(ValueError):
            floyd_warshall_shortest_paths(vertices, edges)
    
    def test_performance(self):
        # Test with large graph
        vertices = 100
        edges = [(i, j, i + j) for i in range(vertices) for j in range(vertices) if i != j]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths(vertices, edges)
        self.assertEqual(distances[0][0], 0)
        self.assertFalse(has_cycle)
        
        # Test with many required edges
        vertices = 100
        edges = [(i, j, i + j) for i in range(vertices) for j in range(vertices) if i != j]
        required = [(i, i + 1) for i in range(vertices - 1)]
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_constraints(vertices, edges, required)
        self.assertEqual(distances[0][0], 0)
        self.assertFalse(has_cycle)
        
        # Test with many capacity constraints
        vertices = 100
        edges = [(i, j, i + j, i + j) for i in range(vertices) for j in range(vertices) if i != j]
        constraints = {i: i + 1 for i in range(vertices)}
        distances, next_vertices, has_cycle = floyd_warshall_shortest_paths_with_capacity(vertices, edges, constraints)
        self.assertEqual(distances[0][0], 0)
        self.assertFalse(has_cycle)


if __name__ == '__main__':
    unittest.main() 