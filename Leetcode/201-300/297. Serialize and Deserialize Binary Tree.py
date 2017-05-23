def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    res = []
    if root == None:    return res
    q = [root]
    while q:
        new_q = []
        res += [str(n.val) if n != None else None for n in q]
        for node in q:
            if node:
                new_q.append(node.left)
                new_q.append(node.right)
        q = new_q

    while res[-1] == None:
        res.pop()

    return res


def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data == []:    return None

    root = TreeNode(int(data[0]))
    queue = [root]
    isLeftChild = True
    index = 0

    for d in data[1:]:
        if d != None:
            node = TreeNode(d)
            if isLeftChild:
                queue[index].left = node
            else:
                queue[index].right = node
            queue.append(node)

        if not isLeftChild:
            index += 1

        isLeftChild = not isLeftChild
    return root