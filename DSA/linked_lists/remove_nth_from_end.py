"""
Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input Format:
- head: ListNode - The head of the linked list
- n: int - The position from the end to remove (1-indexed)

Output Format:
- ListNode - The head of the modified linked list

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The 2nd node from the end is 4, so we remove it.

Constraints:
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Remove the nth node from the end of the linked list using two pointers.
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
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 5])
    
    def test_remove_first_node(self):
        head = self.create_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [2])
    
    def test_single_node(self):
        head = self.create_linked_list([1])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 