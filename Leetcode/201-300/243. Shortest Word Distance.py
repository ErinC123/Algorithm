#   Question: 243. Shortest Word Distance
# Difficulty: Easy
#       Tags: Array
'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.
Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list
'''
'''
idea:
1. create lst_word1 to store all indexes of word1 and lst_word1 for word2.
2. calculate all distances of all indexes
3. return the smallest
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst_word1, lst_word2, dis = [], [], []
        for i in range(len(words)):
            if words[i] == word1:
                lst_word1.append(i)
            if words[i] == word2:
                lst_word2.append(i)
        for i in lst_word1:
            for j in lst_word2:
                dis.append(abs(i-j))
        return min(dis)

s = Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "practice","coding"))
