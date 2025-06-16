"""
Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Input Format:
- s: str - The string to search in
- t: str - The string containing characters to find

Output Format:
- str - The minimum window substring containing all characters from t

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Time Complexity: O(m + n)
Space Complexity: O(k) where k is the number of unique characters in t
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window substring containing all characters from t.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(self.solution.minWindow(s, t), "BANC")
    
    def test_example2(self):
        s = "a"
        t = "a"
        self.assertEqual(self.solution.minWindow(s, t), "a")
    
    def test_example3(self):
        s = "a"
        t = "aa"
        self.assertEqual(self.solution.minWindow(s, t), "")
    
    def test_no_match(self):
        s = "ABCDEF"
        t = "XYZ"
        self.assertEqual(self.solution.minWindow(s, t), "")
    
    def test_exact_match(self):
        s = "ABCD"
        t = "ABCD"
        self.assertEqual(self.solution.minWindow(s, t), "ABCD")
    
    def test_multiple_matches(self):
        s = "ABBCA"
        t = "ABC"
        self.assertEqual(self.solution.minWindow(s, t), "BCA")
    
    def test_case_sensitive(self):
        s = "aBcDeF"
        t = "BcD"
        self.assertEqual(self.solution.minWindow(s, t), "BcD")
    
    def test_duplicate_characters(self):
        s = "AABBC"
        t = "ABC"
        self.assertEqual(self.solution.minWindow(s, t), "ABBC")

if __name__ == '__main__':
    unittest.main() 