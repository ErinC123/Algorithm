#   Question: 217. Contains Duplicate
# Difficulty: Easy
#       Tags: Array, Hash Table
'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct
'''
from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = Counter(nums)
        return (any([v > 1 for k, v in dic.items()]))

s = Solution()
print(s.containsDuplicate([1,1,2,3]))