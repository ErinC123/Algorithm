#   Question: 400. Nth Digit
# Difficulty: Easy
#       Tags: Math
'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:
3

Output:
3

Example 2:
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = n
        i = 1
        while index > (10**i - 10**(i-1))*i:
            index -= (10 ** i - 10 ** (i - 1)) * i
            i += 1
        if index%i == 0:
            integer = 10**(i-1)+(index/i)-1
            return int(str(integer)[i-1])
        else:
            integer = 10**(i-1)+(index//i)
            return int(str(integer)[index%i-1])