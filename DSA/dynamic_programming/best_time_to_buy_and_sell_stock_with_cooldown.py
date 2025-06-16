"""
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

1. After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
2. You cannot engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input Format:
- prices: List[int] - Array of stock prices

Output Format:
- int - Maximum profit achievable

Example:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Input: prices = [1]
Output: 0
Explanation: With one price, we cannot make any transactions.

Constraints:
- 1 <= len(prices) <= 5000
- 0 <= prices[i] <= 1000

Time Complexity: O(n) where n is the length of prices
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Find the maximum profit with cooldown period.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        prices = [1,2,3,0,2]
        self.assertEqual(self.solution.maxProfit(prices), 3)
    
    def test_example2(self):
        prices = [1]
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_two_days(self):
        prices = [1,2]
        self.assertEqual(self.solution.maxProfit(prices), 1)
    
    def test_three_days(self):
        prices = [1,2,3]
        self.assertEqual(self.solution.maxProfit(prices), 2)
    
    def test_four_days(self):
        prices = [1,2,3,4]
        self.assertEqual(self.solution.maxProfit(prices), 3)
    
    def test_decreasing_prices(self):
        prices = [4,3,2,1]
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_increasing_prices(self):
        prices = [1,2,3,4]
        self.assertEqual(self.solution.maxProfit(prices), 3)
    
    def test_alternating_prices(self):
        prices = [1,3,2,4]
        self.assertEqual(self.solution.maxProfit(prices), 3)
    
    def test_equal_prices(self):
        prices = [2,2,2,2]
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_single_transaction(self):
        prices = [3,3,5,0,0,3,1,4]
        self.assertEqual(self.solution.maxProfit(prices), 6)
    
    def test_multiple_transactions(self):
        prices = [3,3,5,0,0,3,1,4]
        self.assertEqual(self.solution.maxProfit(prices), 6)
    
    def test_complex_sequence(self):
        prices = [1,2,4,2,5,7,2,4,9,0]
        self.assertEqual(self.solution.maxProfit(prices), 15)
    
    def test_cooldown_required(self):
        prices = [1,2,4,2,5,7,2,4,9,0]
        self.assertEqual(self.solution.maxProfit(prices), 15)
    
    def test_no_profit_possible(self):
        prices = [5,4,3,2,1]
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_single_price_change(self):
        prices = [1,2,1,2,1]
        self.assertEqual(self.solution.maxProfit(prices), 1)

if __name__ == '__main__':
    unittest.main() 