#   Question: 371. Sum of Two Integers
# Difficulty: Easy
#       Tags: Bit Manipulation
'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        lst = []
        lst.append(a)
        lst.append(b)
        return(sum(lst))
s = Solution()
print(s.getSum(1,3))