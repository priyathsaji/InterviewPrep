"""
Binary Search Tree Implementation

A binary search tree is a binary tree where for each node:
- All nodes in its left subtree have values less than the node's value
- All nodes in its right subtree have values greater than the node's value

Time Complexity:
- Insert: O(log n) average case, O(n) worst case
- Delete: O(log n) average case, O(n) worst case
- Search: O(log n) average case, O(n) worst case
- Find Min/Max: O(log n) average case, O(n) worst case

Space Complexity: O(n) where n is the number of nodes in the tree
"""

from typing import TypeVar, Generic, Optional
import unittest

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None

class BinarySearchTree(Generic[T]):
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[Node[T]] = None
        self.size: int = 0
    
    def insert(self, data: T) -> None:
        """
        Insert a new node with the given data into the tree.
        
        Args:
            data: The data to be stored in the new node
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def delete(self, data: T) -> None:
        """
        Delete the node containing the given data from the tree.
        
        Args:
            data: The data to be deleted
            
        Raises:
            ValueError: If the data is not found in the tree
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def search(self, data: T) -> bool:
        """
        Search for a node containing the given data.
        
        Args:
            data: The data to search for
            
        Returns:
            True if the data is found, False otherwise
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def find_min(self) -> T:
        """
        Find the minimum value in the tree.
        
        Returns:
            The minimum value in the tree
            
        Raises:
            ValueError: If the tree is empty
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def find_max(self) -> T:
        """
        Find the maximum value in the tree.
        
        Returns:
            The maximum value in the tree
            
        Raises:
            ValueError: If the tree is empty
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the tree is empty.
        
        Returns:
            True if the tree is empty, False otherwise
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")
    
    def get_size(self) -> int:
        """
        Get the number of nodes in the tree.
        
        Returns:
            The number of nodes in the tree
        """
        raise NotImplementedError("Binary Search Tree implementation not completed")


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree[int]()
    
    def test_empty_tree(self):
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.get_size(), 0)
        with self.assertRaises(ValueError):
            self.bst.find_min()
        with self.assertRaises(ValueError):
            self.bst.find_max()
    
    def test_insert_and_search(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(9)
        
        self.assertEqual(self.bst.get_size(), 5)
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(3))
        self.assertTrue(self.bst.search(7))
        self.assertTrue(self.bst.search(1))
        self.assertTrue(self.bst.search(9))
        self.assertFalse(self.bst.search(4))
    
    def test_find_min_max(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(9)
        
        self.assertEqual(self.bst.find_min(), 1)
        self.assertEqual(self.bst.find_max(), 9)
    
    def test_delete(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(9)
        
        self.bst.delete(3)
        self.assertEqual(self.bst.get_size(), 4)
        self.assertFalse(self.bst.search(3))
        
        self.bst.delete(5)
        self.assertEqual(self.bst.get_size(), 3)
        self.assertFalse(self.bst.search(5))
        
        with self.assertRaises(ValueError):
            self.bst.delete(4)


if __name__ == '__main__':
    unittest.main() 