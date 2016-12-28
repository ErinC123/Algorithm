#   Question: 14. Longest Common Prefix
# Difficulty: Easy
#       Tags: Strings
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        columns = zip(*strs)
        prefix = ""
        for column in columns:
            if all(column[0] == c for c in column):
                prefix = prefix + column[0]
            else:
                return prefix
        return prefix