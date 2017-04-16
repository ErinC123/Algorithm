from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        ht = Counter(nums)
        for k, v in ht.items():
            if v == 2:
                ret.append(k)
        return ret