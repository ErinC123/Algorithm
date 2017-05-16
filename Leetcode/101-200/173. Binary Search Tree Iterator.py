# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.cur   = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur != None or len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        while self.cur != None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        next = self.cur
        self.cur = self.cur.right
        return next.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())