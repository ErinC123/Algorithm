#   Question: 13. Roman to Integer
# Difficulty: Easy
#       Tags: String, Math
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_hash = {}
        roman_hash['I'] = 1
        roman_hash['IV'] = 4
        roman_hash['V'] = 5
        roman_hash['IX'] = 9
        roman_hash['X'] = 10
        roman_hash['XL'] = 40
        roman_hash['L'] = 50
        roman_hash['XC'] = 90
        roman_hash['C'] = 100
        roman_hash['CD'] = 400
        roman_hash['D'] = 500
        roman_hash['CM'] = 900
        roman_hash['M'] = 1000
        num = 0
        length = len(s)
        i = 0
        while i < length:
            if i+1 < length and s[i]+s[i+1] in roman_hash:
                num += roman_hash[s[i]+s[i+1]]
                i = i+1
            else:
                num += roman_hash[s[i]]
            i = i+1
        return num