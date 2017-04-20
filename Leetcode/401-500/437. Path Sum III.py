#   Question: 437. Path Sum III
# Difficulty: Easy
#       Tags: Array, Hash Table
'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent
nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        def helper(root, sum):
            if not root:
                return []
            if not root.left and not root.right:
                if root.val == sum:
                    self.count += 1
                return [root.val]
            lefts = helper(root.left, sum)
            rights = helper(root.right, sum)
            path_sums = [root.val] + [i+root.val for i in lefts] + [i+root.val for i in rights]
            self.count += path_sums.count(sum)
            return path_sums
        helper(root, sum)
        return self.count