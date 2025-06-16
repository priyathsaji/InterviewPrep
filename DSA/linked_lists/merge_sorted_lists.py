"""
Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input Format:
- list1: ListNode - The head of the first sorted linked list
- list2: ListNode - The head of the second sorted linked list

Output Format:
- ListNode - The head of the merged sorted linked list

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

Time Complexity: O(n + m) where n and m are the lengths of the two lists
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists into one sorted linked list.
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes from either list
        current.next = list1 if list1 else list2
        
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
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 4])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])
    
    def test_empty_lists(self):
        list1 = None
        list2 = None
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertIsNone(merged)
    
    def test_one_empty_list(self):
        list1 = self.create_linked_list([1, 2, 3])
        list2 = None
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged), [1, 2, 3])

if __name__ == '__main__':
    unittest.main() 