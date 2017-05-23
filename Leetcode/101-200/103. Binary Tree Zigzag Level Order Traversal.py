# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        if root == None:    return self.res
        q = [root]
        isReverse = False
        while q:
            l = [n.val for n in q]
            if isReverse:
                l = l[::-1]
            isReverse = not isReverse
            self.res.append(l)

            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return self.res