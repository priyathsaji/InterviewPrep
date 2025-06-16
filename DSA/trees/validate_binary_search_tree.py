"""
Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- bool - True if the tree is a valid BST, False otherwise

Example:
Input: root = [2,1,3]
Output: True
Explanation: The tree is a valid BST because:
- The left subtree (1) contains only nodes with values less than 2
- The right subtree (3) contains only nodes with values greater than 2
- Both subtrees are valid BSTs

Input: root = [5,1,4,null,null,3,6]
Output: False
Explanation: The root node's value is 5 but its right child's value is 4, which violates the BST property.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if the binary tree is a valid BST.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [2,1,3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_example2(self):
        # Create tree: [5,1,4,null,null,3,6]
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        
        self.assertFalse(self.solution.isValidBST(root))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_empty_tree(self):
        root = None
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_valid_bst(self):
        # Create tree: [3,1,5,0,2,4,6]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(6)
        
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_invalid_bst(self):
        # Create tree: [3,1,5,0,2,4,2]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(2)
        
        self.assertFalse(self.solution.isValidBST(root))
    
    def test_duplicate_values(self):
        # Create tree: [2,2,2]
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        
        self.assertFalse(self.solution.isValidBST(root))
    
    def test_large_values(self):
        # Create tree: [2147483647,2147483646,2147483648]
        root = TreeNode(2147483647)
        root.left = TreeNode(2147483646)
        root.right = TreeNode(2147483648)
        
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_negative_values(self):
        # Create tree: [-10,-20,-5]
        root = TreeNode(-10)
        root.left = TreeNode(-20)
        root.right = TreeNode(-5)
        
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_unbalanced_valid_bst(self):
        # Create tree: [5,3,6,2,4,null,7]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(7)
        
        self.assertTrue(self.solution.isValidBST(root))
    
    def test_unbalanced_invalid_bst(self):
        # Create tree: [5,3,6,2,4,7,1]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(1)
        
        self.assertFalse(self.solution.isValidBST(root))

if __name__ == '__main__':
    unittest.main() 