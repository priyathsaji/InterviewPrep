"""
Linked List Implementation

A linked list is a linear data structure where elements are stored in nodes,
and each node points to the next node in the sequence.

Time Complexity:
- Insert at beginning: O(1)
- Insert at end: O(n)
- Delete at beginning: O(1)
- Delete at end: O(n)
- Search: O(n)
- Access by index: O(n)

Space Complexity: O(n) where n is the number of elements in the linked list
"""

from typing import TypeVar, Generic, Optional
import unittest

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None

class LinkedList(Generic[T]):
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[Node[T]] = None
        self.size: int = 0
    
    def insert_at_beginning(self, data: T) -> None:
        """
        Insert a new node at the beginning of the linked list.
        
        Args:
            data: The data to be stored in the new node
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def insert_at_end(self, data: T) -> None:
        """
        Insert a new node at the end of the linked list.
        
        Args:
            data: The data to be stored in the new node
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def delete_at_beginning(self) -> T:
        """
        Delete the first node and return its data.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If the linked list is empty
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def delete_at_end(self) -> T:
        """
        Delete the last node and return its data.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If the linked list is empty
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def search(self, data: T) -> bool:
        """
        Search for a node containing the given data.
        
        Args:
            data: The data to search for
            
        Returns:
            True if the data is found, False otherwise
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def get_at_index(self, index: int) -> T:
        """
        Get the data at the specified index.
        
        Args:
            index: The index of the node to get
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If the index is out of range
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.
        
        Returns:
            True if the linked list is empty, False otherwise
        """
        raise NotImplementedError("Linked List implementation not completed")
    
    def get_size(self) -> int:
        """
        Get the number of nodes in the linked list.
        
        Returns:
            The number of nodes in the linked list
        """
        raise NotImplementedError("Linked List implementation not completed")


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList[int]()
    
    def test_empty_list(self):
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(self.ll.get_size(), 0)
        with self.assertRaises(IndexError):
            self.ll.delete_at_beginning()
        with self.assertRaises(IndexError):
            self.ll.delete_at_end()
        with self.assertRaises(IndexError):
            self.ll.get_at_index(0)
    
    def test_insert_at_beginning(self):
        self.ll.insert_at_beginning(1)
        self.ll.insert_at_beginning(2)
        self.ll.insert_at_beginning(3)
        
        self.assertEqual(self.ll.get_size(), 3)
        self.assertEqual(self.ll.get_at_index(0), 3)
        self.assertEqual(self.ll.get_at_index(1), 2)
        self.assertEqual(self.ll.get_at_index(2), 1)
    
    def test_insert_at_end(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        
        self.assertEqual(self.ll.get_size(), 3)
        self.assertEqual(self.ll.get_at_index(0), 1)
        self.assertEqual(self.ll.get_at_index(1), 2)
        self.assertEqual(self.ll.get_at_index(2), 3)
    
    def test_delete_at_beginning(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        
        self.assertEqual(self.ll.delete_at_beginning(), 1)
        self.assertEqual(self.ll.delete_at_beginning(), 2)
        self.assertEqual(self.ll.delete_at_beginning(), 3)
        self.assertTrue(self.ll.is_empty())
    
    def test_delete_at_end(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        
        self.assertEqual(self.ll.delete_at_end(), 3)
        self.assertEqual(self.ll.delete_at_end(), 2)
        self.assertEqual(self.ll.delete_at_end(), 1)
        self.assertTrue(self.ll.is_empty())
    
    def test_search(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        
        self.assertTrue(self.ll.search(1))
        self.assertTrue(self.ll.search(2))
        self.assertTrue(self.ll.search(3))
        self.assertFalse(self.ll.search(4))


if __name__ == '__main__':
    unittest.main() 