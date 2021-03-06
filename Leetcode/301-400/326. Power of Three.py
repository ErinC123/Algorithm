#   Question: 326. Power of Three
# Difficulty: Easy
#       Tags: Math
'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        while n%3 == 0:
            n = n/3
            if n == 1:
                return True
        return False

