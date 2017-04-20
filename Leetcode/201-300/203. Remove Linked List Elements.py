#   Question: 203. Remove Linked List Elements
# Difficulty: Easy
#       Tags: Linked List
'''
Remove all elements from a linked list of integers that have value val.
Example:
    Given: 1->2->6->3->4->5->6, val = 6
    Return 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                prv = None
                cur = head
                nxt = cur.next
                while cur:
                    if cur.val == val:
                        if prv != None:
                            prv.next = nxt
                    else:
                        prv = cur
                    cur = nxt
                    try:
                        nxt = nxt.next
                    except Exception:
                        nxt = None
                return head
        return head