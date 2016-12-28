#   Question: 20. Valid Parentheses
# Difficulty: Easy
#       Tags: Stack, Strings
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''


class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.push(char)
            else:
                if stack.isEmpty() == True:
                    return False
                else:
                    former = stack.pop()
                    suppose_latter = ''
                    if former == '(':
                        suppose_latter = ')'
                    if former == '{':
                        suppose_latter = '}'
                    if former == '[':
                        suppose_latter = ']'
                    if char != suppose_latter:
                        return False
        if stack.isEmpty() == True:
            return True
        else:
            return False

