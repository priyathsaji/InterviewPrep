"""
Problem Statement:
Given an integer array nums and an integer k, return the length of the longest strictly increasing subsequence of nums where the difference between adjacent elements is at most k.

Input Format:
- nums: List[int] - Array of integers
- k: int - Maximum allowed difference between adjacent elements

Output Format:
- int - Length of the longest strictly increasing subsequence

Example:
Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation: The longest increasing subsequence is [1,3,4,5,8]. The difference between adjacent elements is at most 3.

Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation: The longest increasing subsequence is [4,5,8,12]. The difference between adjacent elements is at most 5.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5

Time Complexity: O(n log n) where n is the length of nums
Space Complexity: O(n) where n is the length of nums
"""

class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        """
        Find the length of the longest strictly increasing subsequence where the difference between adjacent elements is at most k.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [4,2,1,4,3,4,5,8,15]
        k = 3
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 5)
    
    def test_example2(self):
        nums = [7,4,5,1,8,12,4,7]
        k = 5
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 4)
    
    def test_single_element(self):
        nums = [1]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 1)
    
    def test_two_elements(self):
        nums = [1,2]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 2)
    
    def test_decreasing_sequence(self):
        nums = [5,4,3,2,1]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 1)
    
    def test_increasing_sequence(self):
        nums = [1,2,3,4,5]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 5)
    
    def test_alternating_sequence(self):
        nums = [1,3,2,4,3,5]
        k = 2
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 4)
    
    def test_negative_numbers(self):
        nums = [-5,-3,-1,1,3,5]
        k = 2
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 6)
    
    def test_duplicate_numbers(self):
        nums = [1,2,2,3,3,3,4]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 4)
    
    def test_large_numbers(self):
        nums = [1000,2000,3000,4000,5000]
        k = 1000
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 5)
    
    def test_small_k(self):
        nums = [1,2,3,4,5]
        k = 1
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 2)
    
    def test_large_k(self):
        nums = [1,2,3,4,5]
        k = 10
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 5)
    
    def test_mixed_numbers(self):
        nums = [1,100,2,200,3,300]
        k = 50
        self.assertEqual(self.solution.lengthOfLIS(nums, k), 3)

if __name__ == '__main__':
    unittest.main() 