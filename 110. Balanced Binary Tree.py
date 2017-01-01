#   Question: 110. Balanced Binary Tree
# Difficulty: Easy
#       Tags: Tree, DFS
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
 of every node never differ by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        else:
            leftValue = self.maxDepth(root.left)+1
            rightValue = self.maxDepth(root.right)+1
            if leftValue > rightValue: return leftValue
            else: return rightValue

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return abs(depth_left-depth_right)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)