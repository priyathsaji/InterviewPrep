"""
Problem Statement:
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[List[int]] - Vertical order traversal of node values

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9
Column  0: Nodes 3 and 15
Column  1: Only node 20
Column  2: Only node 7

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4
Column -1: Only node 2
Column  0: Nodes 1, 5, and 6
Column  1: Only node 3
Column  2: Only node 7

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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the vertical order traversal of the binary tree.
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
        
        self.assertEqual(self.solution.verticalOrder(root), [[9], [3, 15], [20], [7]])
    
    def test_example2(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1, 5, 6], [3], [7]])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.verticalOrder(root), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.verticalOrder(root), [[1]])
    
    def test_two_nodes_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.verticalOrder(root), [[2], [1]])
    
    def test_two_nodes_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.verticalOrder(root), [[1], [2]])
    
    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.verticalOrder(root), [[2], [1], [3]])
    
    def test_four_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1], [3]])
    
    def test_five_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1, 5], [3]])
    
    def test_seven_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1, 5, 6], [3], [7]])
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.verticalOrder(root), [[-2], [-1], [-3]])
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        self.assertEqual(self.solution.verticalOrder(root), [[2000], [1000], [3000]])
    
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
        
        expected = [[8], [4], [2, 9, 10], [1, 5, 12, 13], [3, 6, 14], [7, 11], [15]]
        self.assertEqual(self.solution.verticalOrder(root), expected)
    
    def test_tree_with_duplicates(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.verticalOrder(root), [[1], [1], [1, 1], [1]])
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1], [3]])

if __name__ == '__main__':
    unittest.main() 