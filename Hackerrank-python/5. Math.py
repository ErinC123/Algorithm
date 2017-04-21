# Polar Coordinates
# 线性函数， 角度
# import cmath
# i = input()
# print(abs(complex(i)))
# print(cmath.phase(complex(i)))

# Triangle Quest 2
# 这里之所以过不了是因为 print虽然看起来只有一个，但执行起来其实是好几个，sep是空所以看起来是一行。....这个假设有待考证
# 这里也很巧妙的用了1， 11，111， 1111。。的平方结果。
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(*[j for j in range(1, i+1)]+[k for k in range(i-1, 0, -1)], sep="")
# for i in range(1, 9):
#     print((((10 ** 3) - 1) // 9)**2)

# Mod Divmod
# a, b = int(input()), int(input())
# print(*[int(a/b), a%b, divmod(a, b)], sep= "\n")

# Integers Come In All Sizes
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(a**b+c**d)

# Triangle Quest
# 没想到得到1， 11，111的办法，转化成得到9 99 999。。先，再除以9就是了
# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(i*(10**i-1)//9)

