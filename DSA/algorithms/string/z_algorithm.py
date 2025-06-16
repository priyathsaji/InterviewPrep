"""
Z-Algorithm for String Matching

The Z-Algorithm is a linear time pattern matching algorithm that computes the Z-array,
where Z[i] is the length of the longest substring starting from position i that matches
the prefix of the string. It can be used for pattern matching, string compression,
and finding all occurrences of a pattern in a text.

Time Complexity:
- Best: O(n + m) where n is text length and m is pattern length
- Average: O(n + m)
- Worst: O(n + m)

Space Complexity:
- O(n + m) for storing the Z-array

Characteristics:
1. Linear time complexity
2. No preprocessing needed
3. Works well for pattern matching
4. Can be used for string compression
"""

from typing import List, Tuple
import unittest

def compute_z_array(string: str) -> List[int]:
    """
    Compute the Z-array for a given string.
    
    Args:
        string: The input string
        
    Returns:
        List of Z-values where Z[i] is the length of the longest substring
        starting from position i that matches the prefix of the string
        
    Example:
        >>> compute_z_array("aabxaabxcaabxaabxay")
        [20, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]
    """
    raise NotImplementedError("Z-array computation not completed")

def z_algorithm_search(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using Z-Algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        List of starting indices where pattern is found
        
    Example:
        >>> z_algorithm_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    raise NotImplementedError("Z-Algorithm search implementation not completed")

def z_algorithm_search_first(text: str, pattern: str) -> int:
    """
    Find the first occurrence of pattern in text using Z-Algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Index of first occurrence if found, -1 if not found
        
    Example:
        >>> z_algorithm_search_first("AABAACAADAABAAABAA", "AABA")
        0
    """
    raise NotImplementedError("Z-Algorithm first occurrence search implementation not completed")

def z_algorithm_search_count(text: str, pattern: str) -> int:
    """
    Count the number of occurrences of pattern in text using Z-Algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Number of occurrences of pattern in text
        
    Example:
        >>> z_algorithm_search_count("AABAACAADAABAAABAA", "AABA")
        3
    """
    raise NotImplementedError("Z-Algorithm count implementation not completed")

def find_longest_common_substring(strings: List[str]) -> str:
    """
    Find the longest common substring among a list of strings using Z-Algorithm.
    
    Args:
        strings: List of input strings
        
    Returns:
        The longest common substring
        
    Example:
        >>> find_longest_common_substring(["ABCDGH", "ACDGHR", "ACDGHR"])
        "CDGH"
    """
    raise NotImplementedError("Longest common substring implementation not completed")


class TestZAlgorithm(unittest.TestCase):
    def test_compute_z_array(self):
        # Test with simple string
        string = "aabxaabxcaabxaabxay"
        expected = [20, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]
        self.assertEqual(compute_z_array(string), expected)
        
        # Test with repeating characters
        string = "AAAAA"
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(compute_z_array(string), expected)
        
        # Test with empty string
        string = ""
        expected = []
        self.assertEqual(compute_z_array(string), expected)
    
    def test_z_algorithm_search(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        expected = [0, 9, 13]
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        expected = [0]
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        expected = [4]
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        expected = []
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        expected = []
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        expected = []
        self.assertEqual(z_algorithm_search(text, pattern), expected)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        expected = [0, 1, 2, 3]
        self.assertEqual(z_algorithm_search(text, pattern), expected)
    
    def test_z_algorithm_search_first(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(z_algorithm_search_first(text, pattern), 0)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(z_algorithm_search_first(text, pattern), 0)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(z_algorithm_search_first(text, pattern), 4)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(z_algorithm_search_first(text, pattern), -1)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(z_algorithm_search_first(text, pattern), -1)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(z_algorithm_search_first(text, pattern), -1)
    
    def test_z_algorithm_search_count(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(z_algorithm_search_count(text, pattern), 3)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(z_algorithm_search_count(text, pattern), 1)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(z_algorithm_search_count(text, pattern), 1)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(z_algorithm_search_count(text, pattern), 0)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(z_algorithm_search_count(text, pattern), 0)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(z_algorithm_search_count(text, pattern), 0)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        self.assertEqual(z_algorithm_search_count(text, pattern), 4)
    
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
    
    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        self.assertEqual(z_algorithm_search(text, pattern), [])
        self.assertEqual(z_algorithm_search_first(text, pattern), -1)
        self.assertEqual(z_algorithm_search_count(text, pattern), 0)
    
    def test_special_characters(self):
        text = "Hello! @#$%^&*() World!"
        pattern = "@#$%^&*()"
        self.assertEqual(z_algorithm_search(text, pattern), [7])
        self.assertEqual(z_algorithm_search_first(text, pattern), 7)
        self.assertEqual(z_algorithm_search_count(text, pattern), 1)
    
    def test_unicode_characters(self):
        text = "Hello 世界 World"
        pattern = "世界"
        self.assertEqual(z_algorithm_search(text, pattern), [6])
        self.assertEqual(z_algorithm_search_first(text, pattern), 6)
        self.assertEqual(z_algorithm_search_count(text, pattern), 1)
    
    def test_long_text(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        self.assertEqual(z_algorithm_search(text, pattern), [1000])
        self.assertEqual(z_algorithm_search_first(text, pattern), 1000)
        self.assertEqual(z_algorithm_search_count(text, pattern), 1)
    
    def test_long_pattern(self):
        text = "A" * 1000
        pattern = "A" * 100
        self.assertEqual(len(z_algorithm_search(text, pattern)), 901)
        self.assertEqual(z_algorithm_search_first(text, pattern), 0)
        self.assertEqual(z_algorithm_search_count(text, pattern), 901)


if __name__ == '__main__':
    unittest.main() 