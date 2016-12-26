#   Question: 344. Reverse String
# Difficulty: Easy
#       Tags: Two Pointers, String
'''
Write a function that takes a string as input and returns the string reversed.

eg.
Given s = "hello", return "olleh".

'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

