#   Question: 28. Implement strStr()
# Difficulty: Easy
#       Tags: Two Pointers, String
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        nlen = len(needle)
        for i in range(len(haystack)):
            if i+nlen and haystack[i:i+nlen] == needle:
                return i
        return -1
