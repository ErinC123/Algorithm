#   Question: 258. Add Digits
# Difficulty: Easy
#       Tags: Math
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(i) for i in str(num)]
        while len(digits) > 1:
          temp = sum(digits)
          digits = [int(i) for i in str(temp)]
        return sum(digits)

s = Solution()
print(s.addDigits(38))