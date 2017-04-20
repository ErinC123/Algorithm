#   Question: 169. Majority Element
# Difficulty: Easy
#       Tags: Array, Divide and Conquer, Bit Manipulation
'''
Give an array of size n, find the majority element. The majority element is the element that appears more than
⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''


from collections import Counter
class Solution(object):
    # Method 1:
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]

    # Method 2:
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = Counter(nums)
        return(max(dic, key=dic.get))

s = Solution()
nums = [1,2,3,4,5,6,7,5,5,5,5,5,5,5,5,5,5,5,5]
print(s.majorityElement1(nums))
print(s.majorityElement2(nums))