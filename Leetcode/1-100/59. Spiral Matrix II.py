class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(n):
            matrix.append([0 for i in range(n)])

        t, d, l, r = 0, n - 1, 0, n - 1
        dir = 0
        val = 1
        while t <= d and l <= r:
            if dir == 0:
                for i in range(l, r + 1):
                    matrix[t][i] = val
                    val += 1
                t += 1
            elif dir == 1:
                for i in range(t, d + 1):
                    matrix[i][r] = val
                    val += 1
                r -= 1
            elif dir == 2:
                for i in range(r, l - 1, -1):
                    matrix[d][i] = val
                    val += 1
                d -= 1
            elif dir == 3:
                for i in range(d, t - 1, -1):
                    matrix[i][l] = val
                    val += 1
                l += 1
            dir = (dir + 1) % 4
        return matrix