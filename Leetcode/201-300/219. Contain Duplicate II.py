#   Question: 219. Contains Duplicate II
# Difficulty: Easy
#       Tags: Array, Hash Table
'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k
'''
from collections import Counter
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = Counter(nums)                        # get the list of duplicate items
        dic = {i:x for i, x in enumerate(nums)}     # get the index of each item.  if use nums.index(x), you only get the index of the first instance x
        for fk, fv in freq.items():
            if fv > 1:
                index = []
                for dk, dv in dic.items():
                    if dv == fk:
                        index.append(dk)
                for i in range(1, len(index)):
                    if abs(index[i] - index[i-1]) <= k: # if difference between two index is at most k
                        return True

        return False

s = Solution()
print(s.containsNearbyDuplicate([1,1,3,1,3,1], 1))
