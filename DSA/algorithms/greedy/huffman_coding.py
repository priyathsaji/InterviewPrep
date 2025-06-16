"""
Huffman Coding

Huffman Coding is a lossless data compression algorithm that assigns variable-length
codes to input characters based on their frequencies. More frequent characters get
shorter codes, while less frequent characters get longer codes.

Time Complexity:
- Best: O(n log n) for building the tree
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity:
- O(n) for storing the frequency table and tree

Characteristics:
1. Optimal prefix code
2. Variable-length encoding
3. No code is a prefix of another code
4. More frequent symbols get shorter codes
"""

from typing import Dict, List, Tuple, Optional
from heapq import heappush, heappop
import unittest

class HuffmanNode:
    """Node class for Huffman tree."""
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None
    
    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

def build_huffman_tree(freq_table: Dict[str, int]) -> HuffmanNode:
    """
    Build a Huffman tree from a frequency table.
    
    Args:
        freq_table: Dictionary mapping characters to their frequencies
        
    Returns:
        Root node of the Huffman tree
        
    Example:
        >>> freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        >>> root = build_huffman_tree(freq_table)
        >>> root.freq == sum(freq_table.values())
        True
    """
    raise NotImplementedError("Huffman tree building implementation not completed")

def build_huffman_codes(root: HuffmanNode) -> Dict[str, str]:
    """
    Build Huffman codes from a Huffman tree.
    
    Args:
        root: Root node of the Huffman tree
        
    Returns:
        Dictionary mapping characters to their Huffman codes
        
    Example:
        >>> freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        >>> root = build_huffman_tree(freq_table)
        >>> codes = build_huffman_codes(root)
        >>> len(codes) == len(freq_table)
        True
    """
    raise NotImplementedError("Huffman code building implementation not completed")

def encode_text(text: str, codes: Dict[str, str]) -> str:
    """
    Encode text using Huffman codes.
    
    Args:
        text: Input text to encode
        codes: Dictionary mapping characters to their Huffman codes
        
    Returns:
        Encoded binary string
        
    Example:
        >>> freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        >>> root = build_huffman_tree(freq_table)
        >>> codes = build_huffman_codes(root)
        >>> encoded = encode_text("abc", codes)
        >>> isinstance(encoded, str)
        True
    """
    raise NotImplementedError("Text encoding implementation not completed")

def decode_text(encoded: str, root: HuffmanNode) -> str:
    """
    Decode text using a Huffman tree.
    
    Args:
        encoded: Encoded binary string
        root: Root node of the Huffman tree
        
    Returns:
        Decoded text
        
    Example:
        >>> freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        >>> root = build_huffman_tree(freq_table)
        >>> codes = build_huffman_codes(root)
        >>> encoded = encode_text("abc", codes)
        >>> decoded = decode_text(encoded, root)
        >>> decoded == "abc"
        True
    """
    raise NotImplementedError("Text decoding implementation not completed")

def compress_file(input_file: str, output_file: str) -> None:
    """
    Compress a file using Huffman coding.
    
    Args:
        input_file: Path to input file
        output_file: Path to output file
        
    Example:
        >>> compress_file("input.txt", "compressed.bin")
    """
    raise NotImplementedError("File compression implementation not completed")

def decompress_file(input_file: str, output_file: str) -> None:
    """
    Decompress a file using Huffman coding.
    
    Args:
        input_file: Path to compressed file
        output_file: Path to output file
        
    Example:
        >>> decompress_file("compressed.bin", "decompressed.txt")
    """
    raise NotImplementedError("File decompression implementation not completed")


class TestHuffmanCoding(unittest.TestCase):
    def test_build_huffman_tree(self):
        # Test with simple frequency table
        freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        root = build_huffman_tree(freq_table)
        self.assertEqual(root.freq, sum(freq_table.values()))
        
        # Test with single character
        freq_table = {'a': 1}
        root = build_huffman_tree(freq_table)
        self.assertEqual(root.freq, 1)
        self.assertEqual(root.char, 'a')
        
        # Test with empty frequency table
        freq_table = {}
        with self.assertRaises(ValueError):
            build_huffman_tree(freq_table)
    
    def test_build_huffman_codes(self):
        # Test with simple frequency table
        freq_table = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        self.assertEqual(len(codes), len(freq_table))
        
        # Test prefix property
        for char1, code1 in codes.items():
            for char2, code2 in codes.items():
                if char1 != char2:
                    self.assertFalse(code1.startswith(code2))
                    self.assertFalse(code2.startswith(code1))
        
        # Test with single character
        freq_table = {'a': 1}
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        self.assertEqual(codes['a'], '0')
    
    def test_encode_decode(self):
        # Test with simple text
        text = "hello world"
        freq_table = {}
        for char in text:
            freq_table[char] = freq_table.get(char, 0) + 1
        
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)
        
        # Test with empty text
        text = ""
        freq_table = {}
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)
        
        # Test with single character
        text = "a"
        freq_table = {'a': 1}
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)
    
    def test_compression_ratio(self):
        # Test compression ratio with repeated text
        text = "a" * 1000
        freq_table = {'a': 1000}
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        self.assertLess(len(encoded), len(text) * 8)  # Should be better than ASCII
        
        # Test compression ratio with random text
        text = "".join(chr(i) for i in range(128)) * 10
        freq_table = {}
        for char in text:
            freq_table[char] = freq_table.get(char, 0) + 1
        
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        self.assertLess(len(encoded), len(text) * 8)  # Should be better than ASCII
    
    def test_edge_cases(self):
        # Test with special characters
        text = "!@#$%^&*()_+"
        freq_table = {}
        for char in text:
            freq_table[char] = freq_table.get(char, 0) + 1
        
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)
        
        # Test with Unicode characters
        text = "你好世界"
        freq_table = {}
        for char in text:
            freq_table[char] = freq_table.get(char, 0) + 1
        
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)
    
    def test_performance(self):
        # Test with large text
        text = "".join(chr(i % 128) for i in range(10000))
        freq_table = {}
        for char in text:
            freq_table[char] = freq_table.get(char, 0) + 1
        
        root = build_huffman_tree(freq_table)
        codes = build_huffman_codes(root)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, root)
        self.assertEqual(decoded, text)


if __name__ == '__main__':
    unittest.main() 