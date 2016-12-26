#   Question: 119. Pascal's Triangle II
# Difficulty: Easy
#       Tags: Array
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
    Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(1, rowIndex+2):
            if i == 0: result.append([])
            if i == 1: result.append([1])
            if i == 2: result.append([1,1])
            else:
                last = result[len(result)-1]
                new = []
                for x in range(1, len(last)):
                    new.append(last[x-1]+last[x])
                    new.insert(0,1)
                    new.append(1)
                    result.append(new)
        return result[len(result)-1]

s = Solution()
print(s.getRow(3))