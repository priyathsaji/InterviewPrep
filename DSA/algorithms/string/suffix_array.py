"""
Suffix Array Implementation

A suffix array is a sorted array of all suffixes of a string. It is a data structure
that provides efficient string operations like pattern matching, finding the longest
common substring, and finding the longest repeated substring.

Time Complexity:
- Construction: O(n log n) where n is string length
- Pattern Search: O(m log n) where m is pattern length
- Longest Common Substring: O(n log n)

Space Complexity:
- O(n) for storing the suffix array and LCP array

Characteristics:
1. Space-efficient alternative to suffix trees
2. Supports efficient pattern matching
3. Can be used for various string operations
4. Requires additional LCP array for some operations
"""

from typing import List, Tuple, Optional
import unittest

def build_suffix_array(text: str) -> List[int]:
    """
    Build the suffix array for a given string.
    
    Args:
        text: The input string
        
    Returns:
        List of indices representing the sorted suffixes
        
    Example:
        >>> build_suffix_array("banana")
        [5, 3, 1, 0, 4, 2]
    """
    raise NotImplementedError("Suffix array construction not completed")

def build_lcp_array(text: str, suffix_array: List[int]) -> List[int]:
    """
    Build the Longest Common Prefix (LCP) array for a given string and its suffix array.
    
    Args:
        text: The input string
        suffix_array: The suffix array of the string
        
    Returns:
        List of LCP values where LCP[i] is the length of the longest common prefix
        between suffixes at positions i and i-1 in the suffix array
        
    Example:
        >>> text = "banana"
        >>> sa = build_suffix_array(text)
        >>> build_lcp_array(text, sa)
        [0, 1, 3, 0, 0, 2]
    """
    raise NotImplementedError("LCP array construction not completed")

def search_pattern(text: str, pattern: str, suffix_array: List[int]) -> List[int]:
    """
    Search for a pattern in text using the suffix array.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        suffix_array: The suffix array of the text
        
    Returns:
        List of starting indices where pattern is found
        
    Example:
        >>> text = "banana"
        >>> sa = build_suffix_array(text)
        >>> search_pattern(text, "ana", sa)
        [1, 3]
    """
    raise NotImplementedError("Pattern search implementation not completed")

def find_longest_common_substring(strings: List[str]) -> str:
    """
    Find the longest common substring among a list of strings using suffix arrays.
    
    Args:
        strings: List of input strings
        
    Returns:
        The longest common substring
        
    Example:
        >>> find_longest_common_substring(["ABCDGH", "ACDGHR", "ACDGHR"])
        "CDGH"
    """
    raise NotImplementedError("Longest common substring implementation not completed")

def find_longest_repeated_substring(text: str) -> str:
    """
    Find the longest repeated substring in a string using suffix arrays.
    
    Args:
        text: The input string
        
    Returns:
        The longest repeated substring
        
    Example:
        >>> find_longest_repeated_substring("banana")
        "ana"
    """
    raise NotImplementedError("Longest repeated substring implementation not completed")


class TestSuffixArray(unittest.TestCase):
    def test_build_suffix_array(self):
        # Test with simple string
        text = "banana"
        expected = [5, 3, 1, 0, 4, 2]
        self.assertEqual(build_suffix_array(text), expected)
        
        # Test with repeating characters
        text = "AAAAA"
        expected = [4, 3, 2, 1, 0]
        self.assertEqual(build_suffix_array(text), expected)
        
        # Test with empty string
        text = ""
        expected = []
        self.assertEqual(build_suffix_array(text), expected)
    
    def test_build_lcp_array(self):
        # Test with simple string
        text = "banana"
        sa = build_suffix_array(text)
        expected = [0, 1, 3, 0, 0, 2]
        self.assertEqual(build_lcp_array(text, sa), expected)
        
        # Test with repeating characters
        text = "AAAAA"
        sa = build_suffix_array(text)
        expected = [0, 4, 3, 2, 1]
        self.assertEqual(build_lcp_array(text, sa), expected)
        
        # Test with empty string
        text = ""
        sa = build_suffix_array(text)
        expected = []
        self.assertEqual(build_lcp_array(text, sa), expected)
    
    def test_search_pattern(self):
        # Test with simple pattern
        text = "banana"
        pattern = "ana"
        sa = build_suffix_array(text)
        expected = [1, 3]
        self.assertEqual(search_pattern(text, pattern, sa), expected)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        sa = build_suffix_array(text)
        expected = [0]
        self.assertEqual(search_pattern(text, pattern, sa), expected)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        sa = build_suffix_array(text)
        expected = [4]
        self.assertEqual(search_pattern(text, pattern, sa), expected)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        sa = build_suffix_array(text)
        expected = []
        self.assertEqual(search_pattern(text, pattern, sa), expected)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        sa = build_suffix_array(text)
        expected = []
        self.assertEqual(search_pattern(text, pattern, sa), expected)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        sa = build_suffix_array(text)
        expected = []
        self.assertEqual(search_pattern(text, pattern, sa), expected)
    
    def test_find_longest_common_substring(self):
        # Test with simple strings
        strings = ["ABCDGH", "ACDGHR", "ACDGHR"]
        expected = "CDGH"
        self.assertEqual(find_longest_common_substring(strings), expected)
        
        # Test with no common substring
        strings = ["ABC", "DEF", "GHI"]
        expected = ""
        self.assertEqual(find_longest_common_substring(strings), expected)
        
        # Test with empty strings
        strings = ["", "", ""]
        expected = ""
        self.assertEqual(find_longest_common_substring(strings), expected)
        
        # Test with single string
        strings = ["ABCD"]
        expected = "ABCD"
        self.assertEqual(find_longest_common_substring(strings), expected)
    
    def test_find_longest_repeated_substring(self):
        # Test with simple string
        text = "banana"
        expected = "ana"
        self.assertEqual(find_longest_repeated_substring(text), expected)
        
        # Test with no repeated substring
        text = "ABCD"
        expected = ""
        self.assertEqual(find_longest_repeated_substring(text), expected)
        
        # Test with empty string
        text = ""
        expected = ""
        self.assertEqual(find_longest_repeated_substring(text), expected)
        
        # Test with single character
        text = "A"
        expected = ""
        self.assertEqual(find_longest_repeated_substring(text), expected)
    
    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        sa = build_suffix_array(text)
        self.assertEqual(search_pattern(text, pattern, sa), [])
    
    def test_special_characters(self):
        text = "Hello! @#$%^&*() World!"
        pattern = "@#$%^&*()"
        sa = build_suffix_array(text)
        self.assertEqual(search_pattern(text, pattern, sa), [7])
    
    def test_unicode_characters(self):
        text = "Hello 世界 World"
        pattern = "世界"
        sa = build_suffix_array(text)
        self.assertEqual(search_pattern(text, pattern, sa), [6])
    
    def test_long_text(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        sa = build_suffix_array(text)
        self.assertEqual(search_pattern(text, pattern, sa), [1000])
    
    def test_long_pattern(self):
        text = "A" * 1000
        pattern = "A" * 100
        sa = build_suffix_array(text)
        self.assertEqual(len(search_pattern(text, pattern, sa)), 901)


if __name__ == '__main__':
    unittest.main() 