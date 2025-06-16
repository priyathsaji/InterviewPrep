"""
Problem Statement:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input Format:
- heights: List[int] - Array of integers representing the heights of histogram bars

Output Format:
- int - Area of the largest rectangle in the histogram

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4
Explanation: The largest rectangle is shown in the red area, which has an area = 4 units.

Constraints:
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

Time Complexity: O(n) where n is the length of heights
Space Complexity: O(n) where n is the length of heights
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Find the area of the largest rectangle in the histogram.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        heights = [2,1,5,6,2,3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)
    
    def test_example2(self):
        heights = [2,4]
        self.assertEqual(self.solution.largestRectangleArea(heights), 4)
    
    def test_single_bar(self):
        heights = [1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 1)
    
    def test_two_bars(self):
        heights = [1,2]
        self.assertEqual(self.solution.largestRectangleArea(heights), 2)
    
    def test_three_bars(self):
        heights = [1,2,3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 4)
    
    def test_four_bars(self):
        heights = [1,2,3,4]
        self.assertEqual(self.solution.largestRectangleArea(heights), 6)
    
    def test_decreasing_heights(self):
        heights = [4,3,2,1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 6)
    
    def test_alternating_heights(self):
        heights = [1,3,1,3,1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 5)
    
    def test_equal_heights(self):
        heights = [2,2,2,2]
        self.assertEqual(self.solution.largestRectangleArea(heights), 8)
    
    def test_zero_heights(self):
        heights = [0,0,0,0]
        self.assertEqual(self.solution.largestRectangleArea(heights), 0)
    
    def test_large_heights(self):
        heights = [10000,10000,10000]
        self.assertEqual(self.solution.largestRectangleArea(heights), 30000)
    
    def test_mixed_heights(self):
        heights = [1,100,1,100,1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 100)
    
    def test_uneven_heights(self):
        heights = [1,3,5,7,9]
        self.assertEqual(self.solution.largestRectangleArea(heights), 15)
    
    def test_negative_heights(self):
        heights = [-1,-2,-3,-4]
        self.assertEqual(self.solution.largestRectangleArea(heights), 0)

if __name__ == '__main__':
    unittest.main() 