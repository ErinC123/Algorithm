#   Question: 136. Single Number
# Difficulty: Easy
#       Tags: Hash Table, Bit Manipulation
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ha = Counter(nums)
        result = 0
        for k,v in ha.items():
            if v == 1:
                result = k
        return result

s = Solution()
print(s.singleNumber([1,2, 3, 2, 7, 1, 7]))