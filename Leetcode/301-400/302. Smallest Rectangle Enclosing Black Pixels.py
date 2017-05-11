# class Solution(object):
#     def minArea(self, image, x, y):
#         """
#         :type image: List[List[str]]
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         a = self.calc_range(image)
#         b = self.calc_range(zip(*image))
#         return a * b
#
#     def calc_range(self, image):
#         ret = 0
#         for l in image:
#             ret |= int(''.join(l), 2)
#         return bin(ret).count("1")

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        n = len(image[0])

        left = self.findLeft(image, 0, y)
        right = self.findRight(image, y, n - 1)
        top = self.findTop(image, 0, x)
        bottom = self.findBottom(image, x, m - 1)

        return (right - left + 1) * (bottom - top + 1)

    def findLeft(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) / 2
            if self.isEmptyCol(image, mid):
                start = mid
            else:
                end = mid

        if self.isEmptyCol(image, start):
            return end
        return start

    def findRight(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) / 2
            if self.isEmptyCol(image, mid):
                end = mid
            else:
                start = mid

        if self.isEmptyCol(image, end):
            return start
        return end

    def findTop(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) / 2
            if self.isEmptyRow(image, mid):
                start = mid
            else:
                end = mid

        if self.isEmptyRow(image, start):
            return end
        return start

    def findBottom(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) / 2
            if self.isEmptyRow(image, mid):
                end = mid
            else:
                start = mid

        if self.isEmptyRow(image, end):
            return start
        return end

    def isEmptyCol(self, image, col_idx):
        for i in range(len(image)):
            if image[i][col_idx] == "1":
                return False
        return True

    def isEmptyRow(self, image, row_idx):
        for i in range(len(image[0])):
            if image[row_idx][i] == "1":
                return False
        return True