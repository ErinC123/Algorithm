class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0: return False

        x, y, cnt = 0, len(matrix[0]) - 1, 0
        while x <= len(matrix) - 1 and y >= 0:
            print(matrix[x][y])
            if matrix[x][y] == target:
                cnt += 1
                x += 1
                y -= 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return cnt > 0