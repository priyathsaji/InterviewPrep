"""
Problem Statement:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode.

Input Format:
- encode: List[str] - List of strings to encode
- decode: str - Encoded string to decode

Output Format:
- encode: str - Encoded string
- decode: List[str] - Decoded list of strings

Example:
Input: strs = ["Hello", "World"]
Output: encode: "5#Hello5#World"
       decode: ["Hello", "World"]

Input: strs = [""]
Output: encode: "0#"
       decode: [""]

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

Time Complexity: O(n) where n is the total length of all strings
Space Complexity: O(n)
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        raise NotImplementedError("Solution not implemented")
    
    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        strs = ["Hello", "World"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_empty_string(self):
        strs = [""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_multiple_empty_strings(self):
        strs = ["", "", ""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_special_characters(self):
        strs = ["Hello#World", "Test@123", "Special!Chars"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_long_strings(self):
        strs = ["a" * 100, "b" * 200]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_single_character_strings(self):
        strs = ["a", "b", "c"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_mixed_length_strings(self):
        strs = ["short", "medium length", "very long string with multiple words"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_unicode_characters(self):
        strs = ["Hello", "世界", "🌍"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_numbers_in_strings(self):
        strs = ["123", "456", "789"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_spaces_in_strings(self):
        strs = ["Hello World", "  Spaces  ", "Tab\tTab"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

if __name__ == '__main__':
    unittest.main() 