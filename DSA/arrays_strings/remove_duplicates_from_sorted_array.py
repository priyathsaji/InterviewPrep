"""
Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
2. The remaining elements of nums are not important as well as the size of nums.
3. Return k.

Input Format:
- nums: List[int] - A sorted array of integers

Output Format:
- int - The number of unique elements after removing duplicates

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place and return the number of unique elements.
        """
        raise NotImplementedError("Solution not implemented")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])
    
    def test_single_element(self):
        nums = [1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])
    
    def test_all_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

if __name__ == '__main__':
    unittest.main() 