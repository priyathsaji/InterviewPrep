"""
Problem Statement:
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.

Input Format:
- head: Node - The head of the multilevel doubly linked list

Output Format:
- Node - The head of the flattened doubly linked list

Example:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Constraints:
- The number of nodes will not exceed 1000
- 1 <= Node.val <= 10^5

Time Complexity: O(n) where n is the total number of nodes
Space Complexity: O(1)
"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        """
        Flatten a multilevel doubly linked list.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_multilevel_list(self, values, children):
        if not values:
            return None
            
        # Create nodes
        nodes = []
        for val in values:
            if val is not None:
                nodes.append(Node(val))
            else:
                nodes.append(None)
        
        # Connect nodes
        for i in range(len(nodes) - 1):
            if nodes[i] and nodes[i + 1]:
                nodes[i].next = nodes[i + 1]
                nodes[i + 1].prev = nodes[i]
        
        # Add children
        for i, child_idx in enumerate(children):
            if child_idx is not None and nodes[i]:
                nodes[i].child = nodes[child_idx]
        
        return nodes[0] if nodes else None
    
    def list_to_values(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values
    
    def test_example1(self):
        values = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
        children = [None, None, 9, None, None, None, None, None, None, None, 11, None, None, None, None, None, None]
        head = self.create_multilevel_list(values, children)
        flattened = self.solution.flatten(head)
        self.assertEqual(self.list_to_values(flattened), [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6])
    
    def test_empty_list(self):
        head = None
        flattened = self.solution.flatten(head)
        self.assertIsNone(flattened)
    
    def test_no_children(self):
        values = [1, 2, 3]
        children = [None, None, None]
        head = self.create_multilevel_list(values, children)
        flattened = self.solution.flatten(head)
        self.assertEqual(self.list_to_values(flattened), [1, 2, 3])

if __name__ == '__main__':
    unittest.main() 