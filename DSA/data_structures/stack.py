"""
Stack Implementation

A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
Elements are added and removed from the same end (top) of the stack.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity: O(n) where n is the number of elements in the stack
"""

from typing import TypeVar, Generic, Optional
import unittest

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        """Initialize an empty stack."""
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> T:
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        Return the number of items in the stack.
        
        Returns:
            The number of items in the stack
        """
        return len(self._items)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack[int]()
    
    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        with self.assertRaises(IndexError):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()
    
    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())
    
    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.size(), 1)
    
    def test_generic_type(self):
        string_stack = Stack[str]()
        string_stack.push("hello")
        string_stack.push("world")
        self.assertEqual(string_stack.pop(), "world")
        self.assertEqual(string_stack.pop(), "hello")


if __name__ == '__main__':
    unittest.main() 