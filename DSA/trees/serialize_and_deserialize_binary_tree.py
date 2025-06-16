"""
Problem Statement:
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Input Format:
- For serialization: root: TreeNode - Root of the binary tree
- For deserialization: data: str - Serialized string representation of the tree

Output Format:
- For serialization: str - Serialized string representation of the tree
- For deserialization: TreeNode - Root of the deserialized binary tree

Example:
Input: root = [1,2,3,null,null,4,5]
Output: "1,2,3,null,null,4,5"
Explanation: The serialized string represents the following tree:
    1
   / \
  2   3
     / \
    4   5

Input: data = "1,2,3,null,null,4,5"
Output: [1,2,3,null,null,4,5]
Explanation: The deserialized tree is the same as the original tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000

Time Complexity: O(n) for both serialization and deserialization
Space Complexity: O(n) for both serialization and deserialization
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        """
        raise NotImplementedError("Solution not implemented")
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        """
        raise NotImplementedError("Solution not implemented")

import unittest

class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()
    
    def test_example1(self):
        # Create tree: [1,2,3,null,null,4,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,3,null,null,4,5")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertEqual(deserialized.right.left.val, 4)
        self.assertEqual(deserialized.right.right.val, 5)
    
    def test_empty_tree(self):
        root = None
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertIsNone(deserialized)
    
    def test_single_node(self):
        root = TreeNode(1)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertIsNone(deserialized.left)
        self.assertIsNone(deserialized.right)
    
    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,null,3")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.left.left.val, 3)
        self.assertIsNone(deserialized.right)
    
    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,null,2,null,3")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.right.val, 2)
        self.assertEqual(deserialized.right.right.val, 3)
        self.assertIsNone(deserialized.left)
    
    def test_complete_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,3,4,5,6,7")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertEqual(deserialized.left.left.val, 4)
        self.assertEqual(deserialized.left.right.val, 5)
        self.assertEqual(deserialized.right.left.val, 6)
        self.assertEqual(deserialized.right.right.val, 7)
    
    def test_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "-1,-2,-3")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, -1)
        self.assertEqual(deserialized.left.val, -2)
        self.assertEqual(deserialized.right.val, -3)
    
    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(2000)
        root.right = TreeNode(3000)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1000,2000,3000")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1000)
        self.assertEqual(deserialized.left.val, 2000)
        self.assertEqual(deserialized.right.val, 3000)
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        
        # Test serialization
        serialized = self.codec.serialize(root)
        self.assertEqual(serialized, "1,2,null,3,null,4,null,5")
        
        # Test deserialization
        deserialized = self.codec.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.left.left.val, 3)
        self.assertEqual(deserialized.left.left.left.val, 4)
        self.assertEqual(deserialized.left.left.left.left.val, 5)

if __name__ == '__main__':
    unittest.main() 