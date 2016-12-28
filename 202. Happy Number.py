#   Question: 202. Happy Number
# Difficulty: Easy
#       Tags: Math, Hash Table
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace
the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
'''
if there is number that shows up more than once. There is a cycle
'''
def calc(num):
    nums = list(int(i) for i in str(num))
    return sum([i ** 2 for i in nums])


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ha = {}
        result = True
        while n != 1:
            n = calc(n)
            ha[n] = ha.get(n, 0) + 1;
            if 2 in ha.values():
                result = False
                break
        return result