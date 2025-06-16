"""
Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input Format:
- strs: List[str] - Array of strings to group

Output Format:
- List[List[str]] - List of groups of anagrams

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Time Complexity: O(n * k * log k) where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n * k)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from the input array of strings.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = self.solution.groupAnagrams(strs)
        # Sort each group and the overall result for consistent comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [["bat"], ["nat","tan"], ["ate","eat","tea"]]
        expected = [sorted(group) for group in expected]
        expected.sort()
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [[""]])
    
    def test_single_character(self):
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [["a"]])
    
    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        result = self.solution.groupAnagrams(strs)
        # Sort each group and the overall result for consistent comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [["abc"], ["def"], ["ghi"]]
        expected = [sorted(group) for group in expected]
        expected.sort()
        self.assertEqual(result, expected)
    
    def test_all_same_word(self):
        strs = ["abc", "abc", "abc"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [["abc", "abc", "abc"]])
    
    def test_empty_input(self):
        strs = []
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [])
    
    def test_single_letter_words(self):
        strs = ["a", "b", "c", "a", "b"]
        result = self.solution.groupAnagrams(strs)
        # Sort each group and the overall result for consistent comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [["a", "a"], ["b", "b"], ["c"]]
        expected = [sorted(group) for group in expected]
        expected.sort()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 