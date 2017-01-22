#   Question: 162. Find Peak Element
# Difficulty: Medium
#       Tags: Binary Search, Array
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:  # mid go up
                start = mid
            if nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:  # mid go down
                end = mid
            if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:  # mid is valley
                end = mid
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:  # mid is peak
                return mid

        if nums[end - 1] < nums[end] and end == len(nums) - 1: return end  # go up line, the last point is peak
        if start == 0 and nums[start] > nums[start + 1]: return start  # go down line, the first point is peak

        if nums[start - 1] < nums[start] and nums[start] > nums[start + 1]:
            return start
        if nums[end - 1] < nums[end] and nums[end] > nums[end + 1]:
            return end