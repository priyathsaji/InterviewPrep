"""
Floyd-Warshall Algorithm

The Floyd-Warshall algorithm finds shortest paths between all pairs of vertices
in a weighted graph. It can handle negative edge weights and detect negative cycles.

Time Complexity:
- O(V^3) where V is number of vertices

Space Complexity:
- O(V^2) for distance and next vertex matrices

Applications:
1. All-pairs shortest paths
2. Transitive closure
3. Negative cycle detection
4. Network routing
"""

from typing import Dict, List, Set, Tuple, Optional
import unittest

def floyd_warshall(graph: Dict[int, List[Tuple[int, float]]]) -> Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, Optional[int]]]]:
    """
    Find shortest paths between all pairs of vertices.
    
    Args:
        graph: Adjacency list representation with edge weights
        
    Returns:
        Tuple of (distances, next_vertices)
        distances: Dictionary mapping (i, j) to shortest distance from i to j
        next_vertices: Dictionary mapping (i, j) to next vertex in shortest path from i to j
        
    Example:
        >>> graph = {0: [(1, 4), (2, 2)], 1: [(2, 1), (3, 5)], 2: [(1, 1), (3, 8)], 3: []}
        >>> distances, next_vertices = floyd_warshall(graph)
        >>> distances[0][3]
        8
    """
    raise NotImplementedError("Floyd-Warshall algorithm implementation not completed")

def get_shortest_path(next_vertices: Dict[int, Dict[int, Optional[int]]], start: int, end: int) -> Optional[List[int]]:
    """
    Reconstruct the shortest path from start to end using next_vertices.
    
    Args:
        next_vertices: Dictionary mapping (i, j) to next vertex in shortest path
        start: Starting vertex
        end: Target vertex
        
    Returns:
        List of vertices forming the shortest path if found, None otherwise
        
    Example:
        >>> next_vertices = {0: {1: 1, 2: 2, 3: 1}, 1: {2: 2, 3: 3}, 2: {1: 1, 3: 3}, 3: {}}
        >>> get_shortest_path(next_vertices, 0, 3)
        [0, 1, 3]
    """
    raise NotImplementedError("Shortest path reconstruction implementation not completed")

def detect_negative_cycle(distances: Dict[int, Dict[int, float]]) -> bool:
    """
    Detect if the graph contains a negative cycle.
    
    Args:
        distances: Dictionary mapping (i, j) to shortest distance from i to j
        
    Returns:
        True if negative cycle exists, False otherwise
        
    Example:
        >>> distances = {0: {0: 0, 1: 1}, 1: {0: -1, 1: 0}}
        >>> detect_negative_cycle(distances)
        True
    """
    raise NotImplementedError("Negative cycle detection implementation not completed")


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(2, 1), (3, 5)],
            2: [(1, 1), (3, 8)],
            3: []
        }
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances[0][3], 8)
        self.assertEqual(distances[1][3], 5)
        self.assertEqual(distances[2][3], 8)
        
        graph = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 5)],
            2: [(3, 1)],
            3: []
        }
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances[0][3], 4)
        self.assertEqual(distances[1][3], 3)
        self.assertEqual(distances[2][3], 1)
    
    def test_get_shortest_path(self):
        next_vertices = {
            0: {1: 1, 2: 2, 3: 1},
            1: {2: 2, 3: 3},
            2: {1: 1, 3: 3},
            3: {}
        }
        path = get_shortest_path(next_vertices, 0, 3)
        self.assertEqual(path, [0, 1, 3])
        
        next_vertices = {
            0: {1: 1, 2: 1, 3: 1},
            1: {2: 2, 3: 2},
            2: {3: 3},
            3: {}
        }
        path = get_shortest_path(next_vertices, 0, 3)
        self.assertEqual(path, [0, 1, 2, 3])
        
        next_vertices = {
            0: {1: None, 2: None, 3: None},
            1: {2: None, 3: None},
            2: {3: None},
            3: {}
        }
        path = get_shortest_path(next_vertices, 0, 3)
        self.assertIsNone(path)
    
    def test_detect_negative_cycle(self):
        # Graph with negative cycle
        distances = {
            0: {0: 0, 1: 1},
            1: {0: -1, 1: 0}
        }
        self.assertTrue(detect_negative_cycle(distances))
        
        # Graph without negative cycle
        distances = {
            0: {0: 0, 1: 1},
            1: {0: 1, 1: 0}
        }
        self.assertFalse(detect_negative_cycle(distances))
        
        # Graph with negative edges but no negative cycle
        distances = {
            0: {0: 0, 1: -1, 2: -2, 3: -3},
            1: {0: float('inf'), 1: 0, 2: -1, 3: -2},
            2: {0: float('inf'), 1: float('inf'), 2: 0, 3: -1},
            3: {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: 0}
        }
        self.assertFalse(detect_negative_cycle(distances))
    
    def test_empty_graph(self):
        graph = {}
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances, {})
        self.assertEqual(next_vertices, {})
        
        self.assertFalse(detect_negative_cycle(distances))
    
    def test_single_vertex(self):
        graph = {0: []}
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances, {0: {0: 0}})
        self.assertEqual(next_vertices, {0: {0: None}})
        
        self.assertFalse(detect_negative_cycle(distances))
    
    def test_disconnected_graph(self):
        graph = {0: [(1, 1)], 1: [(0, 1)], 2: [(3, 1)], 3: [(2, 1)]}
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances[0][3], float('inf'))
        self.assertEqual(distances[2][0], float('inf'))
        
        self.assertFalse(detect_negative_cycle(distances))
    
    def test_negative_weights_no_cycle(self):
        graph = {
            0: [(1, -1)],
            1: [(2, -2)],
            2: [(3, -3)],
            3: []
        }
        distances, next_vertices = floyd_warshall(graph)
        self.assertEqual(distances[0][3], -6)
        self.assertEqual(distances[1][3], -5)
        self.assertEqual(distances[2][3], -3)
        
        self.assertFalse(detect_negative_cycle(distances))


if __name__ == '__main__':
    unittest.main() 