#   Question: 290. Word Pattern
# Difficulty: Easy
#       Tags: Hash Table
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

from collections import OrderedDict, Counter
class OrderedCounter(Counter, OrderedDict):
    pass

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        result = False
        dic_pattern = OrderedCounter(pattern)
        str_pattern = OrderedCounter(str.split(' '))
        if len(dic_pattern)==len(str_pattern):
            if all(x in dic_pattern.values() for x in str_pattern.values()):
                result = True
        return result