"""
Problem Statement:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Input Format:
- root: TreeNode - Root of the binary tree

Output Format:
- int - Maximum amount of money that can be robbed

Example:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        Find the maximum amount of money that can be robbed without alerting the police.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_tree(self, values):
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def test_example1(self):
        root = self.create_tree([3,2,3,None,3,None,1])
        self.assertEqual(self.solution.rob(root), 7)
    
    def test_example2(self):
        root = self.create_tree([3,4,5,1,3,None,1])
        self.assertEqual(self.solution.rob(root), 9)
    
    def test_single_node(self):
        root = self.create_tree([3])
        self.assertEqual(self.solution.rob(root), 3)
    
    def test_two_nodes(self):
        root = self.create_tree([3,4])
        self.assertEqual(self.solution.rob(root), 4)
    
    def test_three_nodes(self):
        root = self.create_tree([3,4,5])
        self.assertEqual(self.solution.rob(root), 9)
    
    def test_complete_tree(self):
        root = self.create_tree([3,4,5,1,3,6,7])
        self.assertEqual(self.solution.rob(root), 18)
    
    def test_skewed_tree(self):
        root = self.create_tree([3,4,None,5,None,6])
        self.assertEqual(self.solution.rob(root), 11)
    
    def test_alternating_values(self):
        root = self.create_tree([1,2,3,4,5,6,7])
        self.assertEqual(self.solution.rob(root), 23)
    
    def test_large_values(self):
        root = self.create_tree([100,200,300,400,500])
        self.assertEqual(self.solution.rob(root), 800)
    
    def test_negative_values(self):
        root = self.create_tree([-1,-2,-3])
        self.assertEqual(self.solution.rob(root), -1)
    
    def test_mixed_values(self):
        root = self.create_tree([5,3,6,1,4,None,7])
        self.assertEqual(self.solution.rob(root), 18)

if __name__ == '__main__':
    unittest.main() 