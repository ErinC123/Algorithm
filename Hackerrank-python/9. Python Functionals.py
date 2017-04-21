# Map and Lambda Function
# def fibonacci(n):
#     # return a list of fibonacci numbers
#     res = []
#     for i in range(n):
#         if i == 0:
#             res.append(0)
#         elif i == 1:
#             res.append(1)
#         else:
#             res.append(res[-1]+res[-2])
#     return res

# Validating Email Addresses With a Filter
# import re
# result = []
# address = re.compile(r'^[a-zA-z][\w-]*@[a-zA-Z0-9]+\.\w{1,3}\Z$')
# for i in range(int(input())):
#     email = input()
#     if re.search(address, email):
#         result.append(email)
#
# print(sorted(result))