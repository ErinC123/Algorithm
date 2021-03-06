#   Question: 415. Add Strings
# Difficulty: Easy
#       Tags: Math
'''
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
def convertNum(str):
    digit = 0
    num = 0
    for ele in str[::-1]:
        num += int(ele)*(10**digit)
        digit += 1
    return num
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(convertNum(num1)+convertNum(num2))