#   Question: 83.Remove Duplicates from Sorted List
# 1-100: 101-200
#       Tags: Linked List
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        nxt = head.next
        while nxt:
            if nxt.val != cur.val:
                cur.next = nxt
                cur = nxt
            nxt = nxt.next
            if not nxt:
                cur.next = nxt
        return head