"""
Problem Statement:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
- targetSum: int - Target sum to find in the path

Output Format:
- bool - True if there exists a root-to-leaf path with sum equal to targetSum, False otherwise

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The path with target sum is shown:
    5
   / \
  4   8
 /   / \
11  13  4
/  \      \
7    2      1
Path: 5->4->11->2 = 22

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There is no root-to-leaf path with sum 5.

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -1000 <= Node.val <= 1000
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Check if there exists a root-to-leaf path with sum equal to targetSum.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.right = TreeNode(1)
        
        self.assertTrue(self.solution.hasPathSum(root, 22))
    
    def test_example2(self):
        # Create tree: [1,2,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        self.assertFalse(self.solution.hasPathSum(root, 5))
    
    def test_empty_tree(self):
        root = None
        self.assertFalse(self.solution.hasPathSum(root, 0))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 1))
        self.assertFalse(self.solution.hasPathSum(root, 2))
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertTrue(self.solution.hasPathSum(root, 6))
        self.assertFalse(self.solution.hasPathSum(root, 5))
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertTrue(self.solution.hasPathSum(root, 6))
        self.assertFalse(self.solution.hasPathSum(root, 5))
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        self.assertTrue(self.solution.hasPathSum(root, 7))  # 1->2->4
        self.assertTrue(self.solution.hasPathSum(root, 8))  # 1->2->5
        self.assertTrue(self.solution.hasPathSum(root, 10))  # 1->3->6
        self.assertTrue(self.solution.hasPathSum(root, 11))  # 1->3->7
        self.assertFalse(self.solution.hasPathSum(root, 12))
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        self.assertTrue(self.solution.hasPathSum(root, 7))  # 1->2->4
        self.assertTrue(self.solution.hasPathSum(root, 4))  # 1->3
        self.assertFalse(self.solution.hasPathSum(root, 5))
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        self.assertTrue(self.solution.hasPathSum(root, -3))  # -1->-2
        self.assertTrue(self.solution.hasPathSum(root, -4))  # -1->-3
        self.assertFalse(self.solution.hasPathSum(root, -5))
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        self.assertTrue(self.solution.hasPathSum(root, 3000))  # 1000->2000
        self.assertTrue(self.solution.hasPathSum(root, 4000))  # 1000->3000
        self.assertFalse(self.solution.hasPathSum(root, 5000))
    
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
        
        self.assertTrue(self.solution.hasPathSum(root, 15))  # 1->2->4->8
        self.assertTrue(self.solution.hasPathSum(root, 16))  # 1->2->4->9
        self.assertTrue(self.solution.hasPathSum(root, 18))  # 1->2->5->10
        self.assertTrue(self.solution.hasPathSum(root, 19))  # 1->2->5->11
        self.assertTrue(self.solution.hasPathSum(root, 22))  # 1->3->6->12
        self.assertTrue(self.solution.hasPathSum(root, 23))  # 1->3->6->13
        self.assertTrue(self.solution.hasPathSum(root, 25))  # 1->3->7->14
        self.assertTrue(self.solution.hasPathSum(root, 26))  # 1->3->7->15
        self.assertFalse(self.solution.hasPathSum(root, 27))
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        self.assertTrue(self.solution.hasPathSum(root, 3))  # 1->1->1
        self.assertFalse(self.solution.hasPathSum(root, 4))

if __name__ == '__main__':
    unittest.main() 