#   Question: 101. Symmetric Tree
# Difficulty: Easy
#       Tags: Tree, DFS, BFS
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
   1
   / \
  2   2
   \   \
   3    3

   Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def invertTree(self, root):
        if not root: return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def sameTree(self, root1, root2):
        if not root1 and not root2: return True
        if root1 and root2:
            return root1.val == root2.val and self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        else: return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if root.left: self.invertTree(root.left)
        return self.sameTree(root.left, root.right)