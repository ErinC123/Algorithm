#   Question: 21. Merge Two Sorted Lists
# Difficulty: Easy
#       Tags: Linked List
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            smallerNode = l1
            smallerNode.next = self.mergeTwoLists(l1.next, l2)
        else:
            smallerNode = l2
            smallerNode.next = self.mergeTwoLists(l1, l2.next)
        return smallerNode
