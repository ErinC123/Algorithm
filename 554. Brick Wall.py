class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        max_wid = sum(wall[0])
        edges = {}
        for l in wall:
            index = 0
            for b in l:
                index += b
                if index != max_wid:
                    edges[index] = edges.get(index, 0) + 1

        if edges == {}:
            return len(wall)

        return len(wall) - max(edges.values())