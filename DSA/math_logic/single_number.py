"""
Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Input Format:
- nums: List[int] - Array of integers where all numbers appear twice except one

Output Format:
- int - The single number that appears only once

Example:
Input: nums = [4,1,2,1,2]
Output: 4

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Find the single number using XOR operation.
        XOR properties:
        1. a ^ a = 0 (number XOR with itself is 0)
        2. a ^ 0 = a (number XOR with 0 is the number itself)
        3. XOR is associative and commutative
        """
        result = 0
        for num in nums:
            result ^= num
        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(self.solution.singleNumber(nums), 4)
    
    def test_example2(self):
        nums = [2, 2, 1]
        self.assertEqual(self.solution.singleNumber(nums), 1)
    
    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.singleNumber(nums), 1)
    
    def test_negative_numbers(self):
        nums = [-1, -1, -2]
        self.assertEqual(self.solution.singleNumber(nums), -2)

if __name__ == '__main__':
    unittest.main() 