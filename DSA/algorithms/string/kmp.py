"""
Knuth-Morris-Pratt (KMP) String Matching Algorithm

The KMP algorithm is an efficient string matching algorithm that uses information
about the pattern to avoid unnecessary comparisons.

Time Complexity:
- Preprocessing: O(m) where m is pattern length
- Matching: O(n) where n is text length
- Total: O(n + m)

Space Complexity:
- O(m) for the failure function array

Characteristics:
1. Linear time complexity
2. No backing up in the text
3. Efficient for long patterns
4. Works well with repetitive patterns
"""

from typing import List, Optional
import unittest

def compute_failure_function(pattern: str) -> List[int]:
    """
    Compute the failure function (longest proper prefix that is also a suffix)
    for the KMP algorithm.
    
    Args:
        pattern: The pattern string to compute failure function for
        
    Returns:
        List of integers representing the failure function
        
    Example:
        >>> compute_failure_function("AABAACAABAA")
        [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    """
    raise NotImplementedError("Failure function computation not completed")

def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using KMP algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        List of starting indices where pattern is found
        
    Example:
        >>> kmp_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    raise NotImplementedError("KMP search implementation not completed")

def kmp_search_first(text: str, pattern: str) -> int:
    """
    Find the first occurrence of pattern in text using KMP algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Index of first occurrence if found, -1 if not found
        
    Example:
        >>> kmp_search_first("AABAACAADAABAAABAA", "AABA")
        0
    """
    raise NotImplementedError("KMP first occurrence search implementation not completed")

def kmp_search_count(text: str, pattern: str) -> int:
    """
    Count the number of occurrences of pattern in text using KMP algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        
    Returns:
        Number of occurrences of pattern in text
        
    Example:
        >>> kmp_search_count("AABAACAADAABAAABAA", "AABA")
        3
    """
    raise NotImplementedError("KMP count implementation not completed")


class TestKMP(unittest.TestCase):
    def test_compute_failure_function(self):
        # Test with simple pattern
        pattern = "AABAACAABAA"
        expected = [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
        self.assertEqual(compute_failure_function(pattern), expected)
        
        # Test with single character
        pattern = "A"
        expected = [0]
        self.assertEqual(compute_failure_function(pattern), expected)
        
        # Test with repeating pattern
        pattern = "AAAA"
        expected = [0, 1, 2, 3]
        self.assertEqual(compute_failure_function(pattern), expected)
        
        # Test with no proper prefix
        pattern = "ABCD"
        expected = [0, 0, 0, 0]
        self.assertEqual(compute_failure_function(pattern), expected)
    
    def test_kmp_search(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        expected = [0, 9, 13]
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        expected = [0]
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        expected = [4]
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        expected = []
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        expected = []
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        expected = []
        self.assertEqual(kmp_search(text, pattern), expected)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        expected = [0, 1, 2, 3]
        self.assertEqual(kmp_search(text, pattern), expected)
    
    def test_kmp_search_first(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(kmp_search_first(text, pattern), 0)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(kmp_search_first(text, pattern), 0)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(kmp_search_first(text, pattern), 4)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(kmp_search_first(text, pattern), -1)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(kmp_search_first(text, pattern), -1)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(kmp_search_first(text, pattern), -1)
    
    def test_kmp_search_count(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(kmp_search_count(text, pattern), 3)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(kmp_search_count(text, pattern), 1)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(kmp_search_count(text, pattern), 1)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(kmp_search_count(text, pattern), 0)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(kmp_search_count(text, pattern), 0)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(kmp_search_count(text, pattern), 0)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        self.assertEqual(kmp_search_count(text, pattern), 4)
    
    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        self.assertEqual(kmp_search(text, pattern), [])
        self.assertEqual(kmp_search_first(text, pattern), -1)
        self.assertEqual(kmp_search_count(text, pattern), 0)
    
    def test_special_characters(self):
        text = "Hello! @#$%^&*() World!"
        pattern = "@#$%^&*()"
        self.assertEqual(kmp_search(text, pattern), [7])
        self.assertEqual(kmp_search_first(text, pattern), 7)
        self.assertEqual(kmp_search_count(text, pattern), 1)
    
    def test_unicode_characters(self):
        text = "Hello 世界 World"
        pattern = "世界"
        self.assertEqual(kmp_search(text, pattern), [6])
        self.assertEqual(kmp_search_first(text, pattern), 6)
        self.assertEqual(kmp_search_count(text, pattern), 1)
    
    def test_long_text(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        self.assertEqual(kmp_search(text, pattern), [1000])
        self.assertEqual(kmp_search_first(text, pattern), 1000)
        self.assertEqual(kmp_search_count(text, pattern), 1)
    
    def test_long_pattern(self):
        text = "A" * 1000
        pattern = "A" * 100
        self.assertEqual(len(kmp_search(text, pattern)), 901)
        self.assertEqual(kmp_search_first(text, pattern), 0)
        self.assertEqual(kmp_search_count(text, pattern), 901)


if __name__ == '__main__':
    unittest.main() 