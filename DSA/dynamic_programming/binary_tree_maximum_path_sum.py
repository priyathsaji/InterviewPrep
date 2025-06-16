"""
Problem Statement:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input Format:
- root: TreeNode - Root of the binary tree

Output Format:
- int - Maximum path sum

Example:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Find the maximum path sum in the binary tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_tree(self, values):
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def test_example1(self):
        root = self.create_tree([1,2,3])
        self.assertEqual(self.solution.maxPathSum(root), 6)
    
    def test_example2(self):
        root = self.create_tree([-10,9,20,None,None,15,7])
        self.assertEqual(self.solution.maxPathSum(root), 42)
    
    def test_single_node(self):
        root = self.create_tree([1])
        self.assertEqual(self.solution.maxPathSum(root), 1)
    
    def test_negative_values(self):
        root = self.create_tree([-3])
        self.assertEqual(self.solution.maxPathSum(root), -3)
    
    def test_left_heavy_tree(self):
        root = self.create_tree([1,2,None,3])
        self.assertEqual(self.solution.maxPathSum(root), 6)
    
    def test_right_heavy_tree(self):
        root = self.create_tree([1,None,2,None,None,None,3])
        self.assertEqual(self.solution.maxPathSum(root), 6)
    
    def test_balanced_tree(self):
        root = self.create_tree([1,2,3,4,5,6,7])
        self.assertEqual(self.solution.maxPathSum(root), 18)
    
    def test_all_negative(self):
        root = self.create_tree([-1,-2,-3])
        self.assertEqual(self.solution.maxPathSum(root), -1)
    
    def test_mixed_values(self):
        root = self.create_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
        self.assertEqual(self.solution.maxPathSum(root), 48)
    
    def test_large_tree(self):
        values = [i for i in range(1, 16)]  # Complete binary tree with 15 nodes
        root = self.create_tree(values)
        self.assertEqual(self.solution.maxPathSum(root), 45)  # Path: 7-3-8-4-9-5-10

if __name__ == '__main__':
    unittest.main() 