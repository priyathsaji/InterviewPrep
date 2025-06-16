"""
Problem Statement:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Input Format:
- s: str - Input string

Output Format:
- int - Number of palindromic substrings

Example:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings in s.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "abc"
        self.assertEqual(self.solution.countSubstrings(s), 3)
    
    def test_example2(self):
        s = "aaa"
        self.assertEqual(self.solution.countSubstrings(s), 6)
    
    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.countSubstrings(s), 1)
    
    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.countSubstrings(s), 0)
    
    def test_all_same_characters(self):
        s = "aaaa"
        self.assertEqual(self.solution.countSubstrings(s), 10)  # 4 single + 3 double + 2 triple + 1 quadruple
    
    def test_no_palindromes_except_singles(self):
        s = "abcdef"
        self.assertEqual(self.solution.countSubstrings(s), 6)  # Each character is a palindrome
    
    def test_even_length_palindromes(self):
        s = "abba"
        self.assertEqual(self.solution.countSubstrings(s), 6)  # 4 singles + 1 "bb" + 1 "abba"
    
    def test_odd_length_palindromes(self):
        s = "aba"
        self.assertEqual(self.solution.countSubstrings(s), 4)  # 3 singles + 1 "aba"
    
    def test_mixed_palindromes(self):
        s = "racecar"
        self.assertEqual(self.solution.countSubstrings(s), 10)  # 7 singles + 2 "cec" + 1 "racecar"
    
    def test_repeated_palindromes(self):
        s = "aaaaa"
        self.assertEqual(self.solution.countSubstrings(s), 15)  # 5 singles + 4 doubles + 3 triples + 2 quadruples + 1 quintuple

if __name__ == '__main__':
    unittest.main() 