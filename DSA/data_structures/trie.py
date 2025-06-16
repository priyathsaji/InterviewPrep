"""
Trie (Prefix Tree) Implementation

A trie is a tree-like data structure used to store strings. Each node represents a character,
and the path from root to any node represents a prefix of some string.

Time Complexity:
- Insert: O(m) where m is the length of the string
- Search: O(m) where m is the length of the string
- Delete: O(m) where m is the length of the string
- Prefix Search: O(m) where m is the length of the prefix

Space Complexity: O(ALPHABET_SIZE * N * M) where:
- ALPHABET_SIZE is the number of possible characters
- N is the number of strings
- M is the average length of strings
"""

from typing import Dict, List, Optional
import unittest

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: The word to be inserted
        """
        raise NotImplementedError("Trie implementation not completed")
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        
        Args:
            word: The word to search for
            
        Returns:
            True if the word is found, False otherwise
        """
        raise NotImplementedError("Trie implementation not completed")
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            True if there is any word with the given prefix, False otherwise
        """
        raise NotImplementedError("Trie implementation not completed")
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie.
        
        Args:
            word: The word to be deleted
            
        Returns:
            True if the word was found and deleted, False otherwise
        """
        raise NotImplementedError("Trie implementation not completed")
    
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in the trie.
        
        Returns:
            A list of all words in the trie
        """
        raise NotImplementedError("Trie implementation not completed")


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
    
    def test_empty_trie(self):
        self.assertFalse(self.trie.search(""))
        self.assertFalse(self.trie.starts_with(""))
        self.assertEqual(self.trie.get_all_words(), [])
    
    def test_insert_and_search(self):
        self.trie.insert("hello")
        self.trie.insert("world")
        self.trie.insert("help")
        
        self.assertTrue(self.trie.search("hello"))
        self.assertTrue(self.trie.search("world"))
        self.assertTrue(self.trie.search("help"))
        self.assertFalse(self.trie.search("hel"))
        self.assertFalse(self.trie.search("hell"))
    
    def test_starts_with(self):
        self.trie.insert("hello")
        self.trie.insert("help")
        self.trie.insert("world")
        
        self.assertTrue(self.trie.starts_with("hel"))
        self.assertTrue(self.trie.starts_with("wor"))
        self.assertFalse(self.trie.starts_with("xyz"))
    
    def test_delete(self):
        self.trie.insert("hello")
        self.trie.insert("help")
        
        self.assertTrue(self.trie.delete("hello"))
        self.assertFalse(self.trie.search("hello"))
        self.assertTrue(self.trie.search("help"))
        self.assertFalse(self.trie.delete("xyz"))
    
    def test_get_all_words(self):
        words = ["hello", "help", "world"]
        for word in words:
            self.trie.insert(word)
        
        result = self.trie.get_all_words()
        self.assertEqual(sorted(result), sorted(words))


if __name__ == '__main__':
    unittest.main() 