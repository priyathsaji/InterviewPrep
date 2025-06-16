"""
Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input Format:
- s: str - First string
- t: str - Second string to check if it's an anagram of s

Output Format:
- bool - True if t is an anagram of s, False otherwise

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Time Complexity: O(n)
Space Complexity: O(1) since we only need to store 26 characters
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if t is an anagram of s.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_example2(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))
    
    def test_empty_strings(self):
        s = ""
        t = ""
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_different_lengths(self):
        s = "abc"
        t = "abcd"
        self.assertFalse(self.solution.isAnagram(s, t))
    
    def test_same_string(self):
        s = "hello"
        t = "hello"
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_single_character(self):
        s = "a"
        t = "a"
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_repeated_characters(self):
        s = "aabbcc"
        t = "ccbbaa"
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_case_sensitive(self):
        s = "Hello"
        t = "hello"
        self.assertFalse(self.solution.isAnagram(s, t))

if __name__ == '__main__':
    unittest.main() 