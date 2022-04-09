# Задание 1

# with open(r'test\Lesson5HW.txt', 'w', encoding='utf-8') as f:
#     name = input('Enter your name: ')
#     age = input("Enter your age: ")
#     f.write(f'name: {name}\nage: {age}\n')

# Задание 2

# with open(r'test\Lesson5HW2.txt', 'r', encoding='utf-8') as f:
#     lines = 0
#     for i in f:
#         lines += 1
#         flag = 0
#         word = 0
#         for el in i:
#             if el != ' ' and flag == 0:
#                 word += 1
#                 flag = 1
#             elif el == ' ':
#                 flag = 0
#         print(i, word, 'words')
#     print('total strings: ', lines)

# Задание 3

# with open(r'test\Lesson5HW3.txt', 'r', encoding='utf-8') as f:
#     sal = []
#     poor = []
#     li = f.read().split('\n')
#     for i in li:
#         i = i.split()
#         if int(i[1]) < 20000:
#             poor.append(i[0])
#         sal.append(i[1])
# print(f'Salary less than 20 000: {poor}')
# print(f'Average salary: {sum(map(int, sal)) / len(sal)}')

# Задание 4

# di_rus = {'One' : 'Раз', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new = []
# with open(r'test\Lesson5HW4.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         i = i.split(' ', 1)
#         new.append(di_rus[i[0]] + '  ' + i[1])
#     print(i)
# with open('test\Lesson5HW4_1.txt', 'w', encoding='utf-8') as f2:
#     f2.writelines(new)

# Задание 5

# with open('test\Lesson5HW5.txt', 'w+', encoding='utf-8') as f:
#     line = input('Введите цифры через пробел: \n')
#     f.writelines(line)
#     my_numb = line.split()
#     print(sum(map(int, my_numb)))




