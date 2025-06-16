"""
Problem Statement:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Input Format:
- height: List[int] - An array of non-negative integers representing the heights

Output Format:
- int - The maximum area of water that can be contained

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing height[1] = 8 and height[8] = 7,
which gives us 7 * (8-1) = 49.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum area of water that can be contained using two pointers.
        """
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)
    
    def test_example2(self):
        height = [1, 1]
        self.assertEqual(self.solution.maxArea(height), 1)
    
    def test_example3(self):
        height = [4, 3, 2, 1, 4]
        self.assertEqual(self.solution.maxArea(height), 16)
    
    def test_example4(self):
        height = [1, 2, 1]
        self.assertEqual(self.solution.maxArea(height), 2)
    
    def test_same_height(self):
        height = [5, 5, 5, 5]
        self.assertEqual(self.solution.maxArea(height), 15)

if __name__ == '__main__':
    unittest.main() 