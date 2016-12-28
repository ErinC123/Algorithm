#   Question: 9. Palindrome Number
# Difficulty: Easy
#       Tags: Math
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False