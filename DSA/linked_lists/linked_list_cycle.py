"""
Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Input Format:
- head: ListNode - The head of the linked list

Output Format:
- bool - True if there is a cycle in the linked list, False otherwise

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Constraints:
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Detect if there is a cycle in the linked list using Floyd's Cycle-Finding Algorithm.
        """
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_linked_list_with_cycle(self, values, pos):
        if not values:
            return None
            
        head = ListNode(values[0])
        current = head
        nodes = [head]
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
            nodes.append(current)
            
        if pos != -1:
            current.next = nodes[pos]
            
        return head
    
    def test_example1(self):
        head = self.create_linked_list_with_cycle([3, 2, 0, -4], 1)
        self.assertTrue(self.solution.hasCycle(head))
    
    def test_example2(self):
        head = self.create_linked_list_with_cycle([1, 2], 0)
        self.assertTrue(self.solution.hasCycle(head))
    
    def test_no_cycle(self):
        head = self.create_linked_list_with_cycle([1], -1)
        self.assertFalse(self.solution.hasCycle(head))
    
    def test_empty_list(self):
        head = None
        self.assertFalse(self.solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main() 