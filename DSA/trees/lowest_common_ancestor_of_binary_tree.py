"""
Problem Statement:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
- p: TreeNode - First node
- q: TreeNode - Second node

Output Format:
- TreeNode - The lowest common ancestor of p and q

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.

Constraints:
- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the tree

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
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Find the lowest common ancestor of nodes p and q in the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [3,5,1,6,2,0,8,null,null,7,4]
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        
        p = root.left  # 5
        q = root.right  # 1
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 3)
    
    def test_example2(self):
        # Create tree: [3,5,1,6,2,0,8,null,null,7,4]
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        
        p = root.left  # 5
        q = root.left.right.right  # 4
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 5)
    
    def test_single_node(self):
        root = TreeNode(1)
        p = root
        q = root
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1)
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        p = root.left  # 2
        q = root.left.left  # 3
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 2)
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        p = root.right  # 2
        q = root.right.right  # 3
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 2)
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        p = root.left.left  # 4
        q = root.right.right  # 7
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1)
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        p = root.left.left  # 4
        q = root.right  # 3
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1)
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        p = root.left  # -2
        q = root.right  # -3
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, -1)
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        p = root.left  # 2000
        q = root.right  # 3000
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1000)
    
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
        
        p = root.left.left.left  # 8
        q = root.right.right.right  # 15
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1)
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        p = root.left.left  # 1
        q = root.right  # 1
        
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 1)

if __name__ == '__main__':
    unittest.main() 