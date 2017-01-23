#   Question: 33. Search in Rotated Sorted Array
# Difficulty: Hard
#       Tags: Binary Search, Array
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    def locateMinPoint(self, nums):
        start, end, bound = 0, len(nums) - 1, nums[len(nums) - 1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == bound:
                end = mid
            if nums[mid] < bound:
                end = mid
            if bound < nums[mid]:
                start = mid
        if nums[start] <= bound:
            return start
        else:
            return end

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        min_point_index = self.locateMinPoint(nums)
        if target <= nums[len(nums) - 1]:  # the later part
            start, end = min_point_index, len(nums) - 1
        else:  # the former part
            start, end = 0, min_point_index - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                end = mid
            if target < nums[mid]:
                end = mid
            if target > nums[mid]:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        else:
            return -1