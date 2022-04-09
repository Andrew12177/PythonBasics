# Задание 1

# from time import sleep
#
# class TraficLight:
#
#     __color = ['Red', 'Yellow', 'Green']
#
#     def run(self):
#         i = 0
#         while i < 3:
#             print(f'TraficLight turns: {TraficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(12)
#             i += 1
#
# Light = TraficLight()
# Light.run()

# Задание 2
#1
# class Road:
#
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#
# street = Road(5000, 10)
# sqm_mass = int(input('Enter square meter mass kg: '))
# r_thick = int(input('Enter road thickness cm: '))
# print(f'Asphalt mass: {street._l * street._w * sqm_mass * r_thick / 1000} tonns')

#2
# class Road:
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#     def calc(self):
#         sqm_mass = int(input('Enter square meter mass kg: '))
#         r_thick = int(input('Enter road thickness cm: '))
#         res = self._l * self._w * sqm_mass * r_thick / 1000
#         return f'Asphalt mass: {res} tonns'
#
# street = Road(5000, 10)
# print(street.calc())


# Задание 3

# class Worker:
#     def __init__(self, name, surname, position):
#         self.n = name
#         self.sur = surname
#         self.pos = position
# class Position(Worker):
#     def calc(self):
#         _income = {'wage': 2500, 'bonus': 1500}
#         _income['wage'] = int(input('Enter empoyee''s wage: '))
#         _income['bonus'] = int(input('Enter employee''s bonus: '))
#         get_full_name = self.n + ' ' + self.sur
#         get_total_income = _income.get('wage') + _income.get('bonus')
#         return f'{get_full_name}:  {get_total_income} -'
# emp1 = Position('Nick', 'Brown', 'DevOps')
# print(emp1.calc(), emp1.pos)

# Задание 4

# class Car:
#     def __init__(self, color, name):
#         self.c = color
#         self.n = name
#         self.speed = int(input('Enter speed: '))
#     def go(self):
#         return f'Автомобиль: {self.c} {self.n} поехал'
#     def stop(self):
#         return f'Автомобиль: {self.c} {self.n} остановился'
#     def turn(self):
#         direction = 'right'
#         return f'Автомобиль: {self.c} {self.n} повернул {direction}'
#     def show_speed(self):
#         return f'The speed of the car is: {self.speed}'
# class Towncar(Car):
#     def speeding(self):
#         if self.speed > 60:
#             return f'You are speeding, slow down!!!'
#         else:
#             return f'The speed of the car is: {self.speed}'
# class SportCar(Car):
#     def drifting(self):
#         return f'{self.c} {self.n} is drifting'
# class WorkCar(Car):
#     def speeding(self):
#         if self.speed > 40:
#             return f'You are speeding, slow down!!!'
#         else:
#             return f'The speed of the car is: {self.speed}'
# car1 = Towncar('black', 'Lincoln')
# print(car1.go())
# print(car1.stop())
# print(car1.turn())
# print(car1.speeding())
#
# car2 = SportCar('Red', 'Ferrari')
# print(car2.go())
# print(car2.stop())
# print(car2.turn())
# print(car2.show_speed())
# print(car2.drifting())
#
# car3 = WorkCar('Yellow', 'Taxi')
# print(car3.go())
# print(car3.stop())
# print(car3.turn())
# print(car3.speeding())

# Задание 5

# class Stationery:
#     def __init__(self, title):
#         self.t = title
#     def draw(self):
#         return f'Запуск отрисовки'
# class Pen(Stationery):
#     def draw(self):
#         return f'{self.t} рисует линию'
# class Pencil(Stationery):
#     def draw(self):
#         return f'{self.t} сломался'
# class Handle(Stationery):
#     def draw(self):
#         return f'{self.t} потек'
# Piece1 = Pen('Ручка')
# print(Piece1.draw())
# Piece2 = Pencil('Карандаш')
# print(Piece2.draw())
# Piece3 = Handle('Маркер')
# print(Piece3.draw())




