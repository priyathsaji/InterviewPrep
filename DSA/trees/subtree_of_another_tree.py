"""
Problem Statement:
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Input Format:
- root: TreeNode - Root of the main binary tree
- subRoot: TreeNode - Root of the subtree to check
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

Output Format:
- bool - True if t is a subtree of s, False otherwise

Example:
Input: s = [3,4,5,1,2], t = [4,1,2]
Output: true
Explanation: The tree t is a subtree of s:
     3
    / \
   4   5
  / \
 1   2
    is a subtree of
     3
    / \
   4   5
  / \
 1   2

Input: s = [3,4,5,1,2,null,null,0], t = [4,1,2]
Output: false
Explanation: The tree t is not a subtree of s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
    is not a subtree of
     3
    / \
   4   5
  / \
 1   2

Constraints:
- The number of nodes in the s tree is in the range [1, 2000]
- The number of nodes in the t tree is in the range [1, 1000]
- -10^4 <= Node.val <= 10^4

Time Complexity: O(m * n) where m and n are the number of nodes in s and t respectively
Space Complexity: O(h) where h is the height of the tree s
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if subRoot is a subtree of root.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create main tree: [3,4,5,1,2]
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        
        # Create subtree: [4,1,2]
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_example2(self):
        # Create main tree: [3,4,5,1,2,null,null,0]
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.left.left = TreeNode(0)
        
        # Create subtree: [4,1,2]
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        
        self.assertFalse(self.solution.isSubtree(root, subRoot))
    
    def test_empty_subtree(self):
        root = TreeNode(1)
        subRoot = None
        self.assertFalse(self.solution.isSubtree(root, subRoot))
    
    def test_single_node_match(self):
        root = TreeNode(1)
        subRoot = TreeNode(1)
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_single_node_mismatch(self):
        root = TreeNode(1)
        subRoot = TreeNode(2)
        self.assertFalse(self.solution.isSubtree(root, subRoot))
    
    def test_left_skewed_tree(self):
        # Create main tree: [1,2,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        # Create subtree: [2,3]
        subRoot = TreeNode(2)
        subRoot.left = TreeNode(3)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_right_skewed_tree(self):
        # Create main tree: [1,null,2,null,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        # Create subtree: [2,3]
        subRoot = TreeNode(2)
        subRoot.right = TreeNode(3)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_complete_tree(self):
        # Create main tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        # Create subtree: [2,4,5]
        subRoot = TreeNode(2)
        subRoot.left = TreeNode(4)
        subRoot.right = TreeNode(5)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_negative_values(self):
        # Create main tree: [-1,-2,-3]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        # Create subtree: [-2]
        subRoot = TreeNode(-2)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_large_values(self):
        # Create main tree: [1000,2000,3000]
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        # Create subtree: [2000]
        subRoot = TreeNode(2000)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_deep_tree(self):
        # Create a deep main tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        
        # Create subtree: [4,8,9]
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(8)
        subRoot.right = TreeNode(9)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_tree_with_duplicates(self):
        # Create main tree: [1,1,1,1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        
        # Create subtree: [1,1,1]
        subRoot = TreeNode(1)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(1)
        
        self.assertTrue(self.solution.isSubtree(root, subRoot))
    
    def test_partial_match(self):
        # Create main tree: [1,2,3,4,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        # Create subtree: [2,4,6]
        subRoot = TreeNode(2)
        subRoot.left = TreeNode(4)
        subRoot.right = TreeNode(6)
        
        self.assertFalse(self.solution.isSubtree(root, subRoot))

if __name__ == '__main__':
    unittest.main() 