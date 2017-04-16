from collections import Counter


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        lonelyB = 0
        columns = zip(*picture)
        for row_i in range(len(picture)):
            tmp = Counter(picture[row_i])
            if tmp['B'] == 1:
                col_i = picture[row_i].index('B')
                if 'B' not in columns[col_i][:row_i] and 'B' not in columns[col_i][row_i + 1:]:
                    lonelyB += 1

        return lonelyB
