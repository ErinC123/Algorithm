#   Question: 102. Binary Tree Level Order Traversal
# Difficulty: Easy
#       Tags: Tree, BFS
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
   return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cur, lsts = [root], [[root.val]]
        while cur:
            next_lst, next_lst_node = [], []
            for node in cur:
                if node.left:
                    next_lst_node.append(node.left)
                    next_lst.append(node.left.val)
                if node.right:
                    next_lst_node.append(node.right)
                    next_lst.append(node.right.val)
            if next_lst != []:
                lsts.append(next_lst)
            cur = next_lst_node
        return lsts