"""
Problem Statement:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input Format:
- preorder: List[int] - Preorder traversal of the binary tree
- inorder: List[int] - Inorder traversal of the binary tree

Output Format:
- TreeNode - Root of the constructed binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Explanation: The constructed binary tree is:
    3
   / \
  9  20
     / \
   15   7

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values
- Each value of inorder also appears in preorder
- preorder is guaranteed to be the preorder traversal of the tree
- inorder is guaranteed to be the inorder traversal of the tree

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n)
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct and return the binary tree from preorder and inorder traversals.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        
        root = self.solution.buildTree(preorder, inorder)
        
        # Verify the tree structure
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)
    
    def test_example2(self):
        preorder = [-1]
        inorder = [-1]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, -1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
    
    def test_single_node(self):
        preorder = [1]
        inorder = [1]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
    
    def test_left_skewed_tree(self):
        preorder = [1,2,3]
        inorder = [3,2,1]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertIsNone(root.right)
    
    def test_right_skewed_tree(self):
        preorder = [1,2,3]
        inorder = [1,2,3]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertIsNone(root.left)
    
    def test_complete_tree(self):
        preorder = [1,2,4,5,3,6,7]
        inorder = [4,2,5,1,6,3,7]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)
    
    def test_duplicate_values(self):
        preorder = [1,1,1]
        inorder = [1,1,1]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 1)
        self.assertEqual(root.right.right.val, 1)
        self.assertIsNone(root.left)
    
    def test_negative_values(self):
        preorder = [-1,-2,-3]
        inorder = [-2,-1,-3]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, -1)
        self.assertEqual(root.left.val, -2)
        self.assertEqual(root.right.val, -3)
    
    def test_large_values(self):
        preorder = [1000,500,1500]
        inorder = [500,1000,1500]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1000)
        self.assertEqual(root.left.val, 500)
        self.assertEqual(root.right.val, 1500)
    
    def test_unbalanced_tree(self):
        preorder = [1,2,3,4,5]
        inorder = [5,4,3,2,1]
        
        root = self.solution.buildTree(preorder, inorder)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertEqual(root.left.left.left.val, 4)
        self.assertEqual(root.left.left.left.left.val, 5)
        self.assertIsNone(root.right)

if __name__ == '__main__':
    unittest.main() 