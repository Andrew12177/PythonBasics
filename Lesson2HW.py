# Задание 1
# sex = 'male'
# li = [12, '368', False, [1, 2, 3, 4, 5], sex, 396.654]
# for el in li:
#     print(type(el))

# Задание 2
# user_input = input('Введите числа через пробел: ')
# li = user_input.split()
# li[0], li[1] = li[1], li[0]
# li[2], li[3] = li[3], li[2]
# print(li)

# Задание 3
# seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autum': [9,10, 11]}  # нужно перейти от 10 бальной системы оценки к 5 бальной
# num = int(input('Введите число: '))
# for el in seasons:
#     if num in seasons[el]:
#         print(el)

# Задание 4
# user_input = input('Введите слова через пробел: ')
# li = user_input.split()
# for i, el in enumerate(li, 1):
#      if len(el) <= 10:
#        print(i, el)
#      else:
#          print(i, el [0:10])

# Задание 5
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# num = int(input('Введите число: '))
# for el in range(len(my_list)):
#     if my_list[el] == num:
#         my_list.insert(el + 1, num)
#     elif my_list[0] < num:
#         my_list.insert(0, num)
#     elif my_list[-1] > num:
#         my_list.append(num)
#     elif my_list[el] > num and my_list[el + 1] < num:
#         my_list.insert(el + 1, num)
# print(f'Рейтинг - {my_list}')

