#   Question: 276. Paint Fence
# Difficulty: Easy
#       Tags: Dynamic Programming
'''
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

'''


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k * k
        n2, n1 = k, k * k
        for i in range(3, n + 1):
            ways = (k - 1) * (n2 + n1)
            n2 = n1
            n1 = ways
        return ways
