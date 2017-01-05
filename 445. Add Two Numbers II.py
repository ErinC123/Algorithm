#   Question: 445. Add Two Numbers II
# Difficulty: Medium
#       Tags: Linked List
'''
You are given two linked lists representing two non-negative numbers. The most significant digit comes first and
 each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

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
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        return self.NumToLinkedList(self.LinkedListToNum(l1) + self.LinkedListToNum(l2))

    def LinkedListToNum(self, head):
        num = ""
        while head:
            num += str(head.val)
            head = head.next
        return int(num)

    def NumToLinkedList(self, num):
        str_num = str(num)
        head = ListNode(str_num[0])
        cur = head
        for n in str_num[1:]:
            node = ListNode(n)
            cur.next = node
            cur = node
        return head