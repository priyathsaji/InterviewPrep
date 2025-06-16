"""
Problem Statement:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Input Format:
- nums: List[int] - Array of balloon values

Output Format:
- int - Maximum coins that can be collected

Example:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Input: nums = [1,5]
Output: 10
Explanation:
nums = [1,5] --> [5] --> []
coins = 1*1*5 + 1*5*1 = 10

Constraints:
- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100

Time Complexity: O(n³) where n is the length of nums
Space Complexity: O(n²)
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Find the maximum coins that can be collected by bursting balloons.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [3,1,5,8]
        self.assertEqual(self.solution.maxCoins(nums), 167)
    
    def test_example2(self):
        nums = [1,5]
        self.assertEqual(self.solution.maxCoins(nums), 10)
    
    def test_single_balloon(self):
        nums = [5]
        self.assertEqual(self.solution.maxCoins(nums), 5)
    
    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.maxCoins(nums), 0)
    
    def test_two_balloons(self):
        nums = [2,3]
        self.assertEqual(self.solution.maxCoins(nums), 9)
    
    def test_all_ones(self):
        nums = [1,1,1,1]
        self.assertEqual(self.solution.maxCoins(nums), 4)
    
    def test_increasing_sequence(self):
        nums = [1,2,3,4]
        self.assertEqual(self.solution.maxCoins(nums), 40)
    
    def test_decreasing_sequence(self):
        nums = [4,3,2,1]
        self.assertEqual(self.solution.maxCoins(nums), 40)
    
    def test_alternating_values(self):
        nums = [2,1,2,1,2]
        self.assertEqual(self.solution.maxCoins(nums), 16)
    
    def test_large_values(self):
        nums = [10,20,30,40]
        self.assertEqual(self.solution.maxCoins(nums), 29000)
    
    def test_zeros(self):
        nums = [0,0,0,0]
        self.assertEqual(self.solution.maxCoins(nums), 0)
    
    def test_mixed_values(self):
        nums = [3,1,5,8,2,4]
        self.assertEqual(self.solution.maxCoins(nums), 363)

if __name__ == '__main__':
    unittest.main() 