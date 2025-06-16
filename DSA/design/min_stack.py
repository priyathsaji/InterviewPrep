"""
Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Input Format:
- val: int - The value to push onto the stack

Output Format:
- int - The value for top and getMin operations

Example:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        We use two stacks:
        1. Main stack for regular operations
        2. Min stack to keep track of minimum values
        """

    
    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        If the value is less than or equal to current minimum, push it to min_stack.
        """
        raise NotImplementedError("Solution not implemented")
    
    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        If the popped element is the minimum, remove it from min_stack as well.
        """
        raise NotImplementedError("Solution not implemented")
    
    def top(self) -> int:
        """
        Get the top element.
        """
        raise NotImplementedError("Solution not implemented")
    
    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestMinStack(unittest.TestCase):
    def test_example1(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)
    
    def test_example2(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        self.assertEqual(minStack.top(), 2)
        self.assertEqual(minStack.getMin(), 1)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 1)
    
    def test_duplicate_minimum(self):
        minStack = MinStack()
        minStack.push(5)
        minStack.push(3)
        minStack.push(3)
        self.assertEqual(minStack.getMin(), 3)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 3)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 5)

if __name__ == '__main__':
    unittest.main() 