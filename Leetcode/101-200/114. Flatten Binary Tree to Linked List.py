# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):

        if root == None:    return None

        leftLast = self.helper(root.left)
        rightLast = self.helper(root.right)

        if root.left:
            leftLast.right = root.right
            root.right = root.left
            root.left = None

        if rightLast:   return rightLast
        if leftLast:    return leftLast
        return root