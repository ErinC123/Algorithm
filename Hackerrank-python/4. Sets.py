# Introduction to Set
# def average(array):
#     # your code goes here
#     return float(sum(list(set(array)))/len(list(set(array))))

# Symmetric Difference
# union; difference; intersection; *解list； sep；
# m, ml = input(), set(list(map(int, input().split())))
# n, nl = input(), set(list(map(int, input().split())))
# diff = sorted(list((ml.union(nl)).difference(ml.intersection(nl))))
# print(*diff, sep="\n")

# No Idea!
# test case 数据很多， 前两种方式都超时。
# n, m = input().split()
# arr = list(map(int, input().split()))
# A, B = set(list(map(int, input().split()))), set(list(map(int, input().split())))
# #print(sum([1 for n in A if n in arr])-sum([1 for n in B if n in arr]))
# #print(len(A.intersection(arr)) - len(B.intersection(arr)))
# print(sum([1 if x in A else -1 if x in B else 0 for x in arr]))

# Set.add()
# set add 可以自动判断，如果新的element是不同的才加进来不然就不加
# n = int(input())
# s = set()
# for i in range(n):
#     s.add(input())
# print(len(s))

# Set .discard(), .remove() & .pop()
# 不能写【1】这样会访问不到，写1：的话，如果从1开始没有元素，这个arg就为null
# n = int(input())
# s = set(map(int, input().split()))
# num_ops = int(input())
# for i in range(num_ops):
#     string = input().split()
#     cmd = string[0]
#     arg = string[1:]
#     cmd = cmd + "("+''.join(arg)+")"
#     eval("s."+cmd)
# print(sum(s))

# Set .union() Operation
# union
# e_num, e_list = int(input()), set(list(map(int, input().split())))
# f_num, f_list = int(input()), set(list(map(int, input().split())))
# print(len(e_list.union(f_list)))

# Set .intersection() Operation
# intersection
# e_num, e_list = int(input()), set(list(map(int, input().split())))
# f_num, f_list = int(input()), set(list(map(int, input().split())))
# print(len(e_list.intersection(f_list)))

# Set .difference() Operation
# difference
# e_num, e_list = int(input()), set(list(map(int, input().split())))
# f_num, f_list = int(input()), set(list(map(int, input().split())))
# print(len(e_list.difference(f_list)))

# Set .symmetric_difference() Operation
# symmetric_difference == union.difference(intersection)
# e_num, e_list = int(input()), set(list(map(int, input().split())))
# f_num, f_list = int(input()), set(list(map(int, input().split())))
# print(len(e_list.symmetric_difference(f_list)))

# Set Mutation
# num_A, A = input(), set(list(map(int, input().split())))
# num_ops = int(input())
# for i in range(num_ops):
#     oper = input().split()
#     other_set = set(list(map(int, input().split())))
#     cmd = oper[0]
#     eval("A."+cmd+"(other_set)")
# print(sum(A))

# The Captain's Room
# group个数 * set(rooms)(所有房间的号码）-> 假设captial的房间有k个人住，然后减去实际的情况就得到（k-1）* captial的房间号
# num_g, rooms = int(input()), list(map(int, input().split()))
# print(int((sum(list(set(rooms)))*num_g - sum(rooms))/(num_g-1)))

# Check Subset
# for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
#     a = int(input()); A = set(input().split())
#     b = int(input()); B = set(input().split())
#     print(B.intersection(A) == A)

# Check Strict Superset
# A, num_set = set(list(map(int, input().split()))), int(input())
# ret = True
# for i in range(num_set):
#     s = set(list(map(int, input().split())))
#     if (s.union(A) == A and len(s)<len(A)) == False:
#         ret = False
#         break
# print(ret)