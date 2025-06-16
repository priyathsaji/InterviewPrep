"""
Problem Statement:
Given a binary tree, return the diagonal order traversal of its nodes' values. (i.e., from top-left to bottom-right).

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[List[int]] - Diagonal order traversal of node values

Example:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: [[8,10,14],[3,6,7,13],[1,4]]
Explanation:
Diagonal 0: [8,10,14]
Diagonal 1: [3,6,7,13]
Diagonal 2: [1,4]

Input: root = [1,2,3,4,5,6,7]
Output: [[1,3,7],[2,5,6],[4]]
Explanation:
Diagonal 0: [1,3,7]
Diagonal 1: [2,5,6]
Diagonal 2: [4]

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) where n is the number of nodes
"""

from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diagonalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the diagonal order traversal of the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [8,3,10,1,6,null,14,null,null,4,7,13]
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right.right.left = TreeNode(13)
        
        self.assertEqual(self.solution.diagonalOrder(root), [[8,10,14], [3,6,7,13], [1,4]])
    
    def test_example2(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3,7], [2,5,6], [4]])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.diagonalOrder(root), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.diagonalOrder(root), [[1]])
    
    def test_two_nodes_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.diagonalOrder(root), [[1], [2]])
    
    def test_two_nodes_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,2]])
    
    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3], [2]])
    
    def test_four_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3], [2], [4]])
    
    def test_five_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3], [2,5], [4]])
    
    def test_seven_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3,7], [2,5,6], [4]])
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.diagonalOrder(root), [[-1,-3], [-2]])
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        self.assertEqual(self.solution.diagonalOrder(root), [[1000,3000], [2000]])
    
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
        
        expected = [[1,3,7,15], [2,5,6,11,13,14], [4,9,10,12], [8]]
        self.assertEqual(self.solution.diagonalOrder(root), expected)
    
    def test_tree_with_duplicates(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,1], [1,1], [1]])
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.diagonalOrder(root), [[1,3], [2], [4]])

if __name__ == '__main__':
    unittest.main() 