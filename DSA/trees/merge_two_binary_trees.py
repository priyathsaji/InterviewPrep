"""
Problem Statement:
You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Input Format:
- root1: TreeNode - Root of the first binary tree
- root2: TreeNode - Root of the second binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- TreeNode - Root of the merged binary tree

Example:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Explanation: The merged tree is:
     3
    / \
   4   5
  / \   \
 5   4   7

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
Explanation: The merged tree is:
   2
  /
 2

Constraints:
- The number of nodes in both trees is in the range [0, 2000]
- -10^4 <= Node.val <= 10^4

Time Complexity: O(min(n1, n2)) where n1 and n2 are the number of nodes in root1 and root2 respectively
Space Complexity: O(min(h1, h2)) where h1 and h2 are the heights of root1 and root2 respectively
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Merge two binary trees according to the given rules.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create first tree: [1,3,2,5]
        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(5)
        
        # Create second tree: [2,1,3,null,4,null,7]
        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)
        root2.left.right = TreeNode(4)
        root2.right.right = TreeNode(7)
        
        # Expected merged tree: [3,4,5,5,4,null,7]
        result = self.solution.mergeTrees(root1, root2)
        
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 4)
        self.assertEqual(result.right.val, 5)
        self.assertEqual(result.left.left.val, 5)
        self.assertEqual(result.left.right.val, 4)
        self.assertEqual(result.right.right.val, 7)
    
    def test_example2(self):
        # Create first tree: [1]
        root1 = TreeNode(1)
        
        # Create second tree: [1,2]
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        
        # Expected merged tree: [2,2]
        result = self.solution.mergeTrees(root1, root2)
        
        self.assertEqual(result.val, 2)
        self.assertEqual(result.left.val, 2)
    
    def test_empty_trees(self):
        root1 = None
        root2 = None
        result = self.solution.mergeTrees(root1, root2)
        self.assertIsNone(result)
    
    def test_one_empty_tree(self):
        # Create first tree: [1,2,3]
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        
        root2 = None
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.left.val, 2)
        self.assertEqual(result.right.val, 3)
    
    def test_left_skewed_trees(self):
        # Create first tree: [1,2,null,3]
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.left.left = TreeNode(3)
        
        # Create second tree: [4,5,null,6]
        root2 = TreeNode(4)
        root2.left = TreeNode(5)
        root2.left.left = TreeNode(6)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.left.val, 7)
        self.assertEqual(result.left.left.val, 9)
    
    def test_right_skewed_trees(self):
        # Create first tree: [1,null,2,null,3]
        root1 = TreeNode(1)
        root1.right = TreeNode(2)
        root1.right.right = TreeNode(3)
        
        # Create second tree: [4,null,5,null,6]
        root2 = TreeNode(4)
        root2.right = TreeNode(5)
        root2.right.right = TreeNode(6)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.right.val, 7)
        self.assertEqual(result.right.right.val, 9)
    
    def test_complete_trees(self):
        # Create first tree: [1,2,3,4,5,6,7]
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        root1.right.left = TreeNode(6)
        root1.right.right = TreeNode(7)
        
        # Create second tree: [1,2,3,4,5,6,7]
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        root2.right.left = TreeNode(6)
        root2.right.right = TreeNode(7)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.left.val, 4)
        self.assertEqual(result.right.val, 6)
        self.assertEqual(result.left.left.val, 8)
        self.assertEqual(result.left.right.val, 10)
        self.assertEqual(result.right.left.val, 12)
        self.assertEqual(result.right.right.val, 14)
    
    def test_negative_values(self):
        # Create first tree: [-1,-2,-3]
        root1 = TreeNode(-1)
        root1.left = TreeNode(-2)
        root1.right = TreeNode(-3)
        
        # Create second tree: [-4,-5,-6]
        root2 = TreeNode(-4)
        root2.left = TreeNode(-5)
        root2.right = TreeNode(-6)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, -5)
        self.assertEqual(result.left.val, -7)
        self.assertEqual(result.right.val, -9)
    
    def test_large_values(self):
        # Create first tree: [1000,2000,3000]
        root1 = TreeNode(1000)
        root1.left = TreeNode(2000)
        root1.right = TreeNode(3000)
        
        # Create second tree: [4000,5000,6000]
        root2 = TreeNode(4000)
        root2.left = TreeNode(5000)
        root2.right = TreeNode(6000)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 5000)
        self.assertEqual(result.left.val, 7000)
        self.assertEqual(result.right.val, 9000)
    
    def test_unbalanced_trees(self):
        # Create first tree: [1,2,3,4]
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)
        
        # Create second tree: [5,6,7,8]
        root2 = TreeNode(5)
        root2.left = TreeNode(6)
        root2.right = TreeNode(7)
        root2.left.left = TreeNode(8)
        
        result = self.solution.mergeTrees(root1, root2)
        self.assertEqual(result.val, 6)
        self.assertEqual(result.left.val, 8)
        self.assertEqual(result.right.val, 10)
        self.assertEqual(result.left.left.val, 12)

if __name__ == '__main__':
    unittest.main() 