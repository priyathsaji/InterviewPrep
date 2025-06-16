"""
Problem Statement:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input Format:
- coins: List[int] - Array of coin denominations
- amount: int - Target amount to make up

Output Format:
- int - Minimum number of coins needed to make up the amount, or -1 if impossible

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: It's impossible to make up amount 3 with only coin of denomination 2.

Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed to make up amount 0.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Find the minimum number of coins needed to make up the given amount.
        """
        raise NotImplementedError("Solution not implemented")

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        coins = [1,2,5]
        amount = 11
        self.assertEqual(self.solution.coinChange(coins, amount), 3)
    
    def test_example2(self):
        coins = [2]
        amount = 3
        self.assertEqual(self.solution.coinChange(coins, amount), -1)
    
    def test_example3(self):
        coins = [1]
        amount = 0
        self.assertEqual(self.solution.coinChange(coins, amount), 0)
    
    def test_single_coin(self):
        coins = [1]
        amount = 5
        self.assertEqual(self.solution.coinChange(coins, amount), 5)
    
    def test_multiple_coins_same_denomination(self):
        coins = [1,1,1,1]
        amount = 4
        self.assertEqual(self.solution.coinChange(coins, amount), 4)
    
    def test_large_amount(self):
        coins = [1,2,5]
        amount = 100
        self.assertEqual(self.solution.coinChange(coins, amount), 20)
    
    def test_impossible_amount(self):
        coins = [3,5]
        amount = 7
        self.assertEqual(self.solution.coinChange(coins, amount), -1)
    
    def test_zero_coins(self):
        coins = []
        amount = 5
        self.assertEqual(self.solution.coinChange(coins, amount), -1)
    
    def test_large_coin_values(self):
        coins = [1, 100, 1000]
        amount = 1001
        self.assertEqual(self.solution.coinChange(coins, amount), 2)
    
    def test_duplicate_coin_values(self):
        coins = [1,1,2,2,5,5]
        amount = 11
        self.assertEqual(self.solution.coinChange(coins, amount), 3)
    
    def test_minimum_possible_coins(self):
        coins = [1,2,5,10]
        amount = 18
        self.assertEqual(self.solution.coinChange(coins, amount), 4)

if __name__ == '__main__':
    unittest.main() 