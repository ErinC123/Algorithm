# Tree: Preorder Traversal
# def preOrder(root):
#     # Write your code here
#     res = helper(root)
#     print ' '.join(str(p) for p in res)
#
#
# def helper(root):
#     res = []
#
#     if root == None:    return res
#
#     left = helper(root.left)
#     right = helper(root.right)
#
#     res.append(root.data)
#     res += left
#     res += right
#     return res

# Tree: Postorder Traversal
# def postOrder(root):
#     # Write your code here
#     res = helper(root)
#     print(' '.join(str(i) for i in res))
#
#
# def helper(root):
#     res = []
#
#     if root == None:    return res
#
#     left = helper(root.left)
#     right = helper(root.right)
#
#     res += left + right
#     res.append(root.data)
#     return res

# Tree: Inorder Traversal
# def inOrder(root):
#     # Write your code here
#     res = helper(root)
#     print(' '.join(str(i) for i in res))
#
#
# def helper(root):
#     res = []
#
#     if root == None:    return res
#
#     left = helper(root.left)
#     right = helper(root.right)
#
#     res += left
#     res.append(root.data)
#     res += right
#     return res

# Tree: Height of a Binary Tree
# def height(root):
#     return helper(root) - 1
#
#
# def helper(root):
#     if root == None: return 0
#
#     left_h = helper(root.left)
#     right_h = helper(root.right)
#     h = 1 + max(left_h, right_h)
#     return h

# Tree : Top View
# def topView(root):
#     # Write your code here
#     res = []
#     if root.left != None:
#         goLeft(root.left, res)
#
#     res.append(root.data)
#
#     if root.right != None:
#         goRight(root.right, res)
#
#     print(' '.join(str(i) for i in res))
#
#
# def goLeft(node, res):
#     if node.left != None:
#         goLeft(node.left, res)
#     res.append(node.data)
#
#
# def goRight(node, res):
#     res.append(node.data)
#     if node.right != None:
#         goRight(node.right, res)

# Tree: Level Order Traversal
# def levelOrder(root):
#     # Write code Here
#     res = []
#
#     if root == None:    return res
#
#     q = [root]
#     while q:
#         new_q = []
#         res += [n.data for n in q]
#         for node in q:
#             if node.left:
#                 new_q.append(node.left)
#             if node.right:
#                 new_q.append(node.right)
#         q = new_q
#
#     print(' '.join(str(i) for i in res))


# Binary Search Tree : Insertion
# def insert(r, val):
#     # Enter you code here.
#     new = Node(val)
#
#     return helper(r, new)
#
#
# def helper(r, new):
#     if r == None:   return new
#
#     if r.data > new.data:
#         r.left = helper(r.left, new)
#     else:
#         r.right = helper(r.right, new)
#     return r

# Binary Search Tree : Lowest Common Ancestor
# def lca(root, v1, v2):
#     # Enter your code here
#     if root == None or root.data == v1 or root.data == v2:
#         return root
#     left = lca(root.left, v1, v2)
#     right = lca(root.right, v1, v2)
#
#     if left and right:  return root
#     if left:    return left
#     if right:   return right
#     return None

# Is This a Binary Search Tree?
#     def isValidBST(self, root):
#         # write your code here
#         import sys
#         self.lastVal = -sys.maxint
#         self.isBST = True
#         self.helper(root)
#         return self.isBST
#
#     def helper(self, root):
#         if root == None:    return
#
#         self.helper(root.left)
#
#         if self.lastVal >= root.val:
#             self.isBST = False
#             return
#         self.lastVal = root.val
#
#         self.helper(root.right)