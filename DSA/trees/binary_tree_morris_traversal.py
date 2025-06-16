"""
Problem Statement:
Given a binary tree, implement Morris traversal to perform inorder traversal without using recursion or stack.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[int] - Inorder traversal of node values

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:
   1
    \
     2
    /
   3
Inorder traversal: [1,3,2]

Input: root = [1,2,3,4,5]
Output: [4,2,5,1,3]
Explanation:
     1
    / \
   2   3
  / \
 4   5
Inorder traversal: [4,2,5,1,3]

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) as we only use a constant amount of extra space
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def morrisTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the inorder traversal of the binary tree using Morris traversal.
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
        
        self.assertEqual(self.solution.morrisTraversal(root), [1, 3, 2])
    
    def test_example2(self):
        # Create tree: [1,2,3,4,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        self.assertEqual(self.solution.morrisTraversal(root), [4, 2, 5, 1, 3])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.morrisTraversal(root), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.morrisTraversal(root), [1])
    
    def test_two_nodes_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.morrisTraversal(root), [2, 1])
    
    def test_two_nodes_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.morrisTraversal(root), [1, 2])
    
    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.morrisTraversal(root), [2, 1, 3])
    
    def test_four_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.morrisTraversal(root), [4, 2, 1, 3])
    
    def test_five_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.morrisTraversal(root), [4, 2, 5, 1, 3])
    
    def test_seven_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.morrisTraversal(root), [4, 2, 5, 1, 6, 3, 7])
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.morrisTraversal(root), [-2, -1, -3])
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        self.assertEqual(self.solution.morrisTraversal(root), [2000, 1000, 3000])
    
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
        
        expected = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
        self.assertEqual(self.solution.morrisTraversal(root), expected)
    
    def test_tree_with_duplicates(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.morrisTraversal(root), [1, 1, 1, 1, 1])
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.morrisTraversal(root), [4, 2, 1, 3])

if __name__ == '__main__':
    unittest.main() 