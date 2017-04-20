#   Question: 70. Climbing Stairs
# Difficulty: Easy
#       Tags: Dynamic Programming
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        steps = [1, 1]
        for i in range(2, n+1):
            steps.append(steps[i-1]+steps[i-2])
        return steps[-1]