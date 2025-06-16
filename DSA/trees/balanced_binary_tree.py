"""
Problem Statement:
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- bool - True if the tree is height-balanced, False otherwise

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: The tree is:
    3
   / \
  9  20
     / \
    15  7
The left and right subtrees of every node differ in height by no more than 1.

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Explanation: The tree is:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
The left subtree of node 2 has height 3, while the right subtree has height 1.

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if the binary tree is height-balanced.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [3,9,20,null,null,15,7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_example2(self):
        # Create tree: [1,2,2,3,3,null,null,4,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        
        self.assertFalse(self.solution.isBalanced(root))
    
    def test_empty_tree(self):
        root = None
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertFalse(self.solution.isBalanced(root))
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertFalse(self.solution.isBalanced(root))
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_deep_tree(self):
        # Create a deep tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        self.assertTrue(self.solution.isBalanced(root))
    
    def test_unbalanced_deep_tree(self):
        # Create an unbalanced deep tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        root.left.left.left.left = TreeNode(16)  # Makes the tree unbalanced
        
        self.assertFalse(self.solution.isBalanced(root))

if __name__ == '__main__':
    unittest.main() 