#   Question: 414. Third Maximum Number
# Difficulty: Easy
#       Tags: Array
'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
the maximum number. The time complexity must be in O(n).

eg1,
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

eg2,
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

eg3,
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''

from collections import Counter
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))[::-1]
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]

s = Solution()
print(s.thirdMax([3,2,1]))