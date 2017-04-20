#   Question: 19. Remove Nth Node From End of List
# 1-100: 101-200
#       Tags: Linked List, Two Pointers
'''
Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list become 1->2->3->5.
Note:
    Given n will always be valid.
    Try to do this in one pass.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next: return None
        end = head
        prv_tar = None
        target = head
        for i in range(n-1):
            end = end.next
        while end.next:
            end = end.next
            prv_tar = target
            target = target.next
        if not prv_tar: return head.next
        else:
            prv_tar.next = target.next
        return head
    