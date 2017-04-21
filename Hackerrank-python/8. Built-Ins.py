# Zipped!
# stu_cnt, sub_cnt = map(int, input().split())
# sub_marks = []
# for i in range(sub_cnt):
#     sub_marks.append(list(map(float, input().split())))
# stu_marks = zip(*sub_marks)
# for i in stu_marks:
#     print(sum(i)/sub_cnt)

# Python Evaluation
# eval(input())

# Sort Data
# N, M = map(int, input().split())
# nums = []
# for i in range(N):
#     nums.append(list(map(int, input().split())))
# K = int(input())
#
# for i in sorted(nums, key= lambda x: x[K]):
#     print(*i)

# Any or All
# n, nums = str(int(input())), list(map(int, input().split()))
# print(all([n>0 for n in nums]) and any([str(n)==str(n)[::-1] for n in nums]))

# ginortS
# import string
# print(*sorted(input(), key=(string.ascii_letters+'1357902468').index), sep='')
