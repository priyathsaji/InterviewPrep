"""
Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Input Format:
- s: str - A string to check

Output Format:
- bool - True if the string is a palindrome, False otherwise

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if the string is a palindrome after removing non-alphanumeric characters
        and converting to lowercase.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.isPalindrome(s))
    
    def test_example2(self):
        s = "race a car"
        self.assertFalse(self.solution.isPalindrome(s))
    
    def test_example3(self):
        s = " "
        self.assertTrue(self.solution.isPalindrome(s))

if __name__ == '__main__':
    unittest.main() 