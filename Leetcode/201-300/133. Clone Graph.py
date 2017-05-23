class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:    return None
        # clone nodes
        q = [node]
        nodes = [node]
        mapping = {}
        mapping[node] = UndirectedGraphNode(node.label)
        while q:
            n = q.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in mapping:
                    q.append(neighbor)
                    new = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)
                    mapping[neighbor] = new

        # clone edges
        for n in nodes:
            for neighbor in n.neighbors:
                mapping[n].neighbors.append(mapping[neighbor])

        return mapping[node]