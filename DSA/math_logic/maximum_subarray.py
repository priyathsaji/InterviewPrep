"""
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input Format:
- nums: List[int] - Array of integers

Output Format:
- int - Maximum sum of a contiguous subarray

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Find the maximum sum of a contiguous subarray using Kadane's algorithm.
        The idea is to maintain a running sum and update the maximum sum when we find a larger sum.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)
    
    def test_example2(self):
        nums = [1]
        self.assertEqual(self.solution.maxSubArray(nums), 1)
    
    def test_example3(self):
        nums = [5, 4, -1, 7, 8]
        self.assertEqual(self.solution.maxSubArray(nums), 23)
    
    def test_all_negative(self):
        nums = [-1, -2, -3]
        self.assertEqual(self.solution.maxSubArray(nums), -1)
    
    def test_all_positive(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.maxSubArray(nums), 6)

if __name__ == '__main__':
    unittest.main() 