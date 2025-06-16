"""
Problem Statement:
Given two numbers, find their Greatest Common Divisor (GCD) and Least Common Multiple (LCM).

Input Format:
- a: int - First number
- b: int - Second number

Output Format:
- tuple(int, int) - (GCD, LCM) of the two numbers

Example:
Input: a = 12, b = 18
Output: (6, 36)
Explanation: GCD(12, 18) = 6, LCM(12, 18) = 36

Constraints:
- 1 <= a, b <= 10^9

Time Complexity: O(log(min(a, b))) for GCD
Space Complexity: O(1)
"""

class Solution:
    def gcd_lcm(self, a: int, b: int) -> tuple[int, int]:
        """
        Find GCD and LCM of two numbers using Euclidean algorithm.
        GCD is found using the property that GCD(a, b) = GCD(b, a % b)
        LCM is found using the property that LCM(a, b) = (a * b) / GCD(a, b)
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        a, b = 12, 18
        gcd, lcm = self.solution.gcd_lcm(a, b)
        self.assertEqual(gcd, 6)
        self.assertEqual(lcm, 36)
    
    def test_example2(self):
        a, b = 7, 13
        gcd, lcm = self.solution.gcd_lcm(a, b)
        self.assertEqual(gcd, 1)
        self.assertEqual(lcm, 91)
    
    def test_same_numbers(self):
        a, b = 5, 5
        gcd, lcm = self.solution.gcd_lcm(a, b)
        self.assertEqual(gcd, 5)
        self.assertEqual(lcm, 5)
    
    def test_zero(self):
        a, b = 0, 5
        gcd, lcm = self.solution.gcd_lcm(a, b)
        self.assertEqual(gcd, 5)
        self.assertEqual(lcm, 0)
    
    def test_negative_numbers(self):
        a, b = -12, 18
        gcd, lcm = self.solution.gcd_lcm(a, b)
        self.assertEqual(gcd, 6)
        self.assertEqual(lcm, 36)

if __name__ == '__main__':
    unittest.main() 