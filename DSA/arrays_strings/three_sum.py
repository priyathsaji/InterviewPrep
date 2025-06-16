"""
Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input Format:
- nums: List[int] - An array of integers

Output Format:
- List[List[int]] - List of unique triplets that sum to zero

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
The triplets that sum to zero are:
- [-1,0,1]
- [-1,-1,2]
Note that the order of the output and the order of the triplets does not matter.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List
import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum to zero.
        Using two-pointer technique after sorting the array.
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(len(result), len(expected))
        for triplet in expected:
            self.assertIn(triplet, result)
    
    def test_example2(self):
        nums = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])
    
    def test_example3(self):
        nums = [0]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])
    
    def test_all_zeros(self):
        nums = [0, 0, 0]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [[0, 0, 0]])
    
    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main() 