"""
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input Format:
- nums: List[int] - An array of integers
- target: int - The target sum

Output Format:
- List[int] - Indices of the two numbers that add up to target

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target.
        Using a hash map to store complements for O(n) time complexity.
        """
        raise NotImplementedError("Solution not implemented")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 1], [1, 0]])  # Order doesn't matter
    
    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[1, 2], [2, 1]])
    
    def test_example3(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 1], [1, 0]])
    
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[2, 4], [4, 2]])
    
    def test_duplicate_numbers(self):
        nums = [1, 1, 1, 1, 1]
        target = 2
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]])

if __name__ == '__main__':
    unittest.main() 