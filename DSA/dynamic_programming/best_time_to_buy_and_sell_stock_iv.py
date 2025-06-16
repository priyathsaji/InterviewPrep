"""
Problem Statement:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input Format:
- prices: List[int] - Array of stock prices
- k: int - Maximum number of transactions allowed

Output Format:
- int - Maximum profit achievable

Example:
Input: prices = [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Input: prices = [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
- 1 <= len(prices) <= 1000
- 0 <= prices[i] <= 1000
- 0 <= k <= 100

Time Complexity: O(n * k) where n is the length of prices
Space Complexity: O(n * k)
"""

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """
        Find the maximum profit with at most k transactions.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        prices = [2,4,1]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 2)
    
    def test_example2(self):
        prices = [3,2,6,5,0,3]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 7)
    
    def test_single_day(self):
        prices = [1]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 0)
    
    def test_two_days(self):
        prices = [1,2]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 1)
    
    def test_three_days(self):
        prices = [1,2,3]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 2)
    
    def test_four_days(self):
        prices = [1,2,3,4]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 3)
    
    def test_decreasing_prices(self):
        prices = [4,3,2,1]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 0)
    
    def test_increasing_prices(self):
        prices = [1,2,3,4]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 3)
    
    def test_alternating_prices(self):
        prices = [1,3,2,4]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 4)
    
    def test_zero_transactions(self):
        prices = [1,2,3,4]
        k = 0
        self.assertEqual(self.solution.maxProfit(k, prices), 0)
    
    def test_large_k(self):
        prices = [1,2,3,4]
        k = 100
        self.assertEqual(self.solution.maxProfit(k, prices), 3)
    
    def test_equal_prices(self):
        prices = [2,2,2,2]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 0)
    
    def test_single_transaction(self):
        prices = [3,3,5,0,0,3,1,4]
        k = 1
        self.assertEqual(self.solution.maxProfit(k, prices), 4)
    
    def test_multiple_transactions(self):
        prices = [3,3,5,0,0,3,1,4]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 6)
    
    def test_complex_sequence(self):
        prices = [1,2,4,2,5,7,2,4,9,0]
        k = 2
        self.assertEqual(self.solution.maxProfit(k, prices), 13)

if __name__ == '__main__':
    unittest.main() 