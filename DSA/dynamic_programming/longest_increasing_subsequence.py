"""
Problem Statement:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input Format:
- nums: List[int] - Array of integers

Output Format:
- int - Length of the longest strictly increasing subsequence

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.

Constraints:
- 1 <= len(nums) <= 2500
- -10^4 <= nums[i] <= 10^4

Time Complexity: O(n²) where n is the length of nums
Space Complexity: O(n) where n is the length of nums
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Find the length of the longest strictly increasing subsequence.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [10,9,2,5,3,7,101,18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_example2(self):
        nums = [0,1,0,3,2,3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_example3(self):
        nums = [7,7,7,7,7,7,7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_two_elements(self):
        nums = [1,2]
        self.assertEqual(self.solution.lengthOfLIS(nums), 2)
    
    def test_decreasing_sequence(self):
        nums = [5,4,3,2,1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_increasing_sequence(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)
    
    def test_alternating_sequence(self):
        nums = [1,3,2,4,3,5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_negative_numbers(self):
        nums = [-1,-2,-3,-4,-5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_mixed_numbers(self):
        nums = [-5,3,-2,4,1,0]
        self.assertEqual(self.solution.lengthOfLIS(nums), 3)
    
    def test_duplicate_numbers(self):
        nums = [1,2,2,3,3,3,4]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_large_numbers(self):
        nums = [10000,9000,8000,7000,6000]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_small_numbers(self):
        nums = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(self.solution.lengthOfLIS(nums), 10)

if __name__ == '__main__':
    unittest.main() 