#   Question: 88. Merge Sorted Array
# Difficulty: Easy
#       Tags: Array, Two Pointers
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    You may assume that nums1 has enought space(size that is greater or equal to m+n) to hold additional elements
    from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
