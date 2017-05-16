class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findStartPos(nums, target), self.findEndPos(nums, target)]

    def findStartPos(self, nums, target):
        if len(nums) == 0: return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def findEndPos(self, nums, target):
        if len(nums) == 0: return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1