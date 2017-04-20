#   Question: 118. Pascal's Triangle
# 1-100: 101-200
#       Tags: Array
'''
Given numRows, generate the first numRows of Pascal's triangle.
For example, give numRow = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows+1):
            if i == 0: result.append([])
            if i == 1: result.append([1])
            elif i == 2: result.append([1,1])
            else:
                last = result[len(result)-1]
                new = []
                for x in range(1, len(last)):
                    new.append(last[x-1]+last[x])
                    new.insert(0,1)
                    new.append(1)
                    result.append(new)
        return result

s = Solution()
print(s.generate(5))



