"""
Problem Statement:
Given the root of a complete binary tree, return the number of the nodes in the tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.

Input Format:
- root: TreeNode - Root of the complete binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- int - Number of nodes in the complete binary tree

Example:
Input: root = [1,2,3,4,5,6]
Output: 6
Explanation: The tree is:
     1
    / \
   2   3
  / \ /
 4  5 6
There are 6 nodes in the tree.

Input: root = []
Output: 0
Explanation: The tree is empty.

Input: root = [1]
Output: 1
Explanation: The tree has only one node.

Constraints:
- The number of nodes in the tree is in the range [0, 5 * 10^4]
- 0 <= Node.val <= 5 * 10^4
- The tree is guaranteed to be complete

Time Complexity: O(log^2 n) where n is the number of nodes
Space Complexity: O(1)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Count the number of nodes in a complete binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,2,3,4,5,6]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        
        self.assertEqual(self.solution.countNodes(root), 6)
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.countNodes(root), 0)
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.countNodes(root), 1)
    
    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.countNodes(root), 2)
    
    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.countNodes(root), 3)
    
    def test_four_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.countNodes(root), 4)
    
    def test_five_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.countNodes(root), 5)
    
    def test_seven_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.countNodes(root), 7)
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.countNodes(root), 3)
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        self.assertEqual(self.solution.countNodes(root), 3)
    
    def test_deep_tree(self):
        # Create a deep complete tree
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
        
        self.assertEqual(self.solution.countNodes(root), 15)
    
    def test_tree_with_duplicates(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.countNodes(root), 5)

if __name__ == '__main__':
    unittest.main() 