#   Question: 231. Power of Two
# Difficulty: Easy
#       Tags: Math, Bit Manipulation
'''
Given an integer, write a function to determine if it is a power of two.
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = False
        if n == 0:
            return result
        if n == 1:
            return True
        while n%2 == 0:
            n = n/2
            if n == 1:
                result = True
        return result