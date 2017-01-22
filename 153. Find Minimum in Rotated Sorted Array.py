#   Question: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
#       Tags: Binary Search, Array
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, bound = 0, len(nums)-1, nums[len(nums)-1]
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid] <= bound:
                end = mid
            if nums[mid] > bound:
                start = mid
        if nums[start] <= bound:
            return nums[start]
        if nums[end] <= bound:
            return nums[end]