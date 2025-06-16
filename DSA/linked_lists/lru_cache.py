"""
Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Input Format:
- capacity: int - The capacity of the cache
- key: int - The key to get/put
- value: int - The value to put

Output Format:
- int - The value for get operation
- None - For put operation

Example:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity)
"""

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with the given capacity.
        """
        self.cache = {}  # key -> node
        self.capacity = capacity
        self.size = 0
        
        # Initialize dummy head and tail nodes
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists, otherwise return -1.
        """
        if key not in self.cache:
            return -1
            
        # Move the accessed node to the front (most recently used)
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if it exists, otherwise add the key-value pair.
        If the number of keys exceeds capacity, evict the least recently used key.
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            # Create new node
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            
            if self.size > self.capacity:
                # Remove the least recently used node
                removed = self.removeTail()
                del self.cache[removed.key]
                self.size -= 1
    
    def addToHead(self, node: DLinkedNode) -> None:
        """
        Add a node to the front of the list.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node: DLinkedNode) -> None:
        """
        Remove a node from the list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self, node: DLinkedNode) -> None:
        """
        Move a node to the front of the list.
        """
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self) -> DLinkedNode:
        """
        Remove and return the least recently used node.
        """
        node = self.tail.prev
        self.removeNode(node)
        return node

import unittest

class TestLRUCache(unittest.TestCase):
    def test_example1(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
    
    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
    
    def test_update_existing(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 2)
        self.assertEqual(cache.get(1), 2)

if __name__ == '__main__':
    unittest.main() 