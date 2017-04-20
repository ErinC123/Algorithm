#   Question: 38. Count and Say
# Difficulty: Easy
#       Tags: Strings
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''
from itertools import groupby
def say(count):
    say = ""
    for k, g in groupby(count):
        say += str(sum(1 for _ in g))
        say += str(k)
    return say

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = "1"
        for i in range(n-1):
          count = say(count)
        return count