# collections.Counter()
# items(), keys(), values()
# from collections import Counter
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# print Counter(myList).values()
# [3, 4, 4, 2, 1]

# from collections import Counter
# income = 0
# shoe_cnt, shoes, cust_cnt = input(), Counter(list(map(int, input().split()))), int(input())
#
# for cust_i in range(cust_cnt):
#     shoe, price = map(int, input().split())
#     if shoe in shoes:
#         income += price
#         shoes[shoe] -= 1
#         if shoes[shoe] == 0:
#             del shoes[shoe]
#
# print(income)

# DefaultDict Tutorial
# DefaultDict:
# from collections import defaultdict
#
# m, n = map(int, input().split())
# A = defaultdict(list)
# for i in range(m):
#     A[input()].append(i+1)
# for i in range(n):
#     k = input()
#     if A[k]:
#         print(*A[k])
#     else:
#         print(-1)

# Collections.namedtuple()
# from collections import namedtuple
# cnt, Stud = int(input()), namedtuple('Stud', input().split())
# print(sum([float(s.MARKS) for s in [Stud(*input().split()) for n in range(cnt)]])/cnt)

# Collections.OrderedDict()
# OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# import re
# from collections import OrderedDict
#
# cnt = int(input())
# item_list = OrderedDict()
# for i in range(cnt):
#     fetch = re.search(r'(([A-Z]+\s)+)([0-9]+)', input())
#     item_name = fetch.group(1)
#     net_price = fetch.group(3)
#     item_list[item_name] = item_list.get(item_name, 0) + int(net_price)
# for k, v in item_list.items():
#     print("{0}{1}".format(k, v))

# Word Order
# from collections import OrderedDict
#
# cnt = int(input())
# word_hs = OrderedDict()
#
# for i in range(cnt):
#     k = input()
#     word_hs[k] = word_hs.get(k, 0) + 1
# print(len(word_hs.keys()))
# print(*word_hs.values())

# Collections.deque()
# Double ended queue, support add/remove items from both ends
# append(value); appendleft(value);
# clear();
# extend(value); extendleft(value),
# count(value);
# pop(); popleft()
# remove(value)
# reverse()
# rotate(index)
# from collections import deque
#
# d = deque()
# ops_cnt = int(input())
#
# for i in range(ops_cnt):
#     cmd = input().split()
#     if len(cmd) == 1:
#         cmd = "d."+cmd[0]+"()"
#     else:
#         cmd = "d."+cmd[0]+"("+cmd[1]+")"
#     eval(cmd)
# print(*d)

# Piling Up!
# from collections import deque
#
# d = deque()
# time_cnt = int(input())
#
# for i in range(time_cnt):
#     cube_cnt, cubes = int(input()), deque(map(int, input().split()))
#     top = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()
#
#     while len(cubes) > 0:
#         if cubes[0] >= cubes[-1] and cubes[0] <= top:
#             top = cubes.popleft()
#         elif cubes[-1] > cubes[0] and cubes[-1] <= top:
#             top = cubes.pop()
#         else:
#             break
#     if len(cubes) == 0:
#         print("Yes")
#     else:
#         print("No")

# Most Common
# OrderedCounter 
# from collections import Counter, OrderedDict
# class OrderdCounter(Counter, OrderedDict):
#     pass
#
# [print(*c) for c in OrderdCounter(sorted(input())).most_common(3)]