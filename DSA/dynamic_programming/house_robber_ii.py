"""
Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input Format:
- nums: List[int] - Array representing money in each house

Output Format:
- int - Maximum amount of money that can be robbed

Example:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [1,2,3]
Output: 3
Explanation: You cannot rob house 1 (money = 1) and then rob house 3 (money = 3), because they are adjacent houses.
So you can only rob house 2 (money = 2).

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Time Complexity: O(n) where n is the length of nums
Space Complexity: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Find the maximum amount of money that can be robbed without alerting the police,
        considering that houses are arranged in a circle.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [2,3,2]
        self.assertEqual(self.solution.rob(nums), 3)
    
    def test_example2(self):
        nums = [1,2,3,1]
        self.assertEqual(self.solution.rob(nums), 4)
    
    def test_example3(self):
        nums = [1,2,3]
        self.assertEqual(self.solution.rob(nums), 3)
    
    def test_single_house(self):
        nums = [5]
        self.assertEqual(self.solution.rob(nums), 5)
    
    def test_two_houses(self):
        nums = [2,3]
        self.assertEqual(self.solution.rob(nums), 3)
    
    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.rob(nums), 0)
    
    def test_all_same_amount(self):
        nums = [2,2,2,2,2]
        self.assertEqual(self.solution.rob(nums), 6)
    
    def test_alternating_amounts(self):
        nums = [1,2,1,2,1,2]
        self.assertEqual(self.solution.rob(nums), 6)
    
    def test_increasing_amounts(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.rob(nums), 8)
    
    def test_decreasing_amounts(self):
        nums = [5,4,3,2,1]
        self.assertEqual(self.solution.rob(nums), 8)
    
    def test_large_amounts(self):
        nums = [100,200,300,400]
        self.assertEqual(self.solution.rob(nums), 500)
    
    def test_zero_amounts(self):
        nums = [0,0,0,0,0]
        self.assertEqual(self.solution.rob(nums), 0)
    
    def test_circular_edge_case(self):
        nums = [1,1,1,1]
        self.assertEqual(self.solution.rob(nums), 2)

if __name__ == '__main__':
    unittest.main() 