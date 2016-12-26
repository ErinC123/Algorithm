#   Question: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
#       Tags: Array, Two Pointers
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Give input array nums = [1,1,2]
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't
matter what you leave beyond the new length.
'''
from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = OrderedDict.fromkeys(nums).keys()  # nums[:] does not allocate new memory
        return (len(nums))

s = Solution()
print(s.removeDuplicates([1,1,2]))