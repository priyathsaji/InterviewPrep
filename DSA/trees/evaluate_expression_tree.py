"""
Problem Statement:
Given a binary expression tree, evaluate the expression and return the result.

The expression tree is a binary tree where each node is either:
1. A number (leaf node)
2. An operator (internal node) with two children

Valid operators are: +, -, *, /

Input Format:
- root: TreeNode - Root of the expression tree
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val  # Can be a number or operator
          self.left = left
          self.right = right

Output Format:
- float - Result of evaluating the expression tree

Example:
Input: root = ['*', '+', '+', 3, 1, 2, 4]
Output: 24
Explanation:
    *
   / \
  +   +
 / \ / \
3  1 2  4
The expression is (3 + 1) * (2 + 4) = 4 * 6 = 24

Input: root = ['+', '*', '-', 5, 2, 3, 4]
Output: 21
Explanation:
    +
   / \
  *   -
 / \ / \
5  2 3  4
The expression is (5 * 2) + (3 - 4) = 10 + (-1) = 9

Constraints:
- The number of nodes in the tree is in the range [1, 100]
- Node values are either numbers or operators (+, -, *, /)
- All numbers are in the range [-100, 100]
- Division by zero will not occur

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional, Union

class TreeNode:
    def __init__(self, val: Union[int, str], left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> float:
        """
        Evaluate the expression tree and return the result.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        # Create tree: ['*', '+', '+', 3, 1, 2, 4]
        root = TreeNode('*')
        root.left = TreeNode('+')
        root.right = TreeNode('+')
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)
        
        self.assertEqual(self.solution.evaluateTree(root), 24)
    
    def test_example2(self):
        # Create tree: ['+', '*', '-', 5, 2, 3, 4]
        root = TreeNode('+')
        root.left = TreeNode('*')
        root.right = TreeNode('-')
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        
        self.assertEqual(self.solution.evaluateTree(root), 9)
    
    def test_single_number(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.evaluateTree(root), 5)
    
    def test_simple_addition(self):
        root = TreeNode('+')
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.evaluateTree(root), 5)
    
    def test_simple_subtraction(self):
        root = TreeNode('-')
        root.left = TreeNode(5)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.evaluateTree(root), 2)
    
    def test_simple_multiplication(self):
        root = TreeNode('*')
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.evaluateTree(root), 12)
    
    def test_simple_division(self):
        root = TreeNode('/')
        root.left = TreeNode(6)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.evaluateTree(root), 3)
    
    def test_nested_operations(self):
        # Create tree: ['*', '+', '-', 3, 1, 5, 2]
        root = TreeNode('*')
        root.left = TreeNode('+')
        root.right = TreeNode('-')
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(2)
        
        self.assertEqual(self.solution.evaluateTree(root), 12)
    
    def test_deep_tree(self):
        # Create a deep tree: ['+', '*', '/', 10, 2, 6, 2]
        root = TreeNode('+')
        root.left = TreeNode('*')
        root.right = TreeNode('/')
        root.left.left = TreeNode(10)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(2)
        
        self.assertEqual(self.solution.evaluateTree(root), 23)
    
    def test_negative_numbers(self):
        root = TreeNode('+')
        root.left = TreeNode(-5)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.evaluateTree(root), -2)
    
    def test_large_numbers(self):
        root = TreeNode('*')
        root.left = TreeNode(100)
        root.right = TreeNode(50)
        self.assertEqual(self.solution.evaluateTree(root), 5000)
    
    def test_complex_expression(self):
        # Create tree: ['+', '*', '/', 10, 2, 6, 2, 3]
        root = TreeNode('+')
        root.left = TreeNode('*')
        root.right = TreeNode('/')
        root.left.left = TreeNode(10)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(2)
        
        self.assertEqual(self.solution.evaluateTree(root), 23)
    
    def test_division_with_remainder(self):
        root = TreeNode('/')
        root.left = TreeNode(7)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.evaluateTree(root), 3.5)
    
    def test_multiple_operations(self):
        # Create tree: ['*', '+', '-', 5, 3, 10, 2]
        root = TreeNode('*')
        root.left = TreeNode('+')
        root.right = TreeNode('-')
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(2)
        
        self.assertEqual(self.solution.evaluateTree(root), 64)

if __name__ == '__main__':
    unittest.main() 