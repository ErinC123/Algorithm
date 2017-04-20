#   Question: 205. Isomorphic Strings
# Difficulty: Easy
#       Tags: Hash Table
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

'''
from collections import OrderedDict
def geneNum(str):
        nums = []
        hash = {}
        for i in range(len(str)):
            if str[i] not in hash:
                nums.append(i)
                hash[str[i]] = i
            else:
                nums.append(hash[str[i]])
        return nums

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result = False
        if geneNum(s) == geneNum(t):
            result =True
        return result
