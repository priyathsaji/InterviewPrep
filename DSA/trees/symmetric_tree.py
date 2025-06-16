"""
Problem Statement:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- bool - True if the tree is symmetric, False otherwise

Example:
Input: root = [1,2,2,3,4,4,3]
Output: True
Explanation: The tree is symmetric around its center:
    1
   / \
  2   2
 / \ / \
3  4 4  3

Input: root = [1,2,2,null,3,null,3]
Output: False
Explanation: The tree is not symmetric:
    1
   / \
  2   2
   \   \
   3    3

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if the binary tree is symmetric.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,2,2,3,4,4,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_example2(self):
        # Create tree: [1,2,2,null,3,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        
        self.assertFalse(self.solution.isSymmetric(root))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_empty_tree(self):
        root = None
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_two_nodes(self):
        # Create tree: [1,2,2]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_three_nodes(self):
        # Create tree: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        self.assertFalse(self.solution.isSymmetric(root))
    
    def test_complete_tree(self):
        # Create tree: [1,2,2,3,4,4,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,2,3,null,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-2]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-2)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_different_values(self):
        # Create tree: [1,2,2,3,4,5,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(3)
        
        self.assertFalse(self.solution.isSymmetric(root))
    
    def test_deep_tree(self):
        # Create a deep symmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(5)
        root.left.left.right = TreeNode(6)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right.left.left = TreeNode(8)
        root.right.left.right = TreeNode(7)
        root.right.right.left = TreeNode(6)
        root.right.right.right = TreeNode(5)
        
        self.assertTrue(self.solution.isSymmetric(root))
    
    def test_asymmetric_deep_tree(self):
        # Create a deep asymmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(5)
        root.left.left.right = TreeNode(6)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right.left.left = TreeNode(8)
        root.right.left.right = TreeNode(7)
        root.right.right.left = TreeNode(6)
        root.right.right.right = TreeNode(9)  # Different value
        
        self.assertFalse(self.solution.isSymmetric(root))

if __name__ == '__main__':
    unittest.main() 