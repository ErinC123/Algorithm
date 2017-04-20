#   Question: 288. Unique Word Abbreviation
# Difficulty: Easy
#       Tags: Hash Table, Design
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for i in dictionary:
            if len(i) > 2:
                s = i[0] + str(len(i) - 2) + i[-1]
                if s in self.dic:
                    self.dic[s].append(i)
                else:
                    self.dic[s] = [i]
            else:
                self.dic[i] = [i]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        word_ab = word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word
        return word_ab not in self.dic or (len(self.dic[word_ab]) == 1 and self.dic[word_ab][0] == word)