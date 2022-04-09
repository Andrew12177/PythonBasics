# Задание 1

# class Date:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extr_date(cls, day_month_year):
#         my_date = []
#         for i in day_month_year.split():
#             if i != '-':
#                 my_date.append(i)
#         return f'Today the date is: {int(my_date[0])}:{int(my_date[1])}:{int(my_date[2])}'
#     @staticmethod
#     def valid(day, month, year):
#         if 0 < day <= 31:
#             if 0 < month <= 12:
#                 if 0 < year <= 2022:
#                     return f'{day}:{month}:{year}'
#                 else:
#                     print('Не корректный год ')
#             else:
#                 print('Не корректный месяц')
#         else:
#             print('Не корректный день')
#
# print(Date.extr_date('25 - 12 - 2000'))
# print(Date.valid(12, 0o3, 2022))
# print(Date.valid(32, 5, 2000))
# print(Date.valid(31, 13, 2000))

# Задание 2

# class Divide(Exception):
#     # def __init__(self, txt):
#     #     self.txt = txt
#     pass
#
#
# a = (input('Enter first number: '))
# b = (input('Enter second number: '))
# try:
#     c = int(a) / int(b)
#     if b == 0:
#         raise Divide #('Cannot divide by zero')
# except ValueError:
#     print('It must be integer')
# except ZeroDivisionError:
#     print('oops')
# except Divide: #as err:
#     print('Cannot divide by zero')
# else:
#     print(c)

# Задание 3

# class Mistake:
#     def __init__(self, *args):
#         self.li = []
#
#     def mylist(self):
#         while True:
#             try:
#                 n = int(input('Enter a number: '))
#                 self.li.append(n)
#                 print(f'Your list is: {self.li}')
#             except:
#                 print('Incorrect input')
#                 c = input('Continue? Yes to continue, stop to quit: ')
#                 if c == 'Yes' or c == 'yes':
#                     print(user_list.mylist())
#                 elif c == 'stop':
#                     return f'Game over: {user_list.li}'

# user_list = Mistake(1)
# print(user_list.mylist())

# Задание 4













