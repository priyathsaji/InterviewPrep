"""
Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Input Format:
- s: str - A string to process

Output Format:
- int - The length of the longest substring without repeating characters

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is the size of the character set
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "abcabcbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)
    
    def test_example2(self):
        s = "bbbbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)
    
    def test_example3(self):
        s = "pwwkew"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)
    
    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)
    
    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)
    
    def test_all_unique(self):
        s = "abcdef"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 6)
    
    def test_special_characters(self):
        s = "!@#$%^&*()"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 10)
    
    def test_spaces(self):
        s = "a b c d"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 7)

if __name__ == '__main__':
    unittest.main() 