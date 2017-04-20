#   Question: 160. Intersection of Two Linked Lists.
# 1-100: 101-200
#       Tags: Linked List
'''
Write a program to find the node at which the intersection fo two singly linked lists begins.
For example, the following two linked lists:

    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗
    B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        pA, pB = 0, 0
        nA, nB = headA, headB
        l, s = headA, headB
        while nA:
            pA += 1
            nA = nA.next
        while nB:
            pB += 1
            nB = nB.next
        if pA < pB:
            gc.collect()
            s = headA
            l = headB
        for i in range(abs(pA - pB)):
            l = l.next
        while s:
            if s == l:
                return s
            else:
                try:
                    s = s.next
                    l = l.next
                except Exception:
                    return None