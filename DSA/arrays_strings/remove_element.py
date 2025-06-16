"""
Problem Statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
1. Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
2. The remaining elements of nums are not important as well as the size of nums.
3. Return k.

Input Format:
- nums: List[int] - An array of integers
- val: int - The value to remove

Output Format:
- int - The number of elements in nums which are not equal to val

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in nums in-place and return the new length.
        """
        raise NotImplementedError("Solution not implemented")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [2, 2])
    
    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])
    
    def test_empty_array(self):
        nums = []
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])
    
    def test_no_matches(self):
        nums = [1, 2, 3, 4]
        val = 5
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_all_matches(self):
        nums = [1, 1, 1, 1]
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

if __name__ == '__main__':
    unittest.main() 