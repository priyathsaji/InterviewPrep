"""
Problem Statement:
Design a rate limiter that limits the number of requests per time window.

Implement the RateLimiter class:
- RateLimiter(int requests, int seconds) initializes the rate limiter with the maximum number of requests allowed in the given time window.
- boolean shouldAllowRequest(int timestamp) returns true if the request should be allowed, false otherwise.

Input Format:
- requests: int - Maximum number of requests allowed in the time window
- seconds: int - Time window in seconds
- timestamp: int - Current timestamp in seconds

Output Format:
- bool - True if the request should be allowed, False otherwise

Example:
Input:
["RateLimiter", "shouldAllowRequest", "shouldAllowRequest", "shouldAllowRequest", "shouldAllowRequest"]
[[3, 5], [1], [2], [3], [8]]
Output: [null, true, true, true, true]

Constraints:
- 1 <= requests <= 100
- 1 <= seconds <= 100
- 1 <= timestamp <= 10^9
- At most 10^4 calls will be made to shouldAllowRequest.

Time Complexity: O(1) for shouldAllowRequest
Space Complexity: O(n) where n is the number of requests in the time window
"""

from collections import deque

class RateLimiter:
    def __init__(self, requests: int, seconds: int):
        """
        Initialize the rate limiter with the given parameters.
        We use a deque to store timestamps of requests within the time window.
        """
        self.requests = requests  # Maximum number of requests allowed
        self.seconds = seconds    # Time window in seconds
        self.timestamps = deque() # Store timestamps of requests
    
    def shouldAllowRequest(self, timestamp: int) -> bool:
        """
        Check if the request should be allowed based on the rate limiting rules.
        """
        # Remove timestamps that are outside the current time window
        while self.timestamps and timestamp - self.timestamps[0] >= self.seconds:
            self.timestamps.popleft()
        
        # Check if we can allow more requests
        if len(self.timestamps) < self.requests:
            self.timestamps.append(timestamp)
            return True
        
        return False

import unittest

class TestRateLimiter(unittest.TestCase):
    def test_example1(self):
        limiter = RateLimiter(3, 5)
        self.assertTrue(limiter.shouldAllowRequest(1))
        self.assertTrue(limiter.shouldAllowRequest(2))
        self.assertTrue(limiter.shouldAllowRequest(3))
        self.assertFalse(limiter.shouldAllowRequest(4))
        self.assertTrue(limiter.shouldAllowRequest(8))
    
    def test_example2(self):
        limiter = RateLimiter(2, 3)
        self.assertTrue(limiter.shouldAllowRequest(1))
        self.assertTrue(limiter.shouldAllowRequest(2))
        self.assertFalse(limiter.shouldAllowRequest(3))
        self.assertTrue(limiter.shouldAllowRequest(4))
    
    def test_single_request(self):
        limiter = RateLimiter(1, 5)
        self.assertTrue(limiter.shouldAllowRequest(1))
        self.assertFalse(limiter.shouldAllowRequest(2))
        self.assertTrue(limiter.shouldAllowRequest(6))
    
    def test_concurrent_requests(self):
        limiter = RateLimiter(5, 10)
        for i in range(5):
            self.assertTrue(limiter.shouldAllowRequest(i))
        self.assertFalse(limiter.shouldAllowRequest(5))
        self.assertTrue(limiter.shouldAllowRequest(10))

if __name__ == '__main__':
    unittest.main() 