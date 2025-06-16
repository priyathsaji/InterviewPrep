"""
Problem Statement:
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- TreeNode - Root of the pruned binary tree

Example:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: The tree is:
   1
    \
     0
    / \
   0   1
    becomes
   1
    \
     0
      \
       1
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Explanation: The tree is:
     1
    / \
   0   1
  / \ / \
 0  0 0  1
    becomes
     1
      \
       1
        \
         1

Constraints:
- The number of nodes in the tree is in the range [1, 200]
- Node.val is either 0 or 1

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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Prune the binary tree by removing subtrees that don't contain 1.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,null,0,0,1]
        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 0)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 1)
    
    def test_example2(self):
        # Create tree: [1,0,1,0,0,0,1]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 1)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 1)
    
    def test_single_node_one(self):
        root = TreeNode(1)
        result = self.solution.pruneTree(root)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
    
    def test_single_node_zero(self):
        root = TreeNode(0)
        result = self.solution.pruneTree(root)
        self.assertIsNone(result)
    
    def test_left_skewed_tree(self):
        # Create tree: [1,0,0,0]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.left.left = TreeNode(0)
        root.left.left.left = TreeNode(0)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,0,null,0,null,1]
        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.right = TreeNode(0)
        root.right.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 0)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 0)
        self.assertIsNone(result.right.right.left)
        self.assertEqual(result.right.right.right.val, 1)
    
    def test_complete_tree(self):
        # Create tree: [1,0,1,0,0,0,1]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 1)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 1)
    
    def test_all_zeros(self):
        # Create tree: [0,0,0,0,0]
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        
        result = self.solution.pruneTree(root)
        self.assertIsNone(result)
    
    def test_all_ones(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 1)
        self.assertEqual(result.right.val, 1)
        self.assertEqual(result.left.left.val, 1)
        self.assertEqual(result.left.right.val, 1)
    
    def test_mixed_values(self):
        # Create tree: [1,1,0,1,0,0,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(0)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 1)
        self.assertEqual(result.right.val, 0)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNone(result.left.right)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 1)
    
    def test_deep_tree(self):
        # Create a deep tree with mixed values
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        root.left.left.left = TreeNode(0)
        root.left.left.right = TreeNode(1)
        root.left.right.left = TreeNode(0)
        root.left.right.right = TreeNode(0)
        root.right.left.left = TreeNode(0)
        root.right.left.right = TreeNode(0)
        root.right.right.left = TreeNode(0)
        root.right.right.right = TreeNode(1)
        
        result = self.solution.pruneTree(root)
        
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertEqual(result.right.val, 1)
        self.assertIsNone(result.right.left)
        self.assertEqual(result.right.right.val, 1)
        self.assertIsNone(result.right.right.left)
        self.assertEqual(result.right.right.right.val, 1)

if __name__ == '__main__':
    unittest.main() 