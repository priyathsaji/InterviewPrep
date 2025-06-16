"""
Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Input Format:
- x: int - A signed 32-bit integer

Output Format:
- int - The reversed integer, or 0 if the result is outside the valid range

Example:
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

Constraints:
- -2^31 <= x <= 2^31 - 1

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a signed 32-bit integer.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        x = 123
        self.assertEqual(self.solution.reverse(x), 321)
    
    def test_example2(self):
        x = -123
        self.assertEqual(self.solution.reverse(x), -321)
    
    def test_example3(self):
        x = 120
        self.assertEqual(self.solution.reverse(x), 21)
    
    def test_example4(self):
        x = 0
        self.assertEqual(self.solution.reverse(x), 0)
    
    def test_overflow(self):
        x = 2**31
        self.assertEqual(self.solution.reverse(x), 0)

if __name__ == '__main__':
    unittest.main() 