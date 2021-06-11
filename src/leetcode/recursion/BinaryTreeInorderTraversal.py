# LeetCode 94. Binary Tree Inorder Traversal [Easy]

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [1]
# Output: [1]

# Example 4:

# Input: root = [1,2]
# Output: [2,1]

# Example 5:

# Input: root = [1,null,2]
# Output: [1,2]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        self.recurse(root, result)
        return result

    def recurse(self, root, result):
        if root != None:
            self.recurse(root.left, result)
            result.append(root.val)
            self.recurse(root.right, result)
        return result
