# Lists
# split, eval, join
# if __name__ == '__main__':
#     N = int(input())
#     l = []
#     for i in range(N):
#         s = input().split()
#         cmd = s[0]
#         args = s[1:]
#         if cmd != "print":
#             cmd += "("+ ",".join(args) +")"
#             eval("l."+cmd)
#         else:
#             print(l)

# Tuples
# The difference between tuples and lists: list is mutable, tuple is immutable
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print(hash(tuple(integer_list)))

# List Comprehensions
# 并列for循环； range的上限是exclude的
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     # i < x; j < y; k < z; i+j+k != n
#     print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

# Nested List
# list comprehension; set; join; nested list 里面可以设置临时变量代表第几个
# if __name__ == '__main__':
#     students = [[input(), float(input())] for _ in range(int(input()))]
#     sec_lowest = sorted(list(set(g for [_, g] in students)))[1]
#     print('\n'.join(sorted([n for [n, g] in students if g == sec_lowest])))

# Finding the Percentage
# 得到小数后2位： 1. 用float 能保留小数位，用／／就截掉了 2.round 是四舍五入2位 3. 然后为了能只显示两位，用了%.2f
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     avg = float(sum(student_marks[query_name])/len(student_marks[query_name]))
#     print("%.2f" % round(avg, 2))
