class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        map = {}
        q = []
        cnt = 0
        for pair in prerequisites:
            map[pair[1]] = map.get(pair[1], 0) + 1

        for i in range(numCourses):
            if i not in map:
                q.append(i)
                cnt += 1

        if len(q) == 0: return False

        while q:
            n = q.pop(0)
            for pair in prerequisites:
                if pair[0] == n:
                    map[pair[1]] = map.get(pair[1]) - 1

                    if map[pair[1]] == 0:
                        q.append(pair[1])
                        cnt += 1

        return cnt == numCourses