from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0
        ret = []
        hs = reversed(sorted(Counter(nums).items(), key=lambda (key,value): value))
        for key, value in hs:
            if i < k:
                ret.append(key)
                i += 1
        return sorted(ret)