# Arrays - DS

# import sys
#
#
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# print(*arr[::-1])

# 2D Array - DS

import sys
# def sum_hourglass(arr, i, j):
#     return arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
#            arr[i + 2][j + 2]
#
#
# arr = []
# for arr_i in range(6):
#     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     arr.append(arr_t)
#
# max_sum = sum_hourglass(arr, 0, 0)
# for i in range(len(arr) - 2):
#     for j in range(len(arr[i]) - 2):
#         max_sum = max(max_sum, sum_hourglass(arr, i, j))
#
# print(max_sum)

# Left Rotation
# n, d = map(int, input().split())
# nums = list(map(int, input().split()))
# print(*(nums[d:]+nums[:d]))

# Sparse Arrays
# from collections import Counter
#
# num_cnt, nums = int(input()), []
# for i in range(num_cnt):
#     nums.append(input())
#
# nums_hs = Counter(nums)
# find_cnt = int(input())
# for i in range(find_cnt):
#     k = input()
#     if k in nums_hs:
#         print(nums_hs[k])
#     else:
#         print(0)

# Algorithmic Crush
# nums_cnt, ops_cnt = map(int, input().split())
# nums = [0 for i in range(nums_cnt)]
#
# for i in range(ops_cnt):
#     start, end, n = map(int, input().split())
#     nums[start-1] += n
#     if end < nums_cnt:
#         nums[end] -= n
#     else:
#         nums.append(-n)
#
# for i in range(1, len(nums)-1):
#     nums[i] = nums[i]+nums[i-1]
#
# print(max(nums))