class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1 and len(edges) == 0: return True
        if n == 0:  return False
        if len(edges) != n - 1:   return False

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        q = [min(graph.keys())]
        nodes = []
        while q:
            node = q.pop(0)
            for neighbor in graph[node]:
                if neighbor in nodes:
                    continue
                nodes.append(neighbor)
                q.append(neighbor)

        return len(nodes) == n