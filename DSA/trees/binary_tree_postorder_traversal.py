"""
Problem Statement:
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[int] - List of node values in postorder traversal (left -> right -> root)

Example:
Input: root = [1,null,2,3]
Output: [3,2,1]
Explanation: The postorder traversal is: left subtree -> right subtree -> root
    1
     \
      2
     /
    3

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the postorder traversal of the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.postorderTraversal(root), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.postorderTraversal(root), [1])
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.postorderTraversal(root), [4, 5, 2, 6, 7, 3, 1])
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        self.assertEqual(self.solution.postorderTraversal(root), [4, 2, 3, 1])
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        self.assertEqual(self.solution.postorderTraversal(root), [-2, -3, -1])
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        self.assertEqual(self.solution.postorderTraversal(root), [2000, 3000, 1000])
    
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
        
        expected = [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
        self.assertEqual(self.solution.postorderTraversal(root), expected)
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        self.assertEqual(self.solution.postorderTraversal(root), [1, 1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main() 