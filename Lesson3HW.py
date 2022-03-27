# Задание 1

# def delit(a, b):
#     try:
#         res = a / b
#     except ZeroDivisionError:
#         return 'cannot divide by zero'
#     return res
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# f = delit(a, b)
# print(round(f, 2))


# Задание 2

# def info(name, second_name, birth_year, city, e_mail, tel_number):
#     print(f'{name}, {second_name}, {birth_year}, {city}, {e_mail}, {tel_number}')
# name = input('Введите имя: ')
# second_name = input('Введите фамилию: ')
# birth_year = input('Введите год рождения: ')
# city = input('Введите город: ')
# e_mail = input('Введите мыло: ')
# tel_number = input('Введите тел номер: ')
# info(name, second_name, birth_year, city, e_mail, tel_number)

# Задание 3

# def my_func(num1 , num2, num3):
#     if num1 >= num3 and num2 >= num3:
#         return num1 + num2
#     elif num1 > num2 and num1 < num3:
#         return num1 + num3
#     else:
#         return num2 + num3
# num1 = int(input("enter first number "))
# num2 = int(input("enter second number "))
# num3 = int(input("enter third number "))
# result = my_func(num1 , num2, num3)
# print('Total -', (result))

# Задание 4
# def my_func(x, y):
#     res = x ** abs(y)
#     if y >= 0:
#         return res
#     else:
#         return 1 / res
# x = int(input('enter number1: '))
# y = int(input('enter number2: '))
# f = my_func(x, y)
# print(f)

# Задание 5

# def my_print():
#     sum_res = 0
#     while True:
#         number = input('Enter numbers: ').split()
#         res = 0
#         for el in range(len(number)):
#             if el == 9:
#                 return
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print('Current sum is: ', sum_res)
#     print('Final sum is: ', sum_res)
# my_print()


# Задание 6; 7

# def int_func():
#     word = input('Enter words: ')
#     print(word.title())
# int_func()
