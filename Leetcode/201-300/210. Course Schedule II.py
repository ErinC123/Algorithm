def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    map = {}
    q = []
    res = []
    for pair in prerequisites:
        map[pair[0]] = map.get(pair[0], 0) + 1

    for i in range(numCourses):
        if i not in map:
            q.append(i)
            res.append(i)

    if len(q) == 0: return []

    while q:
        n = q.pop(0)
        for pair in prerequisites:
            if pair[1] == n:
                map[pair[0]] = map.get(pair[0]) - 1

                if map[pair[0]] == 0:
                    q.append(pair[0])
                    res.append(pair[0])

    if len(res) == numCourses:
        return res
    else:
        return []