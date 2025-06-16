"""
Problem Statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Input Format:
- n: int - An unsigned integer

Output Format:
- int - The number of '1' bits in the binary representation of n

Example:
Input: n = 11 (binary: 00000000000000000000000000001011)
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Constraints:
- The input must be a binary string of length 32.

Time Complexity: O(1) as we always process 32 bits
Space Complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Count the number of 1 bits using Brian Kernighan's algorithm.
        The algorithm uses the fact that n & (n-1) removes the rightmost 1 bit.
        """
        count = 0
        while n:
            n &= (n - 1)  # Remove the rightmost 1 bit
            count += 1
        return count

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 11  # 00000000000000000000000000001011
        self.assertEqual(self.solution.hammingWeight(n), 3)
    
    def test_example2(self):
        n = 128  # 00000000000000000000000010000000
        self.assertEqual(self.solution.hammingWeight(n), 1)
    
    def test_zero(self):
        n = 0  # 00000000000000000000000000000000
        self.assertEqual(self.solution.hammingWeight(n), 0)
    
    def test_all_ones(self):
        n = 4294967295  # 11111111111111111111111111111111
        self.assertEqual(self.solution.hammingWeight(n), 32)

if __name__ == '__main__':
    unittest.main() 