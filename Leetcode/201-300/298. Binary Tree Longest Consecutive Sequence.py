class Solution(object):
    longest = 0

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.longest

    def helper(self, root):

        if root == None:    return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        subTreeLongest = 1
        if root.left and root.left.val == root.val + 1:
            subTreeLongest = max(left + 1, subTreeLongest)

        if root.right and root.right.val == root.val + 1:
            subTreeLongest = max(right + 1, subTreeLongest)

        if subTreeLongest > self.longest:
            self.longest = subTreeLongest

        return subTreeLongest