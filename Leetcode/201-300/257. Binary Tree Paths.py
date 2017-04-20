#   Question: 257. Binary Tree Paths
# Difficulty: Easy
#       Tags: Tree, DFS
'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:
   1
 /   \
2     3
 \
  5

All root-to-leaf paths are: ["1->2->5", "1->3"]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []
        self.Paths(root, "", paths)
        return paths

    def Paths(self, root, path, paths):
        if not root:
            return []
        if not root.left and not root.right:
            paths.append(path + str(root.val))
            path = []
        if root.left:
            self.Paths(root.left, path + str(root.val) + "->", paths)
        if root.right:
            self.Paths(root.right, path + str(root.val) + "->", paths)
