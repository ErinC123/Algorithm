class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if len(abbr) > len(word):
            return False
        i = 0
        index = 0
        while i < len(abbr) and index < len(word):
            if abbr[i].isdigit():
                m = 1
                while i + m < len(abbr) and abbr[i:i + m].isdigit():
                    m += 1

                if m > 1:
                    index = index + int(abbr[i:i + m - 1])
                    i = i + len(str(abbr[i:i + m - 1]))
                else:
                    index = index + int(abbr[i])
                    i = i + len(str(abbr[i]))
            else:
                if word[index] != abbr[i]:
                    return False
                i = i + 1
                index = index + 1
        return True

s = Solution()
print(s.validWordAbbreviation("apple", "5"))