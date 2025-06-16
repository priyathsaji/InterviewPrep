"""
Problem Statement:
Given a binary tree, we install cameras on the nodes of the tree. Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Input Format:
- root: TreeNode - Root of the binary tree

Output Format:
- int - Minimum number of cameras needed

Example:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is sufficient to monitor all nodes if placed at the root.

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
- Node.val == 0 for all nodes

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
    def minCameraCover(self, root: TreeNode) -> int:
        """
        Find the minimum number of cameras needed to monitor all nodes of the tree.
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
        root = self.create_tree([0,0,None,0,0])
        self.assertEqual(self.solution.minCameraCover(root), 1)
    
    def test_example2(self):
        root = self.create_tree([0,0,None,0,None,0,None,None,0])
        self.assertEqual(self.solution.minCameraCover(root), 2)
    
    def test_single_node(self):
        root = self.create_tree([0])
        self.assertEqual(self.solution.minCameraCover(root), 1)
    
    def test_two_nodes(self):
        root = self.create_tree([0,0])
        self.assertEqual(self.solution.minCameraCover(root), 1)
    
    def test_three_nodes(self):
        root = self.create_tree([0,0,0])
        self.assertEqual(self.solution.minCameraCover(root), 1)
    
    def test_four_nodes(self):
        root = self.create_tree([0,0,0,0])
        self.assertEqual(self.solution.minCameraCover(root), 1)
    
    def test_five_nodes(self):
        root = self.create_tree([0,0,0,0,0])
        self.assertEqual(self.solution.minCameraCover(root), 2)
    
    def test_skewed_tree(self):
        root = self.create_tree([0,0,None,0,None,0])
        self.assertEqual(self.solution.minCameraCover(root), 2)
    
    def test_complete_tree(self):
        root = self.create_tree([0,0,0,0,0,0,0])
        self.assertEqual(self.solution.minCameraCover(root), 2)
    
    def test_large_tree(self):
        values = [0] * 15
        root = self.create_tree(values)
        self.assertEqual(self.solution.minCameraCover(root), 3)
    
    def test_alternating_tree(self):
        root = self.create_tree([0,0,None,0,None,0,None,0])
        self.assertEqual(self.solution.minCameraCover(root), 2)

if __name__ == '__main__':
    unittest.main() 