"""
Prim's Algorithm for Minimum Spanning Tree

Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a
connected weighted graph. It starts with a single vertex and grows the tree by
adding the minimum weight edge that connects a vertex in the tree to a vertex
outside the tree.

Time Complexity:
- Best: O(E log V) where E is the number of edges and V is the number of vertices
- Average: O(E log V)
- Worst: O(E log V)

Space Complexity:
- O(V + E) where V is the number of vertices and E is the number of edges

Characteristics:
1. Greedy approach
2. Uses priority queue for efficient edge selection
3. Works with both directed and undirected graphs
4. Can handle negative edge weights
"""

from typing import List, Tuple, Dict, Set
from heapq import heappush, heappop
import unittest

def prim_mst(vertices: int, edges: List[Tuple[int, int, float]], start: int = 0) -> List[Tuple[int, int, float]]:
    """
    Find the minimum spanning tree using Prim's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        start: Starting vertex (default: 0)
        
    Returns:
        List of edges in the minimum spanning tree
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> mst = prim_mst(vertices, edges)
        >>> len(mst) == vertices - 1
        True
    """
    raise NotImplementedError("Prim's algorithm implementation not completed")

def prim_mst_with_constraints(vertices: int, edges: List[Tuple[int, int, float]], 
                            required_edges: List[Tuple[int, int]], start: int = 0) -> List[Tuple[int, int, float]]:
    """
    Find the minimum spanning tree with required edges using Prim's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight) tuples
        required_edges: List of edges that must be included in the MST
        start: Starting vertex (default: 0)
        
    Returns:
        List of edges in the minimum spanning tree
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        >>> required = [(0, 1)]
        >>> mst = prim_mst_with_constraints(vertices, edges, required)
        >>> (0, 1) in [(u, v) for u, v, _ in mst]
        True
    """
    raise NotImplementedError("Prim's algorithm with constraints implementation not completed")

def prim_mst_with_capacity(vertices: int, edges: List[Tuple[int, int, float, float]],
                          capacity_constraints: Dict[int, float], start: int = 0) -> List[Tuple[int, int, float]]:
    """
    Find the minimum spanning tree with vertex capacity constraints using Prim's algorithm.
    
    Args:
        vertices: Number of vertices in the graph
        edges: List of edges as (u, v, weight, capacity) tuples
        capacity_constraints: Dictionary mapping vertices to their maximum capacity
        start: Starting vertex (default: 0)
        
    Returns:
        List of edges in the minimum spanning tree
        
    Example:
        >>> vertices = 4
        >>> edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        >>> constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        >>> mst = prim_mst_with_capacity(vertices, edges, constraints)
        >>> len(mst) == vertices - 1
        True
    """
    raise NotImplementedError("Prim's algorithm with capacity constraints implementation not completed")


class TestPrim(unittest.TestCase):
    def test_prim_mst(self):
        # Test with simple graph
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        mst = prim_mst(vertices, edges)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with disconnected graph
        vertices = 4
        edges = [(0, 1, 10), (2, 3, 5)]
        with self.assertRaises(ValueError):
            prim_mst(vertices, edges)
        
        # Test with single vertex
        vertices = 1
        edges = []
        mst = prim_mst(vertices, edges)
        self.assertEqual(len(mst), 0)
        
        # Test with no edges
        vertices = 4
        edges = []
        with self.assertRaises(ValueError):
            prim_mst(vertices, edges)
        
        # Test with different start vertex
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        mst = prim_mst(vertices, edges, start=2)
        self.assertEqual(len(mst), vertices - 1)
    
    def test_prim_mst_with_constraints(self):
        # Test with simple graph and required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1)]
        mst = prim_mst_with_constraints(vertices, edges, required)
        self.assertEqual(len(mst), vertices - 1)
        self.assertTrue(any((u, v) == (0, 1) or (v, u) == (0, 1) for u, v, _ in mst))
        
        # Test with conflicting required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(0, 1), (0, 2), (0, 3), (1, 3)]  # Forms a cycle
        with self.assertRaises(ValueError):
            prim_mst_with_constraints(vertices, edges, required)
        
        # Test with no required edges
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = []
        mst = prim_mst_with_constraints(vertices, edges, required)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with different start vertex
        vertices = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        required = [(1, 3)]
        mst = prim_mst_with_constraints(vertices, edges, required, start=2)
        self.assertEqual(len(mst), vertices - 1)
    
    def test_prim_mst_with_capacity(self):
        # Test with simple graph and capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        mst = prim_mst_with_capacity(vertices, edges, constraints)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with insufficient capacity
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 1, 1: 1, 2: 1, 3: 1}  # Too restrictive
        with self.assertRaises(ValueError):
            prim_mst_with_capacity(vertices, edges, constraints)
        
        # Test with missing capacity constraints
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5}  # Missing constraints for vertices 2 and 3
        with self.assertRaises(ValueError):
            prim_mst_with_capacity(vertices, edges, constraints)
        
        # Test with different start vertex
        vertices = 4
        edges = [(0, 1, 10, 5), (0, 2, 6, 3), (0, 3, 5, 4), (1, 3, 15, 2), (2, 3, 4, 1)]
        constraints = {0: 10, 1: 5, 2: 3, 3: 4}
        mst = prim_mst_with_capacity(vertices, edges, constraints, start=2)
        self.assertEqual(len(mst), vertices - 1)
    
    def test_edge_cases(self):
        # Test with negative edge weights
        vertices = 4
        edges = [(0, 1, -10), (0, 2, -6), (0, 3, -5), (1, 3, -15), (2, 3, -4)]
        mst = prim_mst(vertices, edges)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with zero edge weights
        vertices = 4
        edges = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (1, 3, 0), (2, 3, 0)]
        mst = prim_mst(vertices, edges)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with self-loops
        vertices = 4
        edges = [(0, 0, 10), (1, 1, 5), (2, 2, 6), (3, 3, 4)]
        with self.assertRaises(ValueError):
            prim_mst(vertices, edges)
        
        # Test with duplicate edges
        vertices = 4
        edges = [(0, 1, 10), (1, 0, 10), (0, 2, 6), (2, 0, 6)]
        with self.assertRaises(ValueError):
            prim_mst(vertices, edges)
    
    def test_performance(self):
        # Test with large graph
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        mst = prim_mst(vertices, edges)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with many required edges
        vertices = 1000
        edges = [(i, j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        required = [(i, i + 1) for i in range(vertices - 1)]
        mst = prim_mst_with_constraints(vertices, edges, required)
        self.assertEqual(len(mst), vertices - 1)
        
        # Test with many capacity constraints
        vertices = 1000
        edges = [(i, j, i + j, i + j) for i in range(vertices) for j in range(i + 1, vertices)]
        constraints = {i: i + 1 for i in range(vertices)}
        mst = prim_mst_with_capacity(vertices, edges, constraints)
        self.assertEqual(len(mst), vertices - 1)


if __name__ == '__main__':
    unittest.main() 