#   Question: 204. Count Primes
# Difficulty: Easy
#       Tags: Math, Hash Table
'''
Description:
Count the number of prime numbers less than a non-negative number, n.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = [True]*n
        A[0:2] = [False]*2
        for i in range(2, int(n ** 0.5) + 1):
            if A[i]:
                A[i*i:n:i]=[False]*len(A[i*i:n:i])
        return sum(A)