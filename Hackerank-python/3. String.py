# sWAP cASE
# def swap_case(s):
#     return s.swapcase()

# String Split and Join
# def split_and_join(line):
#     # write your code here
#     return "-".join(line.split(" "))

# What's Your Name?
# def print_full_name(a, b):
#     print("Hello {0} {1}! You just delved into python.".format(a, b))

# Mutation
# string is immutable
# def mutate_string(string, position, character):
#     s = list(string)
#     s[position] = character
#     string = ''.join(s)
#     return string

# Find a string
# 不用新变量存，sum(1 for ...) 结构
# def count_substring(string, sub_string):
#     return sum([1 for i in range(len(string)) if string[i: i+len(sub_string)] == sub_string])

# String Validators
# any
# if __name__ == '__main__':
#     s = input()
#     print(any(c.isalnum() for c in s))
#     print(any(c.isalpha() for c in s))
#     print(any(c.isdigit() for c in s))
#     print(any(c.islower() for c in s))
#     print(any(c.isupper() for c in s))

# Text Alignment
# ljust/rjust/center(width, symbol)
# #Replace all ______ with rjust, ljust or center.
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Designer Door Mat
# symbol * 个数 这个蛮方便的
# N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
# for i in range(1,N,2):
#     print(('.|.'*i).center(M,'-'))
# print('WELCOME'.center(M,'-'))
# for i in range(N-2,-1,-2):
#     print(('.|.'*i).center(M,'-'))

# String Formatting
# oct(); hex(); bin()
# def print_formatted(number):
#     # your code goes here
#     w = len(str(bin(number)[2:]))
#     ret = ""
#     for i in range(1, number+1):
#         ret += ('{0} {1} {2} {3}\n'.format(str(i).rjust(w, ' '),
#                                            str(oct(i)[2:]).rjust(w, ' '),
#                                            str(hex(i)[2:]).upper().rjust(w, ' '),
#                                            str(bin(i)[2:]).rjust(w, ' ')
#                                            ))
#     print(ret)

# Alphabet Rangoli
# 凑index
# def print_rangoli(size):
#     # your code goes here
#     for j in range(size-2, -2, -1):
#         line = [chr(97+i) for i in range(size-1, j, -1)] + [chr(97+i) for i in range(j+2, size, 1)]
#         print('-'.join(line).center((size*4-3), '-'))
#     for j in range(0, size-1):
#         line = [chr(97+i) for i in range(size-1, j, -1)] + [chr(97+i) for i in range(j+2, size, 1)]
#         print('-'.join(line).center((size*4-3), '-'))

# Capitalize
# replace
# def capitalize(s):
#     for x in s.split():
#         s = s.replace(x, x.capitalize())
#     return s

# The Minion Game
# def minion_game(string):
#     # your code goes here
#     vowels = "AEIOU"
#     kevin = stuart = 0
#
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin = kevin + len(string) - i
#         else:
#             stuart = stuart + len(string) - i
#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif stuart > kevin:
#         print("Stuart", stuart)
#     else:
#         print("Draw")

# Merge the Tools
# 把每一个3字母元素当成字典，如果字典出现过了就不往字典加，如果没出现，加到字典里面
# import textwrap
# def merge_the_tools(string, k):
#     # your code goes here
#     for i in textwrap.wrap(string, k):
#         d = dict()
#         print(''.join([d.setdefault(c,c) for c in i if c not in d]))