#   Question: 7. Reverse Integer
# Difficulty: Easy
#       Tags: Math
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        x = str(x)
        if x[0]=='-':
            if int('-'+x[1:][::-1]) > -2**31:
                result = int('-'+x[1:][::-1])
        else:
            if int(x[::-1]) < 2**31-1:
                result = int(x[::-1])
        return result