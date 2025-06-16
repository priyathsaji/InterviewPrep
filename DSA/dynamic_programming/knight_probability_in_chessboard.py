"""
Problem Statement:
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n-1, n-1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Return the probability that the knight remains on the board after it has stopped moving.

Input Format:
- n: int - Size of the chessboard (n x n)
- k: int - Number of moves
- row: int - Starting row position
- column: int - Starting column position

Output Format:
- float - Probability that the knight remains on the board

Example:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board. From each of those positions, there are also two moves that will keep the knight on the board. The total probability the knight stays on the board is 0.0625.

Input: n = 1, k = 0, row = 0, column = 0
Output: 1.0
Explanation: The knight cannot move, so it stays on the board.

Constraints:
- 1 <= n <= 25
- 0 <= k <= 100
- 0 <= row, column < n

Time Complexity: O(k * n^2)
Space Complexity: O(k * n^2)
"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        Calculate the probability that the knight remains on the board after k moves.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n, k, row, column = 3, 2, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.0625)
    
    def test_example2(self):
        n, k, row, column = 1, 0, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 1.0)
    
    def test_single_move(self):
        n, k, row, column = 3, 1, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.25)
    
    def test_center_position(self):
        n, k, row, column = 3, 2, 1, 1
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 1.0)
    
    def test_corner_position(self):
        n, k, row, column = 2, 1, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.0)
    
    def test_edge_position(self):
        n, k, row, column = 3, 1, 0, 1
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.5)
    
    def test_large_board(self):
        n, k, row, column = 8, 30, 6, 4
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.000190525588)
    
    def test_zero_moves(self):
        n, k, row, column = 5, 0, 2, 2
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 1.0)
    
    def test_single_cell_board(self):
        n, k, row, column = 1, 1, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.0)
    
    def test_two_by_two_board(self):
        n, k, row, column = 2, 1, 0, 0
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.0)
    
    def test_three_by_three_board(self):
        n, k, row, column = 3, 1, 1, 1
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 1.0)
    
    def test_four_by_four_board(self):
        n, k, row, column = 4, 2, 1, 1
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 0.875)
    
    def test_five_by_five_board(self):
        n, k, row, column = 5, 2, 2, 2
        self.assertAlmostEqual(self.solution.knightProbability(n, k, row, column), 1.0)

if __name__ == '__main__':
    unittest.main() 