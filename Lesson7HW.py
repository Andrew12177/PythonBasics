# Задание 1

# class Matrix:
#     def __init__(self, li1, li2):
#         self.li1 = li1
#         self.li2 = li2
#     def __add__(self):
#         matr = [[0, 0],
#                 [0, 0],
#                 [0, 0]]
#         for i in range(len(self.li1)):
#             for j in range(len(self.li2[i])):
#                 matr[i][j] = self.li1[i][j] + self.li2[i][j]
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
# my_m = Matrix([[5, 18],
#                [6, 17],
#                [41, 50]],
#               [[45, 8],
#                [6, 7],
#                [24, 5]])
#
# print(my_m.__add__())

# Задание 2
# from abc import ABC, abstractmethod
# class Clothes(ABC):
#     @abstractmethod
#     def c_volume(self):
#         pass
# class Coat(Clothes):
#     def __init__(self, size):
#         self.size = size
#     @property
#     def c_volume(self):
#         res = self.size/6.5 + 0.5
#         return f'На пошив пальто понадобится {round(float(res), 2)} метра ткани'
# class Suit(Clothes):
#     def __init__(self, heit):
#         self.heit = heit
#     @property
#     def c_volume(self):
#         res = 2*self.heit + 0.3
#         return f'На пошив костюма понадобится {round(float(res), 2)} метра ткани'
# coat1 = Coat(56)
# print(coat1.c_volume)
# suit1 = Suit(1.8)
# print(suit1.c_volume)

# Задание 3

# class Cell:
#     def __init__(self, cell_slots):
#         self.cs = int(cell_slots)
#     def __str__(self):
#         return f' Result: {int(self.cs)}'
#     def __add__(self, other):
#         return Cell(self.cs + other.cs)
#     def __sub__(self, other):
#         res = self.cs - other.cs
#         if res > 0:
#             return Cell(res)
#         else:
#             print('Такого не может быть!')
#     def __mul__(self, other):
#         return Cell(self.cs * other.cs)
#     def __truediv__(self, other):
#         return Cell(round(self.cs / other.cs))
#     def make_order(self, slots_in_row):
#         row = ''
#         for i in range(int(self.cs / slots_in_row)):
#             row += f'{"*" * slots_in_row} \n'
#         row += f'{"*" * (self.cs % slots_in_row)}'
#         return row
#
# c1 = Cell(25)
# c2 = Cell(12)
# print(c1 + c2)
# print(c2 - c1)
# print(c1 * c2)
# print(c1 / c2)
# print(c1.make_order(6))
# print(c2.make_order(3))










