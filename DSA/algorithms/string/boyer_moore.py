"""
Boyer-Moore String Matching Algorithm

The Boyer-Moore algorithm is a string matching algorithm that uses two heuristics
to skip unnecessary comparisons: the bad character rule and the good suffix rule.
It is particularly efficient when the pattern is long and the alphabet is large.

Time Complexity:
- Best: O(n/m) when pattern is not in text
- Average: O(n) for random text
- Worst: O(nm) when pattern and text are similar

Space Complexity:
- O(m + σ) where m is pattern length and σ is alphabet size

Characteristics:
1. Uses bad character rule to skip comparisons
2. Uses good suffix rule for additional skipping
3. Works best with long patterns
4. Performs better with larger alphabets
"""

from typing import List, Dict, Optional
import unittest

def compute_bad_character_table(pattern: str) -> Dict[str, int]:
    """
    Compute the bad character table for Boyer-Moore algorithm.
    
    Args:
        pattern: The pattern string
        
    Returns:
        Dictionary mapping characters to their rightmost position in pattern
        
    Example:
        >>> compute_bad_character_table("ABCABC")
        {'A': 3, 'B': 4, 'C': 5}
    """
    raise NotImplementedError("Bad character table computation not completed")

def compute_good_suffix_table(pattern: str) -> List[int]:
    """
    Compute the good suffix table for Boyer-Moore algorithm.
    
    Args:
        pattern: The pattern string
        
    Returns:
        List of shift distances for each position
        
    Example:
        >>> compute_good_suffix_table("ABCABC")
        [6, 6, 6, 6, 6, 6]
    """
    raise NotImplementedError("Good suffix table computation not completed")

def boyer_moore_search(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using Boyer-Moore algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        List of starting indices where pattern is found
        
    Example:
        >>> boyer_moore_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    raise NotImplementedError("Boyer-Moore search implementation not completed")

def boyer_moore_search_first(text: str, pattern: str) -> int:
    """
    Find the first occurrence of pattern in text using Boyer-Moore algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Index of first occurrence if found, -1 if not found
        
    Example:
        >>> boyer_moore_search_first("AABAACAADAABAAABAA", "AABA")
        0
    """
    raise NotImplementedError("Boyer-Moore first occurrence search implementation not completed")

def boyer_moore_search_count(text: str, pattern: str) -> int:
    """
    Count the number of occurrences of pattern in text using Boyer-Moore algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Number of occurrences of pattern in text
        
    Example:
        >>> boyer_moore_search_count("AABAACAADAABAAABAA", "AABA")
        3
    """
    raise NotImplementedError("Boyer-Moore count implementation not completed")


class TestBoyerMoore(unittest.TestCase):
    def test_compute_bad_character_table(self):
        # Test with simple pattern
        pattern = "ABCABC"
        expected = {'A': 3, 'B': 4, 'C': 5}
        self.assertEqual(compute_bad_character_table(pattern), expected)
        
        # Test with repeating characters
        pattern = "AAAAA"
        expected = {'A': 4}
        self.assertEqual(compute_bad_character_table(pattern), expected)
        
        # Test with empty pattern
        pattern = ""
        expected = {}
        self.assertEqual(compute_bad_character_table(pattern), expected)
    
    def test_compute_good_suffix_table(self):
        # Test with simple pattern
        pattern = "ABCABC"
        expected = [6, 6, 6, 6, 6, 6]
        self.assertEqual(compute_good_suffix_table(pattern), expected)
        
        # Test with repeating characters
        pattern = "AAAAA"
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(compute_good_suffix_table(pattern), expected)
        
        # Test with empty pattern
        pattern = ""
        expected = []
        self.assertEqual(compute_good_suffix_table(pattern), expected)
    
    def test_boyer_moore_search(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        expected = [0, 9, 13]
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        expected = [0]
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        expected = [4]
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        expected = []
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        expected = []
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        expected = []
        self.assertEqual(boyer_moore_search(text, pattern), expected)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        expected = [0, 1, 2, 3]
        self.assertEqual(boyer_moore_search(text, pattern), expected)
    
    def test_boyer_moore_search_first(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(boyer_moore_search_first(text, pattern), 0)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(boyer_moore_search_first(text, pattern), 0)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(boyer_moore_search_first(text, pattern), 4)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(boyer_moore_search_first(text, pattern), -1)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(boyer_moore_search_first(text, pattern), -1)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(boyer_moore_search_first(text, pattern), -1)
    
    def test_boyer_moore_search_count(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(boyer_moore_search_count(text, pattern), 3)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(boyer_moore_search_count(text, pattern), 1)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(boyer_moore_search_count(text, pattern), 1)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(boyer_moore_search_count(text, pattern), 0)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(boyer_moore_search_count(text, pattern), 0)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(boyer_moore_search_count(text, pattern), 0)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        self.assertEqual(boyer_moore_search_count(text, pattern), 4)
    
    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        self.assertEqual(boyer_moore_search(text, pattern), [])
        self.assertEqual(boyer_moore_search_first(text, pattern), -1)
        self.assertEqual(boyer_moore_search_count(text, pattern), 0)
    
    def test_special_characters(self):
        text = "Hello! @#$%^&*() World!"
        pattern = "@#$%^&*()"
        self.assertEqual(boyer_moore_search(text, pattern), [7])
        self.assertEqual(boyer_moore_search_first(text, pattern), 7)
        self.assertEqual(boyer_moore_search_count(text, pattern), 1)
    
    def test_unicode_characters(self):
        text = "Hello 世界 World"
        pattern = "世界"
        self.assertEqual(boyer_moore_search(text, pattern), [6])
        self.assertEqual(boyer_moore_search_first(text, pattern), 6)
        self.assertEqual(boyer_moore_search_count(text, pattern), 1)
    
    def test_long_text(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        self.assertEqual(boyer_moore_search(text, pattern), [1000])
        self.assertEqual(boyer_moore_search_first(text, pattern), 1000)
        self.assertEqual(boyer_moore_search_count(text, pattern), 1)
    
    def test_long_pattern(self):
        text = "A" * 1000
        pattern = "A" * 100
        self.assertEqual(len(boyer_moore_search(text, pattern)), 901)
        self.assertEqual(boyer_moore_search_first(text, pattern), 0)
        self.assertEqual(boyer_moore_search_count(text, pattern), 901)


if __name__ == '__main__':
    unittest.main() 