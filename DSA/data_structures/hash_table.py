"""
Hash Table Implementation

A hash table is a data structure that implements an associative array abstract data type,
a structure that can map keys to values. It uses a hash function to compute an index
into an array of buckets or slots, from which the desired value can be found.

Time Complexity:
- Insert: O(1) average case, O(n) worst case
- Delete: O(1) average case, O(n) worst case
- Search: O(1) average case, O(n) worst case

Space Complexity: O(n) where n is the number of key-value pairs
"""

from typing import TypeVar, Generic, Optional, List, Tuple
import unittest

K = TypeVar('K')
V = TypeVar('V')

class HashTable(Generic[K, V]):
    def __init__(self, initial_capacity: int = 10, load_factor: float = 0.75):
        """
        Initialize an empty hash table.
        
        Args:
            initial_capacity: The initial number of buckets
            load_factor: The maximum ratio of elements to buckets before resizing
        """
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._size = 0
        self._buckets: List[List[Tuple[K, V]]] = [[] for _ in range(initial_capacity)]
    
    def put(self, key: K, value: V) -> None:
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        
        Args:
            key: The key to insert
            value: The value to associate with the key
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def get(self, key: K) -> Optional[V]:
        """
        Get the value associated with the given key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key, or None if the key is not found
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def remove(self, key: K) -> Optional[V]:
        """
        Remove the key-value pair with the given key.
        
        Args:
            key: The key to remove
            
        Returns:
            The value that was associated with the key, or None if the key was not found
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def contains_key(self, key: K) -> bool:
        """
        Check if the hash table contains the given key.
        
        Args:
            key: The key to check for
            
        Returns:
            True if the key is found, False otherwise
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def size(self) -> int:
        """
        Get the number of key-value pairs in the hash table.
        
        Returns:
            The number of key-value pairs
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def is_empty(self) -> bool:
        """
        Check if the hash table is empty.
        
        Returns:
            True if the hash table is empty, False otherwise
        """
        raise NotImplementedError("Hash Table implementation not completed")
    
    def clear(self) -> None:
        """Remove all key-value pairs from the hash table."""
        raise NotImplementedError("Hash Table implementation not completed")


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable[str, int]()
    
    def test_empty_hash_table(self):
        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("key"))
        self.assertFalse(self.ht.contains_key("key"))
    
    def test_put_and_get(self):
        self.ht.put("one", 1)
        self.ht.put("two", 2)
        self.ht.put("three", 3)
        
        self.assertEqual(self.ht.size(), 3)
        self.assertEqual(self.ht.get("one"), 1)
        self.assertEqual(self.ht.get("two"), 2)
        self.assertEqual(self.ht.get("three"), 3)
        self.assertIsNone(self.ht.get("four"))
    
    def test_update_value(self):
        self.ht.put("key", 1)
        self.ht.put("key", 2)
        
        self.assertEqual(self.ht.size(), 1)
        self.assertEqual(self.ht.get("key"), 2)
    
    def test_remove(self):
        self.ht.put("one", 1)
        self.ht.put("two", 2)
        
        self.assertEqual(self.ht.remove("one"), 1)
        self.assertEqual(self.ht.size(), 1)
        self.assertIsNone(self.ht.get("one"))
        self.assertEqual(self.ht.get("two"), 2)
        
        self.assertIsNone(self.ht.remove("three"))
    
    def test_contains_key(self):
        self.ht.put("one", 1)
        
        self.assertTrue(self.ht.contains_key("one"))
        self.assertFalse(self.ht.contains_key("two"))
    
    def test_clear(self):
        self.ht.put("one", 1)
        self.ht.put("two", 2)
        
        self.ht.clear()
        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("one"))
        self.assertIsNone(self.ht.get("two"))


if __name__ == '__main__':
    unittest.main() 