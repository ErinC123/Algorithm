#   Question: 24. Swap Nodes in Pairs
# Difficulty: Easy
#       Tags: Linked List
'''
Given a linked list, swap every two adjacent nodes and return its head.
For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3/
 Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
 changed.
'''

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None: return head
        else:
            prv = None
            n1 = head
            n2 = n1.next
            nxt = n2.next
            while n1 and n2:
                if prv:
                    prv.next = n2
                n2.next = n1
                n1.next = nxt
                if n1 == head:
                    head = n2
                prv = n1
                n1 = prv.next
                try:
                    n2 = n1.next
                    nxt = n2.next
                except Exception:
                    n2 = None
                    nxt = None
            return head