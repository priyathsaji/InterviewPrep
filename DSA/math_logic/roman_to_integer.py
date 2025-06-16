"""
Problem Statement:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Input Format:
- s: str - A roman numeral string

Output Format:
- int - The integer value of the roman numeral

Example:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert Roman numeral to integer by processing the string from right to left.
        If current value is greater than or equal to previous value, add it.
        Otherwise, subtract it.
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "MCMXCIV"
        self.assertEqual(self.solution.romanToInt(s), 1994)
    
    def test_example2(self):
        s = "III"
        self.assertEqual(self.solution.romanToInt(s), 3)
    
    def test_example3(self):
        s = "LVIII"
        self.assertEqual(self.solution.romanToInt(s), 58)
    
    def test_single_character(self):
        s = "V"
        self.assertEqual(self.solution.romanToInt(s), 5)
    
    def test_subtractive_notation(self):
        s = "IV"
        self.assertEqual(self.solution.romanToInt(s), 4)
        s = "IX"
        self.assertEqual(self.solution.romanToInt(s), 9)

if __name__ == '__main__':
    unittest.main() 