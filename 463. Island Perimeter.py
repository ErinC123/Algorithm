#   Question: 463. Island Perimeter
# Difficulty: Easy
#       Tags: Hash Table
'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,

and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water

inside that isn't connected to the water around the island). One cell is a square with side length 1.

The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

'''
'''
idea: island line = all lines - inner lines
'''

def checkInnerLines(self, lines):
    inners = 0;
    for line in lines:
        for i in range(1, len(line)):
            if line[i - 1] == 1 and line[i] == 1:
                inners += 1
    return inners


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lands = 0
        for line in grid:
            for i in line:
                if i == 1:
                    lands += 1

        inners = checkInnerLines(self, grid) + checkInnerLines(self, zip(*grid))
        return lands * 4 - inners * 2