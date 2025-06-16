"""
Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[List[int]] - List of lists containing node values at each level

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation:
Level 1: [3]
Level 2: [9,20]
Level 3: [15,7]

Input: root = [1]
Output: [[1]]

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the level order traversal of the binary tree.
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
        
        expected = [[3],[9,20],[15,7]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_example2(self):
        # Create tree: [1]
        root = TreeNode(1)
        
        expected = [[1]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_empty_tree(self):
        root = None
        expected = []
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_single_level(self):
        # Create tree: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        expected = [[1],[2,3]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        expected = [[1],[2],[3]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        expected = [[1],[2,3],[4,5,6,7]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_zigzag_tree(self):
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
        
        expected = [[1],[2,3],[4,5,6,7],[8,9]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        expected = [[-1],[-2,-3]]
        self.assertEqual(self.solution.levelOrder(root), expected)
    
    def test_large_tree(self):
        # Create a tree with 15 nodes
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
        
        expected = [[1],[2,3],[4,5,6,7],[8,9,10,11,12,13,14,15]]
        self.assertEqual(self.solution.levelOrder(root), expected)

if __name__ == '__main__':
    unittest.main() 