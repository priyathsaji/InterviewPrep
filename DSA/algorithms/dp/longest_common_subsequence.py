"""
Longest Common Subsequence (LCS) Algorithm

The Longest Common Subsequence algorithm finds the longest sequence of characters that appear in the same order
in both input sequences, but not necessarily consecutively.

Time Complexity:
- Best: O(mn) where m and n are the lengths of the input sequences
- Average: O(mn)
- Worst: O(mn)

Space Complexity:
- O(mn) for the DP table
- O(m+n) for the reconstructed sequence

Characteristics:
1. Can handle sequences of different lengths
2. Can be extended to handle multiple sequences
3. Can be modified to find all LCS
4. Can be used for DNA sequence alignment
5. Can be adapted for string similarity
"""

from typing import List, Tuple, Optional
import unittest

def longest_common_subsequence(seq1: str, seq2: str) -> str:
    """
    Find the longest common subsequence of two sequences.
    
    Args:
        seq1: First input sequence
        seq2: Second input sequence
        
    Returns:
        The longest common subsequence
        
    Example:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        "ADH"
    """
    raise NotImplementedError("LCS implementation is not provided")

def longest_common_subsequence_length(seq1: str, seq2: str) -> int:
    """
    Find the length of the longest common subsequence of two sequences.
    
    Args:
        seq1: First input sequence
        seq2: Second input sequence
        
    Returns:
        Length of the longest common subsequence
        
    Example:
        >>> longest_common_subsequence_length("ABCDGH", "AEDFHR")
        3
    """
    raise NotImplementedError("LCS length implementation is not provided")

def all_longest_common_subsequences(seq1: str, seq2: str) -> List[str]:
    """
    Find all longest common subsequences of two sequences.
    
    Args:
        seq1: First input sequence
        seq2: Second input sequence
        
    Returns:
        List of all longest common subsequences
        
    Example:
        >>> all_longest_common_subsequences("ABCDGH", "AEDFHR")
        ["ADH"]
    """
    raise NotImplementedError("All LCS implementation is not provided")

def longest_common_subsequence_with_constraints(seq1: str, seq2: str, 
                                              constraints: List[Tuple[str, str]]) -> str:
    """
    Find the longest common subsequence that satisfies given constraints.
    
    Args:
        seq1: First input sequence
        seq2: Second input sequence
        constraints: List of character pairs that must appear together
        
    Returns:
        The longest common subsequence satisfying the constraints
        
    Example:
        >>> constraints = [("A", "D"), ("B", "E")]
        >>> longest_common_subsequence_with_constraints("ABCDGH", "AEDFHR", constraints)
        "ADH"
    """
    raise NotImplementedError("LCS with constraints implementation is not provided")

def longest_common_subsequence_with_weights(seq1: str, seq2: str, 
                                          weights: dict) -> str:
    """
    Find the longest common subsequence with weighted characters.
    
    Args:
        seq1: First input sequence
        seq2: Second input sequence
        weights: Dictionary mapping characters to their weights
        
    Returns:
        The highest weighted common subsequence
        
    Example:
        >>> weights = {"A": 2, "B": 1, "C": 3}
        >>> longest_common_subsequence_with_weights("ABC", "BAC", weights)
        "AC"
    """
    raise NotImplementedError("LCS with weights implementation is not provided")


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_longest_common_subsequence(self):
        # Test with simple sequences
        seq1 = "ABCDGH"
        seq2 = "AEDFHR"
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence(seq1, seq2)
        
        # Test with empty sequences
        seq1 = ""
        seq2 = ""
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence(seq1, seq2)
        
        # Test with no common subsequence
        seq1 = "ABC"
        seq2 = "DEF"
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence(seq1, seq2)
    
    def test_longest_common_subsequence_length(self):
        # Test with simple sequences
        seq1 = "ABCDGH"
        seq2 = "AEDFHR"
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_length(seq1, seq2)
        
        # Test with empty sequences
        seq1 = ""
        seq2 = ""
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_length(seq1, seq2)
        
        # Test with no common subsequence
        seq1 = "ABC"
        seq2 = "DEF"
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_length(seq1, seq2)
    
    def test_all_longest_common_subsequences(self):
        # Test with simple sequences
        seq1 = "ABCDGH"
        seq2 = "AEDFHR"
        with self.assertRaises(NotImplementedError):
            all_longest_common_subsequences(seq1, seq2)
        
        # Test with multiple LCS
        seq1 = "ABC"
        seq2 = "ACB"
        with self.assertRaises(NotImplementedError):
            all_longest_common_subsequences(seq1, seq2)
    
    def test_longest_common_subsequence_with_constraints(self):
        # Test with simple sequences and constraints
        seq1 = "ABCDGH"
        seq2 = "AEDFHR"
        constraints = [("A", "D"), ("B", "E")]
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_with_constraints(seq1, seq2, constraints)
        
        # Test with impossible constraints
        seq1 = "ABC"
        seq2 = "DEF"
        constraints = [("A", "D"), ("B", "E")]
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_with_constraints(seq1, seq2, constraints)
    
    def test_longest_common_subsequence_with_weights(self):
        # Test with simple sequences and weights
        seq1 = "ABC"
        seq2 = "BAC"
        weights = {"A": 2, "B": 1, "C": 3}
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_with_weights(seq1, seq2, weights)
        
        # Test with equal weights
        seq1 = "ABC"
        seq2 = "BAC"
        weights = {"A": 1, "B": 1, "C": 1}
        with self.assertRaises(NotImplementedError):
            longest_common_subsequence_with_weights(seq1, seq2, weights)


if __name__ == '__main__':
    unittest.main() 