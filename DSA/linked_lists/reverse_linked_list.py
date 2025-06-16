"""
Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input Format:
- head: ListNode - The head of the linked list

Output Format:
- ListNode - The head of the reversed linked list

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:
- The number of nodes in the list is in the range [0, 5000]
- -5000 <= Node.val <= 5000

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverse a singly linked list iteratively.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_example1(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])
    
    def test_example2(self):
        head = self.create_linked_list([1, 2])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [2, 1])
    
    def test_empty_list(self):
        head = None
        reversed_head = self.solution.reverseList(head)
        self.assertIsNone(reversed_head)

if __name__ == '__main__':
    unittest.main() 