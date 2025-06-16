"""
Problem Statement:
Given an integer n, return the number of prime numbers that are strictly less than n.

Input Format:
- n: int - The upper bound (exclusive)

Output Format:
- int - The count of prime numbers less than n

Example:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Constraints:
- 0 <= n <= 5 * 10^6

Time Complexity: O(n log log n) - Sieve of Eratosthenes
Space Complexity: O(n)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Count prime numbers using the Sieve of Eratosthenes algorithm.
        """
        if n <= 2:
            return 0
            
        # Initialize array of numbers from 0 to n-1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Mark multiples of primes as non-prime
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        n = 10
        self.assertEqual(self.solution.countPrimes(n), 4)
    
    def test_example2(self):
        n = 0
        self.assertEqual(self.solution.countPrimes(n), 0)
    
    def test_example3(self):
        n = 1
        self.assertEqual(self.solution.countPrimes(n), 0)
    
    def test_large_number(self):
        n = 100
        self.assertEqual(self.solution.countPrimes(n), 25)  # There are 25 primes less than 100

if __name__ == '__main__':
    unittest.main() 