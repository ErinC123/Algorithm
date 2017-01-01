#   Question: 107. Binary Tree Level Order Traversal II
# Difficulty: Easy
#       Tags: Tree
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        cur, lst_val = [root], [[root.val]]
        while cur:
            nxt, nxt_val = [], []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                    nxt_val.append(node.left.val)
                if node.right:
                    nxt.append(node.right)
                    nxt_val.append(node.right.val)
                if nxt_val != []:
                    lst_val.append(nxt_val)
                cur = nxt
        return lst_val[::-1]

