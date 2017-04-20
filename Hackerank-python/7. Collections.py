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

# 


