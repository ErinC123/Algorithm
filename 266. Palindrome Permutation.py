#   Question: 266. Palindrome Permutation
# Difficulty: Easy
#       Tags: Hash Table
'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

'''
'''
idea: 数量为奇数的数字必须少于等于1
'''
from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        qs = 0
        s_hash = Counter(s)
        for k, v in s_hash.items():
            if v%2 != 0:
                qs += 1
        if qs > 1:
            return False
        else:
            return True

s = Solution()
print(s.canPermutePalindrome("carerac"))