"""
Problem Statement:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

Input Format:
- headA: ListNode - The head of the first linked list
- headB: ListNode - The head of the second linked list

Output Format:
- ListNode - The intersection node if exists, None otherwise

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).

Constraints:
- The number of nodes of listA is in the m
- The number of nodes of listB is in the n
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Find the intersection node of two linked lists using two pointers.
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
    
    def create_intersection_lists(self, listA, listB, skipA, skipB):
        if not listA or not listB:
            return None, None
            
        # Create the common part
        common = self.create_linked_list(listA[skipA:])
        
        # Create list A
        headA = self.create_linked_list(listA[:skipA])
        if headA:
            current = headA
            while current.next:
                current = current.next
            current.next = common
        else:
            headA = common
            
        # Create list B
        headB = self.create_linked_list(listB[:skipB])
        if headB:
            current = headB
            while current.next:
                current = current.next
            current.next = common
        else:
            headB = common
            
        return headA, headB
    
    def test_example1(self):
        listA = [4, 1, 8, 4, 5]
        listB = [5, 6, 1, 8, 4, 5]
        skipA = 2
        skipB = 3
        headA, headB = self.create_intersection_lists(listA, listB, skipA, skipB)
        intersection = self.solution.getIntersectionNode(headA, headB)
        self.assertEqual(intersection.val, 8)
    
    def test_no_intersection(self):
        headA = self.create_linked_list([2, 6, 4])
        headB = self.create_linked_list([1, 5])
        intersection = self.solution.getIntersectionNode(headA, headB)
        self.assertIsNone(intersection)
    
    def test_same_list(self):
        head = self.create_linked_list([1, 2, 3])
        intersection = self.solution.getIntersectionNode(head, head)
        self.assertEqual(intersection, head)

if __name__ == '__main__':
    unittest.main() 