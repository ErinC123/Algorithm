#   Question: 299. Bulls and Cows
# Difficulty: Easy
#       Tags: Hash Table
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        counter_secret, counter_guess = Counter(secret), Counter(guess)
        for k, v in counter_secret.items():
            if k in counter_guess:
                cow += min(v, counter_guess[k])

        result = "{0}A{1}B".format(bull, cow-bull)
        return result