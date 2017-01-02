#   Question: 206. Reverse Linked List
# Difficulty: Easy
#       Tags: Linked List
'''
Reverse a singly linked list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur_node = head
        prv_node = None
        next_node = head.next
        while cur_node:
            cur_node.next = prv_node
            prv_node = cur_node
            cur_node = next_node
            try:
                next_node = next_node.next
            except Exception:
                return prv_node

    # Better solutions
    # Iterative way
    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
           return head
        dummy = ListNode(-1)
        cur = head
        while cur:
            tmp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = tmp
        return dummy.next

    # Recursive way
    newHead = ListNode(-1)
    def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        self.helper(head)
        return self.newHead

    def helper(self, p):
        if not p.next:
            self.newHead = p
            return self.newHead

        self.helper(p.next)
        q = p.next
        q.next = p
        p.next = None
        
