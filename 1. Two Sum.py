#   Question: 1. Two Sum
# Difficulty: Easy
#       Tags: Array, Hash Table
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

eg.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i+1:].count(x) > 0:  # if there is a element add current value equals to target
                result += [i, i+1+nums[i+1:].index(x)]
                break
        return result

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
