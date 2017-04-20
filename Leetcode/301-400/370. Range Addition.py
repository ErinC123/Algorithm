class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0 for i in range(length + 1)]
        ret = []

        for u in updates:
            arr[u[0]] += u[2]
            arr[u[1] + 1] += -u[2]

        ret.append(arr[0])
        for num in arr[1:]:
            ret.append(ret[-1] + num)

        if len(ret) > length:
            ret.pop();

        return ret