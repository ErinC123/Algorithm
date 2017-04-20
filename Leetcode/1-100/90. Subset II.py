#   Question: 78. Subsets
# Difficulty: Admin
#       Tags: Array, Backtracking
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        subsets_copy = [] + subsets
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                l = len(subsets_copy)
            for j in range(len(subsets_copy)-l, len(subsets_copy)):
                subsets += [subsets_copy[j]+[nums[i]]]
            subsets_copy = []+subsets
        return subsets

s = Solution()
print(s.subsetsWithDup([1,2,2,2,2]))