"""
Problem Statement:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Input Format:
- word1: str - First string
- word2: str - Second string

Output Format:
- int - Minimum number of operations required

Example:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

Time Complexity: O(m * n) where m and n are the lengths of word1 and word2
Space Complexity: O(m * n)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Find the minimum number of operations required to convert word1 to word2.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        word1 = "horse"
        word2 = "ros"
        self.assertEqual(self.solution.minDistance(word1, word2), 3)
    
    def test_example2(self):
        word1 = "intention"
        word2 = "execution"
        self.assertEqual(self.solution.minDistance(word1, word2), 5)
    
    def test_empty_strings(self):
        word1 = ""
        word2 = ""
        self.assertEqual(self.solution.minDistance(word1, word2), 0)
    
    def test_one_empty_string(self):
        word1 = "abc"
        word2 = ""
        self.assertEqual(self.solution.minDistance(word1, word2), 3)
    
    def test_same_strings(self):
        word1 = "abc"
        word2 = "abc"
        self.assertEqual(self.solution.minDistance(word1, word2), 0)
    
    def test_single_character(self):
        word1 = "a"
        word2 = "b"
        self.assertEqual(self.solution.minDistance(word1, word2), 1)
    
    def test_all_insertions(self):
        word1 = ""
        word2 = "abc"
        self.assertEqual(self.solution.minDistance(word1, word2), 3)
    
    def test_all_deletions(self):
        word1 = "abc"
        word2 = ""
        self.assertEqual(self.solution.minDistance(word1, word2), 3)
    
    def test_all_replacements(self):
        word1 = "abc"
        word2 = "def"
        self.assertEqual(self.solution.minDistance(word1, word2), 3)
    
    def test_mixed_operations(self):
        word1 = "abcd"
        word2 = "bce"
        self.assertEqual(self.solution.minDistance(word1, word2), 2)
    
    def test_long_strings(self):
        word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
        word2 = "pneumonoultramicroscopicsilicovolcanoconioses"
        self.assertEqual(self.solution.minDistance(word1, word2), 1)

if __name__ == '__main__':
    unittest.main() 