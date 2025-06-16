"""
Problem Statement:
Given a string s, return the longest palindromic substring in s.

Input Format:
- s: str - Input string

Output Format:
- str - Longest palindromic substring

Example:
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring using the expand around center approach.
        For each position in the string, we expand outwards to find palindromes of odd and even lengths.
        """
        if not s:
            return ""
            
        start = 0
        max_length = 1
        
        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            """Helper function to expand around center and find palindrome length"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Check for odd length palindromes
            left, right = expand_around_center(i, i)
            if right - left + 1 > max_length:
                max_length = right - left + 1
                start = left
            
            # Check for even length palindromes
            left, right = expand_around_center(i, i + 1)
            if right - left + 1 > max_length:
                max_length = right - left + 1
                start = left
        
        return s[start:start + max_length]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertTrue(result in ["bab", "aba"])
    
    def test_example2(self):
        s = "cbbd"
        self.assertEqual(self.solution.longestPalindrome(s), "bb")
    
    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.longestPalindrome(s), "a")
    
    def test_all_same_characters(self):
        s = "aaaa"
        self.assertEqual(self.solution.longestPalindrome(s), "aaaa")
    
    def test_no_palindrome(self):
        s = "abc"
        self.assertEqual(self.solution.longestPalindrome(s), "a")

if __name__ == '__main__':
    unittest.main() 