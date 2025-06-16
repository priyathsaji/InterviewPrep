"""
Problem Statement:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Input Format:
- head: ListNode - The head of the linked list

Output Format:
- None (modify the list in-place)

Example:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorder the linked list by:
        1. Finding the middle
        2. Reversing the second half
        3. Merging the two halves
        """
        if not head or not head.next:
            return
            
        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        # Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

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
        head = self.create_linked_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 4, 2, 3])
    
    def test_example2(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 5, 2, 4, 3])
    
    def test_two_nodes(self):
        head = self.create_linked_list([1, 2])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2])

if __name__ == '__main__':
    unittest.main() 