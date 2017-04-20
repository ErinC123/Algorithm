class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 != word2:
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
        if word1 == word2:
            lst_word1, dis = [], []
            for i in range(len(words)):
                if words[i] == word1:
                    lst_word1.append(i)
            for i in range(1, len(lst_word1)):
                dis.append(abs(lst_word1[i] - lst_word1[i-1]))
            return min(dis)