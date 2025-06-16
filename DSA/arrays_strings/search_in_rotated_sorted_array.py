"""
Problem Statement:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Input Format:
- nums: List[int] - A rotated sorted array of distinct integers
- target: int - The target value to find

Output Format:
- int - The index of target in nums, or -1 if not found

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in a rotated sorted array.
        """
        raise NotImplementedError("Solution not implemented")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)
    
    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)
    
    def test_example3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)
    
    def test_not_rotated(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)
    
    def test_rotated_at_end(self):
        nums = [2, 3, 4, 5, 1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 4)
    
    def test_rotated_at_start(self):
        nums = [5, 1, 2, 3, 4]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 0)
    
    def test_target_not_in_array(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 8
        self.assertEqual(self.solution.search(nums, target), -1)

if __name__ == '__main__':
    unittest.main() 