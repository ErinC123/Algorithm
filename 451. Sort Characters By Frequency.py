from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        hs = reversed(sorted(Counter(s).items(), key=lambda (k,v): v))
        for k,v in hs:
            ret += k*v
        return ret