#   Question: 66. Plus One
# Difficulty: Easy
#       Tags: Array, Math
'''
Given a non-negative number represented an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        digits[length-1] += 1                   # last digit plus one
        if digits[length-1] > 9:                # if last digit is 10:
            for i in range(length-1, -1, -1):   # carry over
                if digits[i] > 9:               # if digit == 10
                    digits[i] = 0               # digit = 0
                    if i == 0:                  # if the digit is the highest digit of the number, 进位
                        digits.insert(0, 1)
                    else:                       # if the digit is not the highest digit, digit[i-1] plus one
                        digits[i-1] += 1
        return digits

s = Solution()
print(s.plusOne([9,9]))

