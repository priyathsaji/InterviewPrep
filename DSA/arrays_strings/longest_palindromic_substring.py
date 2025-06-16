"""
Problem Statement:
Given a string s, return the longest palindromic substring in s.

A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

Input Format:
- s: str - Input string

Output Format:
- str - Longest palindromic substring

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid answers)

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Constraints:
- 1 <= s.length <= 1000
- s consist only of lowercase English letters.

Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in s.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])
    
    def test_example2(self):
        s = "cbbd"
        self.assertEqual(self.solution.longestPalindrome(s), "bb")
    
    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.longestPalindrome(s), "a")
    
    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.longestPalindrome(s), "")
    
    def test_all_same_characters(self):
        s = "aaaaa"
        self.assertEqual(self.solution.longestPalindrome(s), "aaaaa")
    
    def test_no_palindrome(self):
        s = "abc"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["a", "b", "c"])
    
    def test_even_length_palindrome(self):
        s = "abba"
        self.assertEqual(self.solution.longestPalindrome(s), "abba")
    
    def test_odd_length_palindrome(self):
        s = "aba"
        self.assertEqual(self.solution.longestPalindrome(s), "aba")
    
    def test_multiple_palindromes(self):
        s = "racecar"
        self.assertEqual(self.solution.longestPalindrome(s), "racecar")
    
    def test_palindrome_at_end(self):
        s = "abcdcba"
        self.assertEqual(self.solution.longestPalindrome(s), "abcdcba")
    
    def test_palindrome_at_start(self):
        s = "cbabcd"
        self.assertEqual(self.solution.longestPalindrome(s), "cbabc")

if __name__ == '__main__':
    unittest.main() 