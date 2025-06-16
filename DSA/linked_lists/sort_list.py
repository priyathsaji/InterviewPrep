"""
Problem Statement:
Given the head of a linked list, return the list after sorting it in ascending order.

Input Format:
- head: ListNode - The head of the linked list

Output Format:
- ListNode - The head of the sorted linked list

Example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Constraints:
- The number of nodes in the list is in the range [0, 5 * 10^4]
- -10^5 <= Node.val <= 10^5

Time Complexity: O(n log n)
Space Complexity: O(log n) for recursion stack
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        Sort the linked list using merge sort algorithm.
        """
        if not head or not head.next:
            return head
            
        # Find the middle of the list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        mid = slow.next
        slow.next = None
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        """
        Merge two sorted linked lists.
        """
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
            
        # Attach remaining nodes
        current.next = left if left else right
        
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
        head = self.create_linked_list([4, 2, 1, 3])
        sorted_head = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(sorted_head), [1, 2, 3, 4])
    
    def test_example2(self):
        head = self.create_linked_list([-1, 5, 3, 4, 0])
        sorted_head = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(sorted_head), [-1, 0, 3, 4, 5])
    
    def test_empty_list(self):
        head = None
        sorted_head = self.solution.sortList(head)
        self.assertIsNone(sorted_head)
    
    def test_single_node(self):
        head = self.create_linked_list([1])
        sorted_head = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(sorted_head), [1])

if __name__ == '__main__':
    unittest.main() 