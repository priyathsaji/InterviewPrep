"""
Problem Statement:
Given two strings text1 and text2, return the length of their longest common subsequence.
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

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Time Complexity: O(m*n) where m and n are the lengths of text1 and text2
Space Complexity: O(m*n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Find the length of the longest common subsequence using dynamic programming.
        dp[i][j] represents the length of LCS of text1[0...i-1] and text2[0...j-1]
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

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

if __name__ == '__main__':
    unittest.main() 