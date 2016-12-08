#Tree
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

# preorder
import sys

def preOrder(root):
    sys.stdout.write(str(root.data)+" ")
    if root.left != None:
        preOrder(root.left)
    if root.right != None:
        preOrder(root.right)

# inorder
def inOrder(root):
    if root.left != None:
        inOrder(root.left)
    sys.stdout.write(str(root.data)+" ")
    if root.right != None:
        inOrder(root.right)

# postorder
def postOrder(root):
    if root.left != None:
        postOrder(root.left)
    if root.right != None:
        postOrder(root.right)
    sys.stdout.write(str(root.data)+" ")

# leetcode 404.sum of left leaves
def sumOfLeftLeaves(self, root):

    left_sum = 0
    if root == None:    #bound
        return 0
    if root.left != None and root.left.left == None and root.left.right == None: #left leaves
        left_sum += root.left.val
    left_sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) #break to subquestions
    return left_sum