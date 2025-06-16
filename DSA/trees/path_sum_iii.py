"""
Problem Statement:
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
- targetSum: int - Target sum to find in paths

Output Format:
- int - Number of paths that sum to targetSum

Example:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are:
1. 5 -> 3
2. 5 -> 2 -> 1
3. -3 -> 11

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
Explanation: The paths that sum to 22 are:
1. 5 -> 4 -> 11 -> 2
2. 5 -> 8 -> 4 -> 5
3. 4 -> 11 -> 7

Constraints:
- The number of nodes in the tree is in the range [0, 1000]
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Return the number of paths that sum to targetSum.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [10,5,-3,3,2,null,11,3,-2,null,1]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        
        self.assertEqual(self.solution.pathSum(root, 8), 3)
    
    def test_example2(self):
        # Create tree: [5,4,8,11,null,13,4,7,2,null,null,5,1]
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        
        self.assertEqual(self.solution.pathSum(root, 22), 3)
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.pathSum(root, 0), 0)
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.pathSum(root, 1), 1)
        self.assertEqual(self.solution.pathSum(root, 2), 0)
    
    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.pathSum(root, 3), 1)
        self.assertEqual(self.solution.pathSum(root, 1), 1)
        self.assertEqual(self.solution.pathSum(root, 2), 1)
    
    def test_negative_values(self):
        root = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.pathSum(root, -5), 1)
        self.assertEqual(self.solution.pathSum(root, -2), 1)
        self.assertEqual(self.solution.pathSum(root, -3), 1)
    
    def test_zero_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(-1)
        root.right = TreeNode(1)
        self.assertEqual(self.solution.pathSum(root, 0), 2)
    
    def test_multiple_paths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.pathSum(root, 7), 2)
        self.assertEqual(self.solution.pathSum(root, 10), 1)
        self.assertEqual(self.solution.pathSum(root, 11), 2)
    
    def test_large_values(self):
        root = TreeNode(1000000000)
        root.left = TreeNode(1000000000)
        root.right = TreeNode(1000000000)
        
        self.assertEqual(self.solution.pathSum(root, 2000000000), 2)
        self.assertEqual(self.solution.pathSum(root, 1000000000), 3)
    
    def test_deep_tree(self):
        root = TreeNode(1)
        current = root
        for i in range(10):
            current.left = TreeNode(1)
            current = current.left
        
        self.assertEqual(self.solution.pathSum(root, 10), 1)
        self.assertEqual(self.solution.pathSum(root, 5), 1)
    
    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(3)
        
        self.assertEqual(self.solution.pathSum(root, 6), 4)
        self.assertEqual(self.solution.pathSum(root, 3), 4)
        self.assertEqual(self.solution.pathSum(root, 5), 2)

if __name__ == '__main__':
    unittest.main() 