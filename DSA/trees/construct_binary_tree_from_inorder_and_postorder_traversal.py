"""
Problem Statement:
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Input Format:
- inorder: List[int] - Inorder traversal of the binary tree
- postorder: List[int] - Postorder traversal of the binary tree

Output Format:
- TreeNode - Root of the constructed binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Explanation: The constructed binary tree is:
    3
   / \
  9  20
    /  \
   15   7

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of unique values
- Each value of postorder also appears in inorder
- inorder is guaranteed to be the inorder traversal of the tree
- postorder is guaranteed to be the postorder traversal of the tree

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) where n is the number of nodes
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Construct and return the binary tree from inorder and postorder traversals.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        
        root = self.solution.buildTree(inorder, postorder)
        
        # Verify the tree structure
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right.left.left)
        self.assertIsNone(root.right.left.right)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)
    
    def test_single_node(self):
        inorder = [-1]
        postorder = [-1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, -1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
    
    def test_left_skewed_tree(self):
        inorder = [3, 2, 1]
        postorder = [3, 2, 1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertIsNone(root.right)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.left.left.right)
    
    def test_right_skewed_tree(self):
        inorder = [1, 2, 3]
        postorder = [3, 2, 1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)
    
    def test_complete_tree(self):
        inorder = [4, 2, 5, 1, 6, 3, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.left.left.right)
        self.assertIsNone(root.left.right.left)
        self.assertIsNone(root.left.right.right)
        self.assertIsNone(root.right.left.left)
        self.assertIsNone(root.right.left.right)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)
    
    def test_unbalanced_tree(self):
        inorder = [4, 2, 1, 3]
        postorder = [4, 2, 3, 1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.left.left.right)
    
    def test_negative_values(self):
        inorder = [-3, -2, -1]
        postorder = [-3, -2, -1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, -1)
        self.assertEqual(root.left.val, -2)
        self.assertEqual(root.left.left.val, -3)
        self.assertIsNone(root.right)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.left.left.right)
    
    def test_large_values(self):
        inorder = [1000, 2000, 3000]
        postorder = [1000, 2000, 3000]
        
        root = self.solution.buildTree(inorder, postorder)
        
        self.assertEqual(root.val, 3000)
        self.assertEqual(root.left.val, 2000)
        self.assertEqual(root.left.left.val, 1000)
        self.assertIsNone(root.right)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.left.left.right)
    
    def test_deep_tree(self):
        inorder = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
        postorder = [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
        
        root = self.solution.buildTree(inorder, postorder)
        
        # Verify the tree structure
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)
        self.assertEqual(root.left.left.left.val, 8)
        self.assertEqual(root.left.left.right.val, 9)
        self.assertEqual(root.left.right.left.val, 10)
        self.assertEqual(root.left.right.right.val, 11)
        self.assertEqual(root.right.left.left.val, 12)
        self.assertEqual(root.right.left.right.val, 13)
        self.assertEqual(root.right.right.left.val, 14)
        self.assertEqual(root.right.right.right.val, 15)
        
        # Verify all leaf nodes have no children
        for node in [root.left.left.left, root.left.left.right, root.left.right.left,
                    root.left.right.right, root.right.left.left, root.right.left.right,
                    root.right.right.left, root.right.right.right]:
            self.assertIsNone(node.left)
            self.assertIsNone(node.right)

if __name__ == '__main__':
    unittest.main() 