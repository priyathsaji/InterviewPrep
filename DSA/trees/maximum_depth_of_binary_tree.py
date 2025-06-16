"""
Problem Statement:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- int - Maximum depth of the binary tree

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation: The tree is:
    3
   / \
  9  20
     / \
    15  7
The maximum depth is 3 (path: 3->20->7)

Input: root = [1,null,2]
Output: 2
Explanation: The tree is:
    1
     \
      2
The maximum depth is 2 (path: 1->2)

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Return the maximum depth of the binary tree.
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
        
        self.assertEqual(self.solution.maxDepth(root), 3)
    
    def test_example2(self):
        # Create tree: [1,null,2]
        root = TreeNode(1)
        root.right = TreeNode(2)
        
        self.assertEqual(self.solution.maxDepth(root), 2)
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.maxDepth(root), 0)
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertEqual(self.solution.maxDepth(root), 3)
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertEqual(self.solution.maxDepth(root), 3)
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.maxDepth(root), 3)
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        self.assertEqual(self.solution.maxDepth(root), 3)
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        self.assertEqual(self.solution.maxDepth(root), 2)
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        self.assertEqual(self.solution.maxDepth(root), 2)
    
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
        
        self.assertEqual(self.solution.maxDepth(root), 4)
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        self.assertEqual(self.solution.maxDepth(root), 3)

if __name__ == '__main__':
    unittest.main() 