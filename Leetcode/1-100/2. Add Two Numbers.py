#   Question: 2. Add Two Numbers
# Difficulty: Easy
#       Tags: Linked List, Math
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []
        result = ListNode(0)
        head = result
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val < 10:
                result.next, carry = ListNode(val), 0
            else:
                result.next, carry = ListNode(val%10), val/10
            l1, l2, result = l1.next, l2.next, result.next
        while l1:
            val = l1.val + carry
            if val < 10:
                result.next, carry = ListNode(val), 0
            else:
                result.next, carry = ListNode(val%10), val/10
            l1, result = l1.next, result.next
        while l2:
            val = l2.val + carry
            if val < 10:
                result.next, carry = ListNode(val), 0
            else:
                result.next, carry = ListNode(val%10), val/10
            l2, result = l2.next, result.next
        if carry != 0:
            result.next = ListNode(carry)
        if head.next:
            head = head.next
        return head