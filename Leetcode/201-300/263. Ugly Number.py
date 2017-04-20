#   Question: 263. Ugly Number
# Difficulty: Easy
#       Tags: Math
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14
 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype:bool
        """
        uglyFactors = [1, 2, 3, 5]
        if num in uglyFactors:
            return True
        else:
            while num not in uglyFactors:
                prev = num
                for factor in [2, 3, 5]:
                    if num%factor == 0:
                        num = num/factor
                if num == prev:
                    return False
            return True  