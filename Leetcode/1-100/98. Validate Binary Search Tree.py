# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last = None
        self.isBST = True
        self.inorder(root)
        return self.isBST

    def inorder(self, root):

        if root == None:    return None

        self.inorder(root.left)

        if self.last != None and root.val <= self.last:
            self.isBST = False
        self.last = root.val

        self.inorder(root.right)