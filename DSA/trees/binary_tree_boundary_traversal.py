"""
Problem Statement:
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

The left boundary is defined as the path from root to the left-most node. The right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[int] - Boundary traversal of node values

Example:
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation: The tree is:
   1
    \
     2
    / \
   3   4
The boundary is [1,3,4,2].

Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation: The tree is:
       1
      / \
     2   3
    / \   \
   4   5   6
      / \ / \
     7  8 9 10
The boundary is [1,2,4,7,8,9,10,6,3].

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the boundary traversal of the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,null,2,3,4]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 3, 4, 2])
    
    def test_example2(self):
        # Create tree: [1,2,3,4,5,6,null,null,null,7,8,9,10]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right.right.left = TreeNode(9)
        root.right.right.right = TreeNode(10)
        
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 4, 7, 8, 9, 10, 6, 3])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1])
    
    def test_two_nodes_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2])
    
    def test_two_nodes_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2])
    
    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 3])
    
    def test_four_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 4, 3])
    
    def test_five_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 4, 5, 3])
    
    def test_seven_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 4, 5, 6, 7, 3])
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [-1, -2, -3])
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1000, 2000, 3000])
    
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
        
        expected = [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 7, 3]
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), expected)
    
    def test_tree_with_duplicates(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 1, 1, 1, 1])
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.boundaryOfBinaryTree(root), [1, 2, 4, 3])

if __name__ == '__main__':
    unittest.main() 