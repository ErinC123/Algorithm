#   Question: 448. Find all numbers disappeared in an array
# Difficulty: Easy
#       Tags: Array
'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and other appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list doest not count as extra space
eg.
Input: [4,3,2,7,8,2,3,1]    Output: [5,6]
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        not_exists = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                not_exists.append(i)
        return not_exists

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))