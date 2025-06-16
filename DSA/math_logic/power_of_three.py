"""
Problem Statement:
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Input Format:
- n: int - The number to check

Output Format:
- bool - True if n is a power of three, False otherwise

Example:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Constraints:
- -2^31 <= n <= 2^31 - 1

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Check if a number is a power of three using mathematical properties.
        A number is a power of three if and only if:
        1. It is positive
        2. It divides the largest power of three that fits in an integer
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 27
        self.assertTrue(self.solution.isPowerOfThree(n))
    
    def test_example2(self):
        n = 0
        self.assertFalse(self.solution.isPowerOfThree(n))
    
    def test_example3(self):
        n = 9
        self.assertTrue(self.solution.isPowerOfThree(n))
    
    def test_negative_number(self):
        n = -3
        self.assertFalse(self.solution.isPowerOfThree(n))
    
    def test_not_power_of_three(self):
        n = 45
        self.assertFalse(self.solution.isPowerOfThree(n))

if __name__ == '__main__':
    unittest.main() 