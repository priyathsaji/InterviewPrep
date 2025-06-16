"""
Problem Statement:
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Input Format:
- text1: str - First string
- text2: str - Second string

Output Format:
- int - Length of the longest common subsequence

Example:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Time Complexity: O(m * n) where m and n are the lengths of text1 and text2
Space Complexity: O(m * n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Find the length of the longest common subsequence between text1 and text2.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)
    
    def test_example2(self):
        text1 = "abc"
        text2 = "abc"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)
    
    def test_example3(self):
        text1 = "abc"
        text2 = "def"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)
    
    def test_empty_strings(self):
        text1 = ""
        text2 = ""
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)
    
    def test_one_empty_string(self):
        text1 = "abc"
        text2 = ""
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)
    
    def test_single_character(self):
        text1 = "a"
        text2 = "a"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 1)
    
    def test_no_common_characters(self):
        text1 = "abc"
        text2 = "def"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)
    
    def test_repeated_characters(self):
        text1 = "aabbcc"
        text2 = "abcabc"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)
    
    def test_longer_sequence(self):
        text1 = "abcdefghijklmnopqrstuvwxyz"
        text2 = "acegikmoqsuwy"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 13)
    
    def test_different_lengths(self):
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)
    
    def test_same_characters_different_order(self):
        text1 = "abc"
        text2 = "cba"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 1)

if __name__ == '__main__':
    unittest.main() 