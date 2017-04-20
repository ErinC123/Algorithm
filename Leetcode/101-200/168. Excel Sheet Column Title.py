#   Question: 168. Excel Sheet Column Title
# 1-100: 101-200
#       Tags: Array, Hash Table
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

eg.
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n!=0:
            result += chr((n-1)%26+65)
            n = (n-1)/26
        return result[::-1]