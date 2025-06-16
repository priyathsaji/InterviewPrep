"""
Problem Statement:
Given a non-empty array nums containing only positive integers, determine if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Input Format:
- nums: List[int] - Array of positive integers

Output Format:
- bool - True if the array can be partitioned into two subsets with equal sum, False otherwise

Example:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

Time Complexity: O(n * sum) where n is the length of nums and sum is the total sum of nums
Space Complexity: O(n * sum)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determine if the array can be partitioned into two subsets with equal sum.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [1,5,11,5]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_example2(self):
        nums = [1,2,3,5]
        self.assertFalse(self.solution.canPartition(nums))
    
    def test_single_element(self):
        nums = [1]
        self.assertFalse(self.solution.canPartition(nums))
    
    def test_two_equal_elements(self):
        nums = [1,1]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_two_unequal_elements(self):
        nums = [1,2]
        self.assertFalse(self.solution.canPartition(nums))
    
    def test_all_same_elements(self):
        nums = [2,2,2,2]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_odd_sum(self):
        nums = [1,2,3,4,5]
        self.assertFalse(self.solution.canPartition(nums))
    
    def test_even_sum_possible(self):
        nums = [1,2,3,4,5,5]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_large_numbers(self):
        nums = [100,100,100,100]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_alternating_numbers(self):
        nums = [1,2,1,2,1,2]
        self.assertTrue(self.solution.canPartition(nums))
    
    def test_impossible_partition(self):
        nums = [1,2,3,4,5,6,7]
        self.assertFalse(self.solution.canPartition(nums))

if __name__ == '__main__':
    unittest.main() 