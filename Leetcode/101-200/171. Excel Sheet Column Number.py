#   Question: 171. Excel Sheet Column Number
# Difficulty: Easy
#       Tags: Math
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        num = 0
        digit = 0
        for ele in s:
            num += (ord(ele)-64)*(26**digit)
            digit += 1
        return num