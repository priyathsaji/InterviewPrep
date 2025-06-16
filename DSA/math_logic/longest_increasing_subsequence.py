"""
Problem Statement:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input Format:
- nums: List[int] - Array of integers

Output Format:
- int - Length of the longest increasing subsequence

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Find the length of the longest increasing subsequence using binary search.
        We maintain a list of the smallest possible tail values for all increasing subsequences
        of different lengths.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_example2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)
    
    def test_example3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)
    
    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)
    
    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

if __name__ == '__main__':
    unittest.main() 