"""
Dijkstra's Algorithm for Shortest Path

Dijkstra's Algorithm is a greedy algorithm that finds the shortest paths between nodes
in a graph. It works by maintaining a set of nodes whose shortest distance from the
source is known, and iteratively selecting the node with the minimum distance.

Time Complexity:
- Best: O((V + E) log V) where V is the number of vertices and E is the number of edges
- Average: O((V + E) log V)
- Worst: O((V + E) log V)

Space Complexity:
- O(V + E) where V is the number of vertices and E is the number of edges

Characteristics:
1. Greedy approach
2. Uses priority queue for efficient node selection
3. Works with directed and undirected graphs
4. Cannot handle negative edge weights
"""

from typing import List, Tuple, Dict, Set
from heapq import heappush, heappop
import unittest

def dijkstra_shortest_path(vertices: int, edges: List[Tuple[int, int, float]], start: int) -> Tuple[List[float], List[int]]:
    """
    Find the shortest paths from a start vertex to all other vertices using Dijkstra's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        >>> distances[3] == 5
        True
    """
    raise NotImplementedError("Dijkstra's algorithm implementation not completed")

def dijkstra_shortest_path_with_constraints(vertices: int, edges: List[Tuple[int, int, float]],
                                          required_edges: List[Tuple[int, int]], start: int) -> Tuple[List[float], List[int]]:
    """
    Find the shortest paths with required edges using Dijkstra's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        required_edges: List of edges that must be included in the path
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> required = [(0, 1)]
        >>> distances, prev = dijkstra_shortest_path_with_constraints(vertices, edges, required, 0)
        >>> distances[1] == 10
        True
    """
    raise NotImplementedError("Dijkstra's algorithm with constraints implementation not completed")

def dijkstra_shortest_path_with_capacity(vertices: int, edges: List[Tuple[int, int, float, float]],
                                        capacity_constraints: Dict[int, float], start: int) -> Tuple[List[float], List[int]]:
    """
    Find the shortest paths with vertex capacity constraints using Dijkstra's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight, capacity) tuples
        capacity_constraints: Dictionary mapping vertices to their maximum capacity
        start: Starting vertex
        
    Returns:
        Tuple of (distances, previous_vertices) where:
        - distances[i] is the shortest distance from start to vertex i
        - previous_vertices[i] is the previous vertex in the shortest path to i
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        >>> constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        >>> distances, prev = dijkstra_shortest_path_with_capacity(vertices, edges, constraints, 0)
        >>> distances[3] == 5
        True
    """
    raise NotImplementedError("Dijkstra's algorithm with capacity constraints implementation not completed")

def reconstruct_path(previous_vertices: List[int], start: int, end: int) -> List[int]:
    """
    Reconstruct the shortest path from start to end using the previous_vertices array.
    
    Args:
        previous_vertices: List of previous vertices in the shortest paths
        start: Starting vertex
        end: Ending vertex
        
    Returns:
        List of vertices in the shortest path from start to end
        
    Example:
        >>> prev = [-1, 0, 0, 2]
        >>> path = reconstruct_path(prev, 0, 3)
        >>> path == [0, 2, 3]
        True
    """
    raise NotImplementedError("Path reconstruction implementation not completed")


class TestDijkstra(unittest.TestCase):
    def test_dijkstra_shortest_path(self):
        # Test with simple graph
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[3], 5)
        
        # Test with disconnected graph
        vertices = 4
        edges = [(0, 1, 10), (2, 3, 5)]
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[2], float('inf'))
        self.assertEqual(distances[3], float('inf'))
        
        # Test with single vertex
        vertices = 1
        edges = []
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        
        # Test with no edges
        vertices = 4
        edges = []
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[1], float('inf'))
    
    def test_dijkstra_shortest_path_with_constraints(self):
        # Test with simple graph and required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1)]
        distances, prev = dijkstra_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[1], 10)
        
        # Test with conflicting required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1), (0, 2), (0, 3), (1, 3)]  # Forms a cycle
        with self.assertRaises(ValueError):
            dijkstra_shortest_path_with_constraints(vertices, edges, required, 0)
        
        # Test with no required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = []
        distances, prev = dijkstra_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[3], 5)
    
    def test_dijkstra_shortest_path_with_capacity(self):
        # Test with simple graph and capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        distances, prev = dijkstra_shortest_path_with_capacity(vertices, edges, constraints, 0)
        self.assertEqual(distances[3], 5)
        
        # Test with insufficient capacity
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 1, 1: 1, 2: 1, 3: 1}  # Too restrictive
        with self.assertRaises(ValueError):
            dijkstra_shortest_path_with_capacity(vertices, edges, constraints, 0)
        
        # Test with missing capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5}  # Missing constraints for vertices 2 and 3
        with self.assertRaises(ValueError):
            dijkstra_shortest_path_with_capacity(vertices, edges, constraints, 0)
    
    def test_reconstruct_path(self):
        # Test with simple path
        prev = [-1, 0, 0, 2]
        path = reconstruct_path(prev, 0, 3)
        self.assertEqual(path, [0, 2, 3])
        
        # Test with no path
        prev = [-1, 0, 0, -1]
        path = reconstruct_path(prev, 0, 3)
        self.assertEqual(path, [])
        
        # Test with single vertex
        prev = [-1]
        path = reconstruct_path(prev, 0, 0)
        self.assertEqual(path, [0])
        
        # Test with invalid vertices
        prev = [-1, 0, 0, 2]
        with self.assertRaises(ValueError):
            reconstruct_path(prev, 0, 4)
    
    def test_edge_cases(self):
        # Test with negative edge weights
        vertices = 4
        edges = [(0, 1, -10), (0, 2, -6), (0, 3, -5), (1, 3, -15), (2, 3, -4)]
        with self.assertRaises(ValueError):
            dijkstra_shortest_path(vertices, edges, 0)
        
        # Test with zero edge weights
        vertices = 4
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (1, 3, 0), (2, 3, 0)]
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[3], 0)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, 10), (1, 1, 5), (2, 2, 6), (3, 3, 4)]
        with self.assertRaises(ValueError):
            dijkstra_shortest_path(vertices, edges, 0)
        
        # Test with duplicate edges
        vertices = 4
        edges = [(0, 1, 10), (1, 0, 10), (0, 2, 6), (2, 0, 6)]
        with self.assertRaises(ValueError):
            dijkstra_shortest_path(vertices, edges, 0)
    
    def test_performance(self):
        # Test with large graph
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        distances, prev = dijkstra_shortest_path(vertices, edges, 0)
        self.assertEqual(distances[0], 0)
        
        # Test with many required edges
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        required = [(i, i + 1) for i in range(vertices - 1)]
        distances, prev = dijkstra_shortest_path_with_constraints(vertices, edges, required, 0)
        self.assertEqual(distances[0], 0)
        
        # Test with many capacity constraints
        vertices = 1000
        edges = [(i, j, i + j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        constraints = {i: i + 1 for i in range(vertices)}
        distances, prev = dijkstra_shortest_path_with_capacity(vertices, edges, constraints, 0)
        self.assertEqual(distances[0], 0)


if __name__ == '__main__':
    unittest.main() 