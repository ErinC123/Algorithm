#   Question: 238. Product of Array Except Self
# Difficulty: Easy
#       Tags: Array
'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for
the purpose of space complexity analysis.)
'''
'''
idea:
result1 = [1, 1*num1, 1*num1*num2, 1*num1*num2*num3]
result2 = [1, 1*num4, 1*num4*num3, 1*num4*num3*num2]
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result1, result2, result = [1], [1], []
        for i in range(0, length-1):
            result1.append(result1[len(result1)-1]*nums[i])
        for i in range(length-1, 0, -1):
            result2.append(result2[len(result2)-1]*nums[i])
        for i in range(0, length):
            result.append(result1[i]*result2[length-i-1])
        print(result1,result2)
        return result
