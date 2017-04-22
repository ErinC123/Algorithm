# Print the Elements of a Linked List
"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""
# def print_list(head):
#     tmp = head
#     while tmp:
#         print(tmp.data)
#         tmp = tmp.next

# Insert a Node at the Tail of a Linked List
# """
#  Insert Node at the end of a linked list
#  head pointer input could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method
# """
#
#
# def Insert(head, data):
#     if head == None:
#         head = Node(data)
#     else:
#         tail = head
#         while tail.next:
#             tail = tail.next
#         new = Node(data)
#         tail.next = new
#     return head

# Insert a node at the head of a linked list
# """
#  Insert Node at the begining of a linked list
#  head input could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
# def Insert(head, data):
#     if head == None:
#         head = Node(data)
#     else:
#         new = Node(data)
#         new.next = head
#         head = new
#     return head

# Insert a node at a specific position in a linked list
# """
#  Insert Node at a specific position in a linked list
#  head input could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
# # This is a "method-only" submission.
# # You only need to complete this method.
# def InsertNth(head, data, position):
#     if head == None:
#         head = Node(data, head)
#     elif position == 0:
#         node = Node(data, head)
#         head = node
#     else:
#         p = head
#         i = 0
#         while i + 1 < position:
#             p = p.next
#             i += 1
#         new = Node(data)
#         new.next = p.next
#         p.next = new
#     return head

# Delete a Node
# """
#  Delete Node at a given position in a linked list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
#
# def Delete(head, position):
#     if head != None:
#         if position == 0:
#             tmp = head.next
#             head.next = None
#             head = tmp
#         else:
#             i = 0
#             p = head
#             while i + 1 < position:
#                 p = p.next
#                 i += 1
#             p.next = p.next.next
#     return head

# Print in Reverse
# """
#  Print elements of a linked list in reverse order as standard output
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#
# """
#
#
# def ReversePrint(head):
#     if head != None:
#         ReversePrint(head.next)
#         print(head.data)

# Reverse a linked list
# """
#  Reverse a linked list
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
#
# def Reverse(head):
#     if head != None:
#         p = head
#         while p.next != None:
#             tmp = p.next
#             p.next = p.next.next
#             tmp.next = head
#             head = tmp
#     return head

# Compare two linked lists
# """
#  Merge two linked list
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
#
# def CompareLists(headA, headB):
#     a, b = headA, headB
#     while a != None and b != None:
#         if a.data == b.data:
#             a, b = a.next, b.next
#         else:
#             return 0
#     if a == None and b == None:
#         return 1
#     else:
#         return 0

# Merge two sorted linked lists
# """
#  Merge two linked lists
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
#
# def MergeLists(headA, headB):
#     if headA == None: return headB
#     if headB == None: return headA
#
#     if headA.data < headB.data:
#         head = headA
#         headA = headA.next
#     else:
#         head = headB
#         headB = headB.next
#
#     head.next = MergeLists(headA, headB)
#     return head

# Get Node Value
# Body
# """
#  Get Node data of the Nth Node from the end.
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the node data of the linked list in the below method.
# """
#
#
# def GetNode(head, position):
#     if head != None:
#         list_len = 0
#         p = head
#         while p != None:
#             p = p.next
#             list_len += 1
#
#         pos_f = list_len - (position + 1)
#         p = head
#         i = 0
#         while i < pos_f:
#             p = p.next
#             i += 1
#         return p.data

# Delete duplicate-value nodes from a sorted linked list
# """
#  Delete duplicate nodes
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#  return back the head of the linked list in the below method.
# """
#
#
# def RemoveDuplicates(head):
#     if head != None:
#         p = head
#         while p != None and p.next != None:
#             if p.next.data == p.data:
#                 p.next = p.next.next
#             else:
#                 p = p.next
#     return head

# Cycle Detection
# """
# Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
#
# A Node is defined as:
#
#     class Node(object):
#         def __init__(self, data = None, next_node = None):
#             self.data = data
#             self.next = next_node
# """
#
#
# def has_cycle(head):
#     slow, fast = head, head.next
#     while slow != None and fast != None:
#         fast = fast.next
#         slow = slow.next
#         if fast == slow:
#             return 1
#     return 0

# Find Merge Point of Two Lists
# """
#  Find the node at which both lists merge and return the data of that node.
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None):
#        self.data = data
#        self.next = next_node
#
#
# """
#
# def calc_len(head):
#     list_len = 0
#     if head != None:
#         p = head
#         while p:
#             list_len += 1
#             p = p.next
#     return list_len
#
#
# def FindMergeNode(headA, headB):
#     len_a, len_b = calc_len(headA), calc_len(headB)
#     if len_a < len_b:
#         pos = len_b - len_a
#         i = 0
#         while i < pos:
#             headB = headB.next
#             i += 1
#     elif len_b < len_a:
#         pos = len_a - len_b
#         i = 0
#         while i < pos:
#             headA = headA.next
#             i += 1
#
#     a_cur = headA
#     b_cur = headB
#     while a_cur != None:
#         if a_cur != b_cur:
#             a_cur = a_cur.next
#             b_cur = b_cur.next
#         else:
#             return a_cur.data
#     return None

# Inserting a Node Into a Sorted Doubly Linked List
# """
#  Insert a node into a sorted doubly linked list
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None, prev_node = None):
#        self.data = data
#        self.next = next_node
#        self.prev = prev_node
#
#  return the head node of the updated list
# """
#
#
# def SortedInsert(head, data):
#     new = Node(data)
#     if head == None:
#         head = new
#     else:
#         if new.data < head.data:
#             new.next = head
#             head = new
#         else:
#             pre, cur = None, head
#             while cur != None and cur.data < new.data:
#                 pre = cur
#                 cur = cur.next
#             new.next = pre.next
#             pre.next = new
#
#     return head

# # Reverse a doubly linked list
# """
#  Reverse a doubly linked list
#  head could be None as well for empty list
#  Node is defined as
#
#  class Node(object):
#
#    def __init__(self, data=None, next_node=None, prev_node = None):
#        self.data = data
#        self.next = next_node
#        self.prev = prev_node
#
#  return the head node of the updated list
# """
#
#
# def Reverse(head):
#     if head != None and head.next != None:
#         p = head
#         new_h = p
#         while p != None:
#             tmp = p.next
#             p.next = p.prev
#             p.prev = tmp
#             new_h = p
#             p = tmp
#         return new_h
#     return head