#   Question: 62. Unique Paths
# Difficulty: 201-300
#       Tags: Dynamic Programming, Array
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
 of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def helper(m, n, row, col, grids):
            if row > m or col > n:
                return 0
            if row == m and col == n:
                return 1
            if grids[row][col] == 0:
                grids[row][col] = helper(m, n, row+1, col, grids) + helper(m, n, row, col+1, grids)
            return grids[row][col]
        grids = [[0] * n for _ in range(m)]
        return helper(m-1, n-1, 0, 0, grids)