"""
Problem Statement:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input Format:
- s: str - A string of uppercase English letters
- k: int - Maximum number of operations allowed

Output Format:
- int - Length of the longest substring with same characters after k operations

Example:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring with same characters after k replacements.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(self.solution.characterReplacement(s, k), 4)
    
    def test_example2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(self.solution.characterReplacement(s, k), 4)
    
    def test_no_replacements(self):
        s = "AAAA"
        k = 0
        self.assertEqual(self.solution.characterReplacement(s, k), 4)
    
    def test_all_replacements(self):
        s = "ABCD"
        k = 3
        self.assertEqual(self.solution.characterReplacement(s, k), 4)
    
    def test_single_character(self):
        s = "A"
        k = 1
        self.assertEqual(self.solution.characterReplacement(s, k), 1)
    
    def test_empty_string(self):
        s = ""
        k = 1
        self.assertEqual(self.solution.characterReplacement(s, k), 0)
    
    def test_max_replacements(self):
        s = "ABCDEF"
        k = 6
        self.assertEqual(self.solution.characterReplacement(s, k), 6)

if __name__ == '__main__':
    unittest.main() 