"""
Problem Statement:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord is not required to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Input Format:
- beginWord: str - Starting word
- endWord: str - Target word
- wordList: List[str] - List of valid words

Output Format:
- int - Length of shortest transformation sequence, or 0 if impossible

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

Time Complexity: O(N * 26 * L) where N is the number of words and L is the length of each word
Space Complexity: O(N)
"""

from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Return the length of the shortest transformation sequence.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)
    
    def test_example2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 0)
    
    def test_same_word(self):
        beginWord = "hit"
        endWord = "hit"
        wordList = ["hot"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 1)
    
    def test_one_step(self):
        beginWord = "hit"
        endWord = "hot"
        wordList = ["hot"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 2)
    
    def test_no_path(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 0)
    
    def test_multiple_paths(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog","pot","pod"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)
    
    def test_long_words(self):
        beginWord = "abcdefghij"
        endWord = "abcdefghik"
        wordList = ["abcdefghik"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 2)
    
    def test_empty_wordlist(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = []
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 0)
    
    def test_word_not_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 0)
    
    def test_begin_word_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hit","hot","dot","dog","lot","log","cog"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)
    
    def test_maximum_length(self):
        beginWord = "a" * 10
        endWord = "b" * 10
        wordList = ["a" * 9 + "b", "a" * 8 + "bb", "a" * 7 + "bbb", "a" * 6 + "bbbb",
                   "a" * 5 + "bbbbb", "a" * 4 + "bbbbbb", "a" * 3 + "bbbbbbb",
                   "a" * 2 + "bbbbbbbb", "a" + "b" * 9, "b" * 10]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 11)
    
    def test_complex_path(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog","pot","pod","pad","pat","pit","pot"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)
    
    def test_cyclic_path(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog","hot","dot","dog","lot","log"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)
    
    def test_multiple_end_words(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog","cog","cog"]
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), 5)

if __name__ == '__main__':
    unittest.main() 