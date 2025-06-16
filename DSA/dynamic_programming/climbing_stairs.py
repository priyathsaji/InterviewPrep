"""
Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input Format:
- n: int - The number of steps to reach the top

Output Format:
- int - The number of distinct ways to climb to the top

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb n stairs using dynamic programming.
        This is essentially the Fibonacci sequence.
        """
        if n <= 2:
            return n
            
        prev1, prev2 = 2, 1  # For n=2 and n=1
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 3
        self.assertEqual(self.solution.climbStairs(n), 3)
    
    def test_example2(self):
        n = 2
        self.assertEqual(self.solution.climbStairs(n), 2)
    
    def test_example3(self):
        n = 1
        self.assertEqual(self.solution.climbStairs(n), 1)
    
    def test_example4(self):
        n = 4
        self.assertEqual(self.solution.climbStairs(n), 5)

if __name__ == '__main__':
    unittest.main() 