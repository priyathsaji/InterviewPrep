"""
Problem Statement:
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Input Format:
- piles: List[int] - Array of integers representing the number of stones in each pile

Output Format:
- bool - True if Alice wins, False if Bob wins

Example:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Input: piles = [3,7,2,3]
Output: true
Explanation: Alice can take either the first or last 3. In either case, she can force a win.

Constraints:
- 2 <= len(piles) <= 500
- len(piles) is even
- 1 <= piles[i] <= 500
- sum(piles) is odd

Time Complexity: O(n²) where n is the number of piles
Space Complexity: O(n²) where n is the number of piles
"""

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """
        Determine if Alice can win the stone game assuming both players play optimally.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        piles = [5,3,4,5]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_example2(self):
        piles = [3,7,2,3]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_two_piles(self):
        piles = [1,2]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_four_piles(self):
        piles = [1,2,3,4]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_six_piles(self):
        piles = [1,2,3,4,5,6]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_equal_piles(self):
        piles = [2,2,2,2]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_alternating_piles(self):
        piles = [1,3,1,3]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_increasing_piles(self):
        piles = [1,2,3,4,5,6]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_decreasing_piles(self):
        piles = [6,5,4,3,2,1]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_large_piles(self):
        piles = [100,200,300,400]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_small_piles(self):
        piles = [1,1,1,1]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_mixed_piles(self):
        piles = [1,100,1,100]
        self.assertTrue(self.solution.stoneGame(piles))
    
    def test_uneven_piles(self):
        piles = [1,3,5,7]
        self.assertTrue(self.solution.stoneGame(piles))

if __name__ == '__main__':
    unittest.main() 