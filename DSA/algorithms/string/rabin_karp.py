"""
Rabin-Karp String Matching Algorithm

The Rabin-Karp algorithm is a string matching algorithm that uses hashing to find
patterns in text. It computes a hash value for the pattern and for each window
of the same length in the text.

Time Complexity:
- Best: O(n + m) when no hash collisions
- Average: O(n + m) with good hash function
- Worst: O(nm) when all windows have same hash value

Space Complexity:
- O(1) for the basic implementation
- O(n) if storing all matches

Characteristics:
1. Uses rolling hash for efficient computation
2. Can find multiple patterns simultaneously
3. Works well with multiple pattern matching
4. Hash collisions may cause false positives
"""

from typing import List, Optional
import unittest

def rabin_karp_search(text: str, pattern: str, base: int = 256, prime: int = 101) -> List[int]:
    """
    Find all occurrences of pattern in text using Rabin-Karp algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        base: Base for the hash function (default: 256 for ASCII)
        prime: Prime number for the hash function (default: 101)
        
    Returns:
        List of starting indices where pattern is found
        
    Example:
        >>> rabin_karp_search("AABAACAADAABAAABAA", "AABA")
        [0, 9, 13]
    """
    raise NotImplementedError("Rabin-Karp search implementation not completed")

def rabin_karp_search_first(text: str, pattern: str, base: int = 256, prime: int = 101) -> int:
    """
    Find the first occurrence of pattern in text using Rabin-Karp algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        base: Base for the hash function (default: 256 for ASCII)
        prime: Prime number for the hash function (default: 101)
        
    Returns:
        Index of first occurrence if found, -1 if not found
        
    Example:
        >>> rabin_karp_search_first("AABAACAADAABAAABAA", "AABA")
        0
    """
    raise NotImplementedError("Rabin-Karp first occurrence search implementation not completed")

def rabin_karp_search_count(text: str, pattern: str, base: int = 256, prime: int = 101) -> int:
    """
    Count the number of occurrences of pattern in text using Rabin-Karp algorithm.
    
    Args:
        text: The text string to search in
        pattern: The pattern string to search for
        base: Base for the hash function (default: 256 for ASCII)
        prime: Prime number for the hash function (default: 101)
        
    Returns:
        Number of occurrences of pattern in text
        
    Example:
        >>> rabin_karp_search_count("AABAACAADAABAAABAA", "AABA")
        3
    """
    raise NotImplementedError("Rabin-Karp count implementation not completed")

def rabin_karp_search_multiple(text: str, patterns: List[str], base: int = 256, prime: int = 101) -> dict[str, List[int]]:
    """
    Find all occurrences of multiple patterns in text using Rabin-Karp algorithm.
    
    Args:
        text: The text string to search in
        patterns: List of pattern strings to search for
        base: Base for the hash function (default: 256 for ASCII)
        prime: Prime number for the hash function (default: 101)
        
    Returns:
        Dictionary mapping each pattern to its list of starting indices
        
    Example:
        >>> rabin_karp_search_multiple("AABAACAADAABAAABAA", ["AABA", "AA"])
        {'AABA': [0, 9, 13], 'AA': [0, 3, 9, 13, 16]}
    """
    raise NotImplementedError("Rabin-Karp multiple pattern search implementation not completed")


class TestRabinKarp(unittest.TestCase):
    def test_rabin_karp_search(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        expected = [0, 9, 13]
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        expected = [0]
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        expected = [4]
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        expected = []
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        expected = []
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        expected = []
        self.assertEqual(rabin_karp_search(text, pattern), expected)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        expected = [0, 1, 2, 3]
        self.assertEqual(rabin_karp_search(text, pattern), expected)
    
    def test_rabin_karp_search_first(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(rabin_karp_search_first(text, pattern), 0)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(rabin_karp_search_first(text, pattern), 0)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(rabin_karp_search_first(text, pattern), 4)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(rabin_karp_search_first(text, pattern), -1)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(rabin_karp_search_first(text, pattern), -1)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(rabin_karp_search_first(text, pattern), -1)
    
    def test_rabin_karp_search_count(self):
        # Test with simple pattern
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(rabin_karp_search_count(text, pattern), 3)
        
        # Test with pattern at start
        text = "ABCDEFG"
        pattern = "ABC"
        self.assertEqual(rabin_karp_search_count(text, pattern), 1)
        
        # Test with pattern at end
        text = "ABCDEFG"
        pattern = "EFG"
        self.assertEqual(rabin_karp_search_count(text, pattern), 1)
        
        # Test with no match
        text = "ABCDEFG"
        pattern = "XYZ"
        self.assertEqual(rabin_karp_search_count(text, pattern), 0)
        
        # Test with empty pattern
        text = "ABCDEFG"
        pattern = ""
        self.assertEqual(rabin_karp_search_count(text, pattern), 0)
        
        # Test with empty text
        text = ""
        pattern = "ABC"
        self.assertEqual(rabin_karp_search_count(text, pattern), 0)
        
        # Test with repeating pattern
        text = "AAAAA"
        pattern = "AA"
        self.assertEqual(rabin_karp_search_count(text, pattern), 4)
    
    def test_rabin_karp_search_multiple(self):
        # Test with multiple patterns
        text = "AABAACAADAABAAABAA"
        patterns = ["AABA", "AA"]
        expected = {
            "AABA": [0, 9, 13],
            "AA": [0, 3, 9, 13, 16]
        }
        self.assertEqual(rabin_karp_search_multiple(text, patterns), expected)
        
        # Test with no matches
        text = "ABCDEFG"
        patterns = ["XYZ", "123"]
        expected = {
            "XYZ": [],
            "123": []
        }
        self.assertEqual(rabin_karp_search_multiple(text, patterns), expected)
        
        # Test with empty patterns
        text = "ABCDEFG"
        patterns = []
        expected = {}
        self.assertEqual(rabin_karp_search_multiple(text, patterns), expected)
    
    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        self.assertEqual(rabin_karp_search(text, pattern), [])
        self.assertEqual(rabin_karp_search_first(text, pattern), -1)
        self.assertEqual(rabin_karp_search_count(text, pattern), 0)
    
    def test_special_characters(self):
        text = "Hello! @#$%^&*() World!"
        pattern = "@#$%^&*()"
        self.assertEqual(rabin_karp_search(text, pattern), [7])
        self.assertEqual(rabin_karp_search_first(text, pattern), 7)
        self.assertEqual(rabin_karp_search_count(text, pattern), 1)
    
    def test_unicode_characters(self):
        text = "Hello 世界 World"
        pattern = "世界"
        self.assertEqual(rabin_karp_search(text, pattern), [6])
        self.assertEqual(rabin_karp_search_first(text, pattern), 6)
        self.assertEqual(rabin_karp_search_count(text, pattern), 1)
    
    def test_long_text(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        self.assertEqual(rabin_karp_search(text, pattern), [1000])
        self.assertEqual(rabin_karp_search_first(text, pattern), 1000)
        self.assertEqual(rabin_karp_search_count(text, pattern), 1)
    
    def test_long_pattern(self):
        text = "A" * 1000
        pattern = "A" * 100
        self.assertEqual(len(rabin_karp_search(text, pattern)), 901)
        self.assertEqual(rabin_karp_search_first(text, pattern), 0)
        self.assertEqual(rabin_karp_search_count(text, pattern), 901)
    
    def test_hash_collision(self):
        # Test with different base and prime to avoid hash collisions
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        self.assertEqual(rabin_karp_search(text, pattern, base=31, prime=1000000007), [0, 9, 13])


if __name__ == '__main__':
    unittest.main() 