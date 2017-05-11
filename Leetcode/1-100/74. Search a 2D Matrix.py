class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False

        # target row
        row_idx = self.findTargetRow(matrix, target)

        # target position in the row
        return self.findTarget(matrix[row_idx], target)

    def findTargetRow(self, matrix, target):
        if target > matrix[len(matrix) - 1][0]: return len(matrix) - 1
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid

        if matrix[start][0] == target:
            return start

        if matrix[end][0] == target:
            return end
        if matrix[start][0] > target:
            if start < 0:
                return start
            return start - 1
        if end < 0:
            return end
        return end - 1

    def findTarget(self, row, target):
        start, end = 0, len(row) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if row[mid] > target:
                end = mid
            else:
                start = mid

        if row[end] == target or row[start] == target:
            return True
        return False