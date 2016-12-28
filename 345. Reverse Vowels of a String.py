#   Question: 345. Reverse Vowels of a String
# Difficulty: Easy
#       Tags: Two Pointers, String
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        s = list(s)
        for ele in s:
            if ele in 'aeiouAEIOU':
                vowels.append(ele)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels.pop()
        return "".join(s)