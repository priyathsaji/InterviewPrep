"""
Depth-First Search (DFS) Algorithm

DFS is an algorithm for traversing or searching tree or graph data structures.
It starts at a root node and explores as far as possible along each branch before backtracking.

Time Complexity:
- Adjacency List: O(V + E)
- Adjacency Matrix: O(V^2)

Space Complexity:
- O(V) for visited set and recursion stack

Applications:
1. Maze solving
2. Topological sorting
3. Cycle detection
4. Strongly connected components
5. Path finding
"""

from typing import Dict, List, Set, Optional
import unittest

def dfs_recursive(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Perform DFS traversal recursively.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        >>> dfs_recursive(graph, 2)
        [2, 0, 1, 3]
    """
    raise NotImplementedError("Recursive DFS implementation not completed")

def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Perform DFS traversal iteratively using a stack.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        >>> dfs_iterative(graph, 2)
        [2, 3, 0, 1]
    """
    raise NotImplementedError("Iterative DFS implementation not completed")

def dfs_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find a path from start to end using DFS.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        end: Target vertex
        
    Returns:
        List of vertices forming the path if found, None otherwise
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        >>> dfs_path(graph, 0, 3)
        [0, 2, 3]
    """
    raise NotImplementedError("DFS path finding implementation not completed")

def dfs_cycle_detection(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if the graph contains a cycle using DFS.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        True if cycle exists, False otherwise
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        >>> dfs_cycle_detection(graph)
        True
    """
    raise NotImplementedError("DFS cycle detection implementation not completed")


class TestDFS(unittest.TestCase):
    def test_dfs_recursive(self):
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        result = dfs_recursive(graph, 2)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        result = dfs_recursive(graph, 0)
        self.assertEqual(result, [0, 1, 2, 3])
    
    def test_dfs_iterative(self):
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        result = dfs_iterative(graph, 2)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
        
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        result = dfs_iterative(graph, 0)
        self.assertEqual(result, [0, 1, 2, 3])
    
    def test_dfs_path(self):
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        path = dfs_path(graph, 0, 3)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 3)
        
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        path = dfs_path(graph, 0, 3)
        self.assertEqual(path, [0, 1, 2, 3])
        
        path = dfs_path(graph, 3, 0)
        self.assertIsNone(path)
    
    def test_dfs_cycle_detection(self):
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        self.assertTrue(dfs_cycle_detection(graph))
        
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        self.assertFalse(dfs_cycle_detection(graph))
        
        graph = {0: [1], 1: [2], 2: [0]}
        self.assertTrue(dfs_cycle_detection(graph))
    
    def test_empty_graph(self):
        graph = {}
        self.assertEqual(dfs_recursive(graph, 0), [])
        self.assertEqual(dfs_iterative(graph, 0), [])
        self.assertIsNone(dfs_path(graph, 0, 1))
        self.assertFalse(dfs_cycle_detection(graph))
    
    def test_single_vertex(self):
        graph = {0: []}
        self.assertEqual(dfs_recursive(graph, 0), [0])
        self.assertEqual(dfs_iterative(graph, 0), [0])
        self.assertEqual(dfs_path(graph, 0, 0), [0])
        self.assertFalse(dfs_cycle_detection(graph))
    
    def test_disconnected_graph(self):
        graph = {0: [1], 1: [0], 2: [3], 3: [2]}
        result = dfs_recursive(graph, 0)
        self.assertEqual(len(result), 2)
        self.assertEqual(set(result), {0, 1})
        
        result = dfs_iterative(graph, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(set(result), {2, 3})
        
        self.assertIsNone(dfs_path(graph, 0, 3))
        self.assertFalse(dfs_cycle_detection(graph))


if __name__ == '__main__':
    unittest.main() 