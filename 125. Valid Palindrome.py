#   Question: 125. Valid Palindrome
# Difficulty: Easy
#       Tags: Two-Pointers, Strings
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r"[^A-Za-z0-9]+", '', s).lower()
        if s == s[::-1]:
            return True
        else:
            return False
