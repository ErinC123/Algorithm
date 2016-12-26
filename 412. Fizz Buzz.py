#   Question: 412. Fizz Buzz
# Difficulty: Easy
#       Tags: None
'''
Write a program that outputs the string representation of numbers from 1 to n
But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output "FizzBuzz"

'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0:
            return result
        i = 1
        while i <= n:
            if i%15 == 0:
                result.append("FizzBuzz")
            elif i%3 == 0:
                result.append("Fizz")
            elif i%5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            i += 1
        return result

s = Solution()
print(s.fizzBuzz(15))