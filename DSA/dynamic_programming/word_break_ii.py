"""
Problem Statement:
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input Format:
- s: str - String to be segmented
- wordDict: List[str] - List of valid words

Output Format:
- List[str] - List of all possible sentences

Example:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Explanation: Both "cats and dog" and "cat sand dog" are valid sentences.

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: All three sentences are valid.

Constraints:
- 1 <= len(s) <= 20
- 1 <= len(wordDict) <= 1000
- 1 <= len(wordDict[i]) <= 10
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

Time Complexity: O(n * 2^n) where n is the length of s
Space Complexity: O(n * 2^n) where n is the length of s
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        Find all possible sentences by breaking the string into valid words.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "catsanddog"
        wordDict = ["cat","cats","and","sand","dog"]
        expected = ["cats and dog","cat sand dog"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example2(self):
        s = "pineapplepenapple"
        wordDict = ["apple","pen","applepen","pine","pineapple"]
        expected = ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_single_word(self):
        s = "cat"
        wordDict = ["cat"]
        expected = ["cat"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_two_words(self):
        s = "catsand"
        wordDict = ["cat","sand"]
        expected = ["cat sand"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_no_solution(self):
        s = "catsandog"
        wordDict = ["cat","cats","and","sand","dog"]
        expected = []
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_multiple_solutions(self):
        s = "aaaaaaa"
        wordDict = ["a","aa","aaa"]
        expected = ["a a a a a a a","a a a a a aa","a a a a aa a","a a a aa a a","a a aa a a a","a aa a a a a","aa a a a a a","a a a aaa","a a aaa a","a aaa a a","aaa a a a","a aa aaa","aa a aaa","aaa a aa","aa aaa a","aaa aa a"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_empty_string(self):
        s = ""
        wordDict = ["cat","dog"]
        expected = [""]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_empty_dict(self):
        s = "cat"
        wordDict = []
        expected = []
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_long_string(self):
        s = "aaaaaaaaaaaaaaaaaaaa"
        wordDict = ["a","aa","aaa","aaaa"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(len(result) > 0)
    
    def test_repeated_words(self):
        s = "catcat"
        wordDict = ["cat"]
        expected = ["cat cat"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_overlapping_words(self):
        s = "aaaa"
        wordDict = ["a","aa","aaa"]
        expected = ["a a a a","a a aa","a aa a","aa a a","aa aa","aaa a","a aaa"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main() 