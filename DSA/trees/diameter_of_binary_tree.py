"""
Problem Statement:
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- int - Length of the diameter of the tree

Example:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: The tree is:
    1
   / \
  2   3
 / \
4   5
The diameter is 3 (path: 4->2->1->3 or 5->2->1->3)

Input: root = [1,2]
Output: 1
Explanation: The tree is:
    1
   /
  2
The diameter is 1 (path: 1->2)

Constraints:
- The number of nodes in the tree is in the range [1, 10^4]
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Return the length of the diameter of the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,2,3,4,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)
    
    def test_example2(self):
        # Create tree: [1,2]
        root = TreeNode(1)
        root.left = TreeNode(2)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)
    
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
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 6)
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)
    
    def test_diameter_not_through_root(self):
        # Create tree: [1,2,3,4,5,6,7,8,9]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 5)

if __name__ == '__main__':
    unittest.main() 