#   Question: 113. Path Sum II
# Difficulty: Easy
#       Tags: Tree, DFS
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

        return
        [
         [5,4,11,2],
         [5,8,4,5]
        ]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lsts = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        else:
            self.lsts = []
            self.path(root, sum, [])
        return self.lsts

    def path(self, root, sum, lst):
        if not root.left and not root.right:
            lst.append(root.val)
            if sum == root.val:
                return self.lsts.append(lst)
            else:
                return None
        else:
            if root.left:
                self.path(root.left, sum-root.val, lst+[root.val])
            if root.right:
                self.path(root.right, sum-root.val, lst+[root.val])