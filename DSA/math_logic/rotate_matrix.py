"""
Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

Input Format:
- matrix: List[List[int]] - n x n matrix to rotate

Output Format:
- None (modify the matrix in-place)

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise in-place.
        The rotation can be done in two steps:
        1. Transpose the matrix
        2. Reverse each row
        """

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_example2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_single_element(self):
        matrix = [[1]]
        expected = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_2x2_matrix(self):
        matrix = [[1,2],[3,4]]
        expected = [[3,1],[4,2]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

if __name__ == '__main__':
    unittest.main() 