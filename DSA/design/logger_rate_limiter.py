"""
Problem Statement:
Design a logger system that receives stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds.

Implement the Logger class:
- Logger() initializes the logger object.
- bool shouldPrintMessage(int timestamp, string message) returns true if the message should be printed in the given timestamp, otherwise returns false.

Input Format:
- timestamp: int - The timestamp in seconds
- message: str - The message to be logged

Output Format:
- bool - True if the message should be printed, False otherwise

Example:
Input:
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output: [null, true, true, false, false, false, true]

Constraints:
- 0 <= timestamp <= 10^9
- Every timestamp will be passed in non-decreasing order (chronological order).
- 1 <= message.length <= 30
- At most 10^4 calls will be made to shouldPrintMessage.

Time Complexity: O(1) for shouldPrintMessage
Space Complexity: O(n) where n is the number of unique messages
"""

class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        We use a dictionary to store the last timestamp for each message.
        """
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestLogger(unittest.TestCase):
    def test_example1(self):
        logger = Logger()
        self.assertTrue(logger.shouldPrintMessage(1, "foo"))
        self.assertTrue(logger.shouldPrintMessage(2, "bar"))
        self.assertFalse(logger.shouldPrintMessage(3, "foo"))
        self.assertFalse(logger.shouldPrintMessage(8, "bar"))
        self.assertFalse(logger.shouldPrintMessage(10, "foo"))
        self.assertTrue(logger.shouldPrintMessage(11, "foo"))
    
    def test_example2(self):
        logger = Logger()
        self.assertTrue(logger.shouldPrintMessage(1, "hello"))
        self.assertTrue(logger.shouldPrintMessage(2, "world"))
        self.assertFalse(logger.shouldPrintMessage(3, "hello"))
        self.assertTrue(logger.shouldPrintMessage(11, "hello"))
    
    def test_same_timestamp(self):
        logger = Logger()
        self.assertTrue(logger.shouldPrintMessage(1, "msg1"))
        self.assertTrue(logger.shouldPrintMessage(1, "msg2"))
        self.assertFalse(logger.shouldPrintMessage(1, "msg1"))
    
    def test_multiple_messages(self):
        logger = Logger()
        messages = ["msg1", "msg2", "msg3", "msg4", "msg5"]
        for i, msg in enumerate(messages):
            self.assertTrue(logger.shouldPrintMessage(i, msg))
        for i, msg in enumerate(messages):
            self.assertFalse(logger.shouldPrintMessage(i + 5, msg))
        for i, msg in enumerate(messages):
            self.assertTrue(logger.shouldPrintMessage(i + 10, msg))

if __name__ == '__main__':
    unittest.main() 