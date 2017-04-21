# itertools.product()
# list(product([1,2,3],[3,4])): [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
# from itertools import product
# A, B = list(map(int, input().split())), list(map(int, input().split()))
# print(*list(product(A, B)))

# itertools.permutations()
# list(permutations(['1','2','3'],2)): [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# from itertools import permutations
# S, k = input().split()
# l = []
# for i in list(permutations(S, int(k))):
#     l.append(''.join(i))
# print('\n'.join(sorted(l)))

# itertools.combinations()
# A = [1,1,3,3,3] -- list(combinations(A,4)) : [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
# from itertools import combinations
# S, k = input().split()
# res = []
# for i in range(1, int(k)+1):
#     for e in list(combinations(sorted(S), i)):  # for every tuple
#         res.append(''.join(e))
# print('\n'.join(res))

# itertools.combinations_with_replacement()
# from itertools import combinations_with_replacement
#  A = [1,1,3,3,3] -- list(combinations(A,2)) : [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
# S, k = input().split()
# for e in list(combinations_with_replacement(sorted(S), int(k))):
#     print(''.join(e))

# Compress the String!
# groupby
# from itertools import groupby
# a = input()
# res = []
# for key, group in groupby(a):
#     res.append(tuple([len(list(group)), int(key)]))
# print(*res)

# Iterables and Iterators
# 
# from itertools import combinations
# N, letters, K = int(input()), list(input().split()), int(input())
# # l_in = [i for i in range(1, len(letters)+1)]
# l = list(combinations(letters, K))
# cnt = 0
# for e in l:
#     if 'a' in e:
#         cnt += 1
# print(cnt/len(l))


