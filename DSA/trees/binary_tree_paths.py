"""
Problem Statement:
Given the root of a binary tree, return all root-to-leaf paths in any order.

Input Format:
- root: TreeNode - Root of the binary tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- List[str] - List of all root-to-leaf paths in the format "root->child->...->leaf"

Example:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Explanation: The tree is:
    1
   / \
  2   3
   \
    5
There are two paths: 1->2->5 and 1->3

Input: root = [1]
Output: ["1"]

Constraints:
- The number of nodes in the tree is in the range [1, 100]
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Return all root-to-leaf paths in the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: [1,2,3,null,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        
        expected = ["1->2->5", "1->3"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.binaryTreePaths(root), ["1"])
    
    def test_empty_tree(self):
        root = None
        self.assertEqual(self.solution.binaryTreePaths(root), [])
    
    def test_left_skewed_tree(self):
        # Create tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertEqual(self.solution.binaryTreePaths(root), ["1->2->3"])
    
    def test_right_skewed_tree(self):
        # Create tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        self.assertEqual(self.solution.binaryTreePaths(root), ["1->2->3"])
    
    def test_complete_tree(self):
        # Create tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        expected = ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_unbalanced_tree(self):
        # Create tree: [1,2,3,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        
        expected = ["1->2->4", "1->3"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_negative_values(self):
        # Create tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        expected = ["-1->-2", "-1->-3"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_large_values(self):
        # Create tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        expected = ["1000->2000", "1000->3000"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
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
        
        expected = [
            "1->2->4->8", "1->2->4->9", "1->2->5->10", "1->2->5->11",
            "1->3->6->12", "1->3->6->13", "1->3->7->14", "1->3->7->15"
        ]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_tree_with_duplicates(self):
        # Create tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        expected = ["1->1->1", "1->1->1", "1->1"]
        result = self.solution.binaryTreePaths(root)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main() 