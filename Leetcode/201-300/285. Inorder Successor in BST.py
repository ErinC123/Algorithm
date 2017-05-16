# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None

        while root and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root == None:    return None

        if root.right == None:
            return successor

        root = root.right
        while root.left:
            root = root.left
        return root