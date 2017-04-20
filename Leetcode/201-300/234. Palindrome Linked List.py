#   Question: 234. Palindrome Linked List
# Difficulty: Easy
#       Tags: Linked List, Two Pointers
'''
Given a singly linked list, determine if it is a palindrome
'''

class Solution(object):
    def Reverse(self, head):
        current = head
        prv = None
        nxt = current.next
        while current:
            current.next = prv
            prv = current
            current = nxt
        try:
            nxt = nxt.next
        except Exception:
            return prv

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        slow = self.Reverse(slow)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next
        return True