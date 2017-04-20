#   Question: 111. Minimum Depth of Binary Tree
# Difficulty: Easy
#       Tags: Tree
'''
Given a binary tree, find its maximum depth.

The minimum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def minDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.minval = sys.maxint
        # left = 2**32
        # right = 2**32
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if root.left:
        #     left = self.minDepth(root.left)
        # if root.right:
        #     right = self.minDepth(root.right)
        # return 1+min(left, right)
        self.topdown(root, 1)
        return self.minval

    def topdown(self, root, depth):
        if not root:
            return
        if not root.left and not root.right:
            self.minval = min(self.minval, depth)
            return
        if root.left:
            self.topdown(root.left, depth + 1)
        if root.right:
            self.topdown(root.right, depth + 1)