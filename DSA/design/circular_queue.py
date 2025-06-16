"""
Problem Statement:
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle.

Implement the MyCircularQueue class:
- MyCircularQueue(int k) Initializes the object with the size of the queue to be k.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

Input Format:
- k: int - The size of the queue
- value: int - The value to enqueue

Output Format:
- bool - True/False for enQueue, deQueue, isEmpty, and isFull operations
- int - The value for Front and Rear operations

Example:
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output: [null, true, true, true, false, 3, true, true, true, 4]

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

Time Complexity: O(1) for all operations
Space Complexity: O(k) where k is the size of the queue
"""

class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True
    
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0
    
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.size

import unittest

class TestCircularQueue(unittest.TestCase):
    def test_example1(self):
        queue = MyCircularQueue(3)
        self.assertTrue(queue.enQueue(1))
        self.assertTrue(queue.enQueue(2))
        self.assertTrue(queue.enQueue(3))
        self.assertFalse(queue.enQueue(4))
        self.assertEqual(queue.Rear(), 3)
        self.assertTrue(queue.isFull())
        self.assertTrue(queue.deQueue())
        self.assertTrue(queue.enQueue(4))
        self.assertEqual(queue.Rear(), 4)
    
    def test_example2(self):
        queue = MyCircularQueue(2)
        self.assertTrue(queue.enQueue(1))
        self.assertTrue(queue.enQueue(2))
        self.assertFalse(queue.enQueue(3))
        self.assertEqual(queue.Front(), 1)
        self.assertEqual(queue.Rear(), 2)
        self.assertTrue(queue.deQueue())
        self.assertTrue(queue.enQueue(3))
        self.assertEqual(queue.Front(), 2)
        self.assertEqual(queue.Rear(), 3)
    
    def test_empty_queue(self):
        queue = MyCircularQueue(3)
        self.assertTrue(queue.isEmpty())
        self.assertFalse(queue.isFull())
        self.assertEqual(queue.Front(), -1)
        self.assertEqual(queue.Rear(), -1)
        self.assertFalse(queue.deQueue())
    
    def test_full_queue(self):
        queue = MyCircularQueue(2)
        self.assertTrue(queue.enQueue(1))
        self.assertTrue(queue.enQueue(2))
        self.assertTrue(queue.isFull())
        self.assertFalse(queue.isEmpty())
        self.assertFalse(queue.enQueue(3))
        self.assertEqual(queue.Front(), 1)
        self.assertEqual(queue.Rear(), 2)

if __name__ == '__main__':
    unittest.main() 