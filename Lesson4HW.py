# Задание 1
'''
ar1 - 160
ar2 - 48
ar3 - 590
'''
# from sys import argv
# ar1, ar2, ar3, = map(int, argv[1:])
# print('Hours worked: ', ar1)
# print('$ per hour: ', ar2)
# print('Bonus: ', ar3)
# def wages():
#     res = ar1*ar2+ar3
#     return res
# f = wages()
# print('Your pay is: ', f)

# Задание 2

# li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new = [li[i] for i in range(len(li)) if li[i] > li[i - 1]]
# print(new)

# Задание 3

# li = [i for i in range(20, 240) if i %20 == 0]
# new = [i for i in range(20, 240) if i %21 == 0]
# print(li)
# print(new)

# Задание 4

# li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new = [el for el in li if li.count(el) == 1]
# print(new)

# Задание 5
'''
Сделал 2-мя способами через math и через functools
похоже, что рез-т одинаковый ))
'''
# import math
# from functools import reduce
# li = [i for i in range(100, 1001) if i %2 == 0]
# print('Multiplication result: ', math.prod(li))
# def multiply(a, b):
#     return a * b
# result = reduce(multiply, li)
# print(result)


# Задание 6

from itertools import count, cycle

# for el in count(5, 7):
#     if el > 300:
#         break
#     print(el)

# li = [i for i in range(2, 100) if i %2 != 0]
# i = 0
# for el in cycle(li):
#     print(el)
#     i += 1
#     if i == 59:
#         break

# Задание 7

# import math
# def gen():
#     for el in (i for i in range(3, 159) if i %2 == 0):
#         yield el
# for el in gen():
#     if el > 33:
#         break
#     print(math.factorial(el))



