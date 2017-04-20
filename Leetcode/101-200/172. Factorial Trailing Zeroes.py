#   Question: 172. Factorial Trailing Zeroes
# Difficulty: Easy
#       Tags: Math
'''
Given an integer n, return the number of trailing zeroes in n!
Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros = 0
        while n > 0:
            n = n/5
            zeros += n
        return zeros
    