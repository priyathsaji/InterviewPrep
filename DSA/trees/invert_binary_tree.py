"""
Problem Statement:
Given the root of a binary tree, invert the tree, and return its root.

Inverting a binary tree means that the left and right subtrees of every node are swapped.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- TreeNode - Root of the inverted binary tree

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Explanation: The tree is:
     4
    / \
   2   7
  / \ / \
 1  3 6  9
    becomes
     4
    / \
   7   2
  / \ / \
 9  6 3  1

Input: root = [2,1,3]
Output: [2,3,1]
Explanation: The tree is:
   2
  / \
 1   3
    becomes
   2
  / \
 3   1

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert the binary tree by swapping left and right subtrees.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [4,2,7,1,3,6,9]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 4)
        self.assertEqual(result.left.val, 7)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 9)
        self.assertEqual(result.left.right.val, 6)
        self.assertEqual(result.right.left.val, 3)
        self.assertEqual(result.right.right.val, 1)
    
    def test_example2(self):
        # Create tree: [2,1,3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 2)
        self.assertEqual(result.left.val, 3)
        self.assertEqual(result.right.val, 1)
    
    def test_empty_tree(self):
        root = None
        result = self.solution.invertTree(root)
        self.assertIsNone(result)
    
    def test_single_node(self):
        root = TreeNode(1)
        result = self.solution.invertTree(root)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 2)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 3)
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 2)
        self.assertEqual(result.left.left.val, 3)
        self.assertIsNone(result.right)
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 3)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 7)
        self.assertEqual(result.left.right.val, 6)
        self.assertEqual(result.right.left.val, 5)
        self.assertEqual(result.right.right.val, 4)
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, -1)
        self.assertEqual(result.left.val, -3)
        self.assertEqual(result.right.val, -2)
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1000)
        self.assertEqual(result.left.val, 3000)
        self.assertEqual(result.right.val, 2000)
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 3)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.right.right.val, 4)
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        result = self.solution.invertTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 1)
        self.assertEqual(result.right.val, 1)
        self.assertEqual(result.left.left.val, 1)
        self.assertEqual(result.left.right.val, 1)

if __name__ == '__main__':
    unittest.main() 