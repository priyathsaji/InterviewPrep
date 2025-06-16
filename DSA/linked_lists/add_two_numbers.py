"""
Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Input Format:
- l1: ListNode - The head of the first linked list
- l2: ListNode - The head of the second linked list

Output Format:
- ListNode - The head of the resulting linked list

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Constraints:
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Time Complexity: O(max(n, m)) where n and m are the lengths of the two lists
Space Complexity: O(max(n, m))
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented as linked lists.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from the nodes or 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            
            # Create new node with the digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

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
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 8])
    
    def test_different_lengths(self):
        l1 = self.create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.create_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])
    
    def test_carry_at_end(self):
        l1 = self.create_linked_list([5])
        l2 = self.create_linked_list([5])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), [0, 1])

if __name__ == '__main__':
    unittest.main() 