# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        self.nums = []
        self.inorder(root, key)
        return self.build(0, len(self.nums) - 1)

    def inorder(self, root, key):

        if root == None:    return

        self.inorder(root.left, key)
        if root.val != key:
            self.nums.append(root.val)
        self.inorder(root.right, key)

    def build(self, l, r):
        if l > r:   return None
        if l == r:  return TreeNode(self.nums[l])

        mid = (l + r) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node