"""
Problem Statement:
Implement a Trie (Prefix Tree) with insert, search, and startsWith methods.

Implement the Trie class:
- Trie() initializes the trie object.
- void insert(String word) inserts the string word into the trie.
- boolean search(String word) returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Input Format:
- word: str - The word to insert or search
- prefix: str - The prefix to check

Output Format:
- bool - True/False for search and startsWith operations

Example:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity: O(m) for all operations, where m is the length of the word/prefix
Space Complexity: O(ALPHABET_SIZE * N * M) where N is the number of words and M is the average length
"""

class TrieNode:
    def __init__(self):
        """
        Initialize a TrieNode with:
        - children: dictionary to store child nodes
        - is_end: boolean to mark if this node represents the end of a word
        """
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        raise NotImplementedError("Solution not implemented")
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        raise NotImplementedError("Solution not implemented")
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestTrie(unittest.TestCase):
    def test_example1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
    
    def test_example2(self):
        trie = Trie()
        trie.insert("hello")
        self.assertFalse(trie.search("hell"))
        self.assertTrue(trie.startsWith("hell"))
        trie.insert("hell")
        self.assertTrue(trie.search("hell"))
    
    def test_empty_string(self):
        trie = Trie()
        trie.insert("")
        self.assertTrue(trie.search(""))
        self.assertTrue(trie.startsWith(""))
    
    def test_multiple_words(self):
        trie = Trie()
        words = ["cat", "car", "dog", "do"]
        for word in words:
            trie.insert(word)
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("car"))
        self.assertTrue(trie.search("dog"))
        self.assertTrue(trie.search("do"))
        self.assertFalse(trie.search("ca"))
        self.assertTrue(trie.startsWith("ca"))
        self.assertTrue(trie.startsWith("do"))

if __name__ == '__main__':
    unittest.main() 