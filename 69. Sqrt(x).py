#   Question: 69. Sqrt(x)
# Difficulty: Medium
#       Tags: Binary Search, Math
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid ** 2 == x:
                end = mid
            if x < mid ** 2:
                end = mid
            if mid ** 2 < x:
                start = mid

        if end ** 2 <= x:
            return end
        if start ** 2 <= x:
            return start
        else:
            return -1