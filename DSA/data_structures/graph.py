"""
Graph Implementation

A graph is a data structure that consists of a set of vertices (nodes) and a set of edges
that connect these vertices. This implementation supports both directed and undirected graphs.

Time Complexity:
- Add Vertex: O(1)
- Add Edge: O(1)
- Remove Vertex: O(V + E) where V is number of vertices and E is number of edges
- Remove Edge: O(1)
- Check if Edge Exists: O(1)
- Get Neighbors: O(1)

Space Complexity: O(V + E) where V is number of vertices and E is number of edges
"""

from typing import TypeVar, Generic, Dict, Set, List, Optional
import unittest

T = TypeVar('T')

class Graph(Generic[T]):
    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.
        
        Args:
            directed: If True, create a directed graph; if False, create an undirected graph
        """
        self._vertices: Dict[T, Set[T]] = {}
        self._directed = directed
    
    def add_vertex(self, vertex: T) -> None:
        """
        Add a vertex to the graph.
        
        Args:
            vertex: The vertex to add
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def add_edge(self, vertex1: T, vertex2: T) -> None:
        """
        Add an edge between two vertices.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            
        Raises:
            ValueError: If either vertex does not exist in the graph
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def remove_vertex(self, vertex: T) -> None:
        """
        Remove a vertex and all its edges from the graph.
        
        Args:
            vertex: The vertex to remove
            
        Raises:
            ValueError: If the vertex does not exist in the graph
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def remove_edge(self, vertex1: T, vertex2: T) -> None:
        """
        Remove an edge between two vertices.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            
        Raises:
            ValueError: If either vertex does not exist or if there is no edge between them
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def has_vertex(self, vertex: T) -> bool:
        """
        Check if a vertex exists in the graph.
        
        Args:
            vertex: The vertex to check
            
        Returns:
            True if the vertex exists, False otherwise
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def has_edge(self, vertex1: T, vertex2: T) -> bool:
        """
        Check if an edge exists between two vertices.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            
        Returns:
            True if the edge exists, False otherwise
            
        Raises:
            ValueError: If either vertex does not exist in the graph
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def get_neighbors(self, vertex: T) -> Set[T]:
        """
        Get all neighbors of a vertex.
        
        Args:
            vertex: The vertex to get neighbors for
            
        Returns:
            A set of neighboring vertices
            
        Raises:
            ValueError: If the vertex does not exist in the graph
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def get_vertices(self) -> Set[T]:
        """
        Get all vertices in the graph.
        
        Returns:
            A set of all vertices
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def get_edges(self) -> List[Tuple[T, T]]:
        """
        Get all edges in the graph.
        
        Returns:
            A list of tuples representing edges (vertex1, vertex2)
        """
        raise NotImplementedError("Graph implementation not completed")
    
    def is_directed(self) -> bool:
        """
        Check if the graph is directed.
        
        Returns:
            True if the graph is directed, False otherwise
        """
        raise NotImplementedError("Graph implementation not completed")


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.undirected_graph = Graph[int](directed=False)
        self.directed_graph = Graph[int](directed=True)
    
    def test_empty_graph(self):
        self.assertEqual(len(self.undirected_graph.get_vertices()), 0)
        self.assertEqual(len(self.undirected_graph.get_edges()), 0)
        self.assertFalse(self.undirected_graph.has_vertex(1))
    
    def test_add_vertex(self):
        self.undirected_graph.add_vertex(1)
        self.undirected_graph.add_vertex(2)
        
        self.assertTrue(self.undirected_graph.has_vertex(1))
        self.assertTrue(self.undirected_graph.has_vertex(2))
        self.assertEqual(len(self.undirected_graph.get_vertices()), 2)
    
    def test_add_edge_undirected(self):
        self.undirected_graph.add_vertex(1)
        self.undirected_graph.add_vertex(2)
        self.undirected_graph.add_edge(1, 2)
        
        self.assertTrue(self.undirected_graph.has_edge(1, 2))
        self.assertTrue(self.undirected_graph.has_edge(2, 1))
        self.assertEqual(len(self.undirected_graph.get_edges()), 2)
    
    def test_add_edge_directed(self):
        self.directed_graph.add_vertex(1)
        self.directed_graph.add_vertex(2)
        self.directed_graph.add_edge(1, 2)
        
        self.assertTrue(self.directed_graph.has_edge(1, 2))
        self.assertFalse(self.directed_graph.has_edge(2, 1))
        self.assertEqual(len(self.directed_graph.get_edges()), 1)
    
    def test_remove_vertex(self):
        self.undirected_graph.add_vertex(1)
        self.undirected_graph.add_vertex(2)
        self.undirected_graph.add_edge(1, 2)
        
        self.undirected_graph.remove_vertex(1)
        self.assertFalse(self.undirected_graph.has_vertex(1))
        self.assertFalse(self.undirected_graph.has_edge(1, 2))
        self.assertFalse(self.undirected_graph.has_edge(2, 1))
    
    def test_remove_edge(self):
        self.undirected_graph.add_vertex(1)
        self.undirected_graph.add_vertex(2)
        self.undirected_graph.add_edge(1, 2)
        
        self.undirected_graph.remove_edge(1, 2)
        self.assertFalse(self.undirected_graph.has_edge(1, 2))
        self.assertFalse(self.undirected_graph.has_edge(2, 1))
    
    def test_get_neighbors(self):
        self.undirected_graph.add_vertex(1)
        self.undirected_graph.add_vertex(2)
        self.undirected_graph.add_vertex(3)
        self.undirected_graph.add_edge(1, 2)
        self.undirected_graph.add_edge(1, 3)
        
        neighbors = self.undirected_graph.get_neighbors(1)
        self.assertEqual(neighbors, {2, 3})


if __name__ == '__main__':
    unittest.main() 