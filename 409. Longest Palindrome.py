#   Question: 409. Longest Palindrome
# Difficulty: Easy
#       Tags: Hash Table
'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can
be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, x, dic = 0, 0, Counter(s).items()
        for k, v in dic:
            length += v
            if v%2 != 0:
                x += 1
        if x != 0:
            length = length-x+1
        return length