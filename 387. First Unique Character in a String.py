#   Question: 387. First Unique Character in a String
# Difficulty: Easy
#       Tags: Array, Hash Table
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

eg.
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''

from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        uniq = []
        s_hash = Counter(s)
        for k, v in s_hash.items():
            if v == 1:
                uniq.append(k)

        if len(uniq) == 0:
            return -1

        for i in range(len(s)):
            if s[i] in uniq:
                return i