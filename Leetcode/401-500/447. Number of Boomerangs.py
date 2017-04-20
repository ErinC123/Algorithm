#   Question: 447. Number of Boomerangs
# Difficulty: Easy
#       Tags: Hash Table
'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that
the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the
range [-10000, 10000] (inclusive).

Example:
    Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

import math
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return 0
        res = 0
        for i in range(len(points)):
            pDict = {}
            for j in range(len(points)):
                if j == i:
                    continue
                dis = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                key = str(dis)
                if key in pDict:
                    pDict[key] += 1
                else:
                    pDict[key] = 1
            for p in pDict:
                if pDict[p] > 1:
                    res += pDict[p] * (pDict[p] - 1)
        return res