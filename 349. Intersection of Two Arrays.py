#   Question: 349. Intersection of Two Arrays
# Difficulty: Easy
#       Tags: Binary Search, Hash Table, Two Pointers, Sort
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        set1, set2 = set(nums1), set(nums2)
        for e in set1:
            if e in set2:
                result.append(e)
        return result