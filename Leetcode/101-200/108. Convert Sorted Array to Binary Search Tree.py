# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: return None

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l > r:  return None
        if l == r: return TreeNode(nums[l])

        mid = (l + r) / 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, l, mid - 1)
        node.right = self.helper(nums, mid + 1, r)
        return node