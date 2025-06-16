"""
Problem Statement:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Input Format:
- nums: List[int] - A rotated sorted array of unique integers

Output Format:
- int - The minimum element in the array

Example:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array.
        """
        raise NotImplementedError("Solution not implemented")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 1)
    
    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 0)
    
    def test_example3(self):
        nums = [11, 13, 15, 17]
        self.assertEqual(self.solution.findMin(nums), 11)
    
    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.findMin(nums), 1)
    
    def test_two_elements(self):
        nums = [2, 1]
        self.assertEqual(self.solution.findMin(nums), 1)
    
    def test_not_rotated(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.findMin(nums), 1)
    
    def test_rotated_once(self):
        nums = [5, 1, 2, 3, 4]
        self.assertEqual(self.solution.findMin(nums), 1)
    
    def test_negative_numbers(self):
        nums = [-3, -2, -1, -5, -4]
        self.assertEqual(self.solution.findMin(nums), -5)

if __name__ == '__main__':
    unittest.main() 