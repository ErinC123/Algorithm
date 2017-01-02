#   Question: 369. Plus One Linked List
# Difficulty: Easy
#       Tags: Linked List
'''
Given a non-negative number represented as a singly linked list of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    carry = 0
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        self.helper(head)
        if self.carry != 0:
            new = ListNode(self.carry)
            new.next = head
            head = new
        return head
    def helper(self, digit):
        if digit.next == None:
            digit.val += 1
            if digit.val == 10:
                digit.val, self.carry = 0, 1
            return
        self.helper(digit.next)
        digit.val += self.carry
        if digit.val == 10:
                digit.val, self.carry = 0, 1
        else:
            self.carry = 0