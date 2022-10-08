# s = 'Привет Даниил!'
#  print(s[::-1])
#  print(s[2])
#  print(s[-2])
#  print(s[:5])
#  print(s[:-3])
#  print(s[::2])
#  print(s[1::2])
#  print(s[::-1])
# print(s[::-2])
# print(len(s))
#  print(s.find('о'))
#  print(s.rfind('и'))
#  print(s.find('а',7,10))
#  print(s.count('и'))
#
# result = s[7:13] + s[6] + s[:-7]
#  print(result)
#
# q = s.find(' ')
# result = s[q+1:-1] + s[q] + s[:q]
# print(result)
# ----------------
# g = '@ghasz@1hdsah@1hs@@!'
# print(g.replace('@',''))

# s = 'He has long hair'
# print(s.rfind('h'))
# s = s[:s.find('h')] + s[s.rfind('h') +1 :]
# print(s)
# v = 'how1 how2 how3 how4'
# v = v.replace('how2', 'How2')
# v = v.replace('how3', 'How3')
# print(v)


# print('Привет меня зовут Данил'.count(' ') +1)

# a = int(input('Введи число'))
# if a > 10:
#     print('Ваше число больше 10')
# elif a > 0:
#     print('Ваше число больше 0,но меньше 10')
# elif a == 0:
#     print('Ваше число равно нулю')
# else:
#     print('Ваше число не больше 0')

# num3 = input('Введи арифметическую операцию\n')
# if num3.find('+')>0:
#     operator = '+'
#     num1 = int(num3[:num3.find('+')])
#     num2 = int(num3[num3.find('+') +1:])
# elif num3.find('-')>0:
#     operator = '-'
#     num1 = int(num3[:num3.find('-')])
#     num2 = int(num3[num3.find('-') +1:])
# elif num3.find('*')>0:
#     operator = '*'
#     num1 = int(num3[:num3.find('*')])
#     num2 = int(num3[num3.find('*') + 1:])
# elif num3.find('/')>0:
#     operator = '/'
#     num1 = int(num3[:num3.find('/')])
#     num2 = int(num3[num3.find('/') +1:])
# else:
#     operator = ''
#
#  num1 = float(input('Введите первое число:'))
#  operator = '+'
#  num2 = float(input('Введите второе число:'))
#
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '/':
#     print(num1 / num2)
# elif operator == '*':
#     print(num1 * num2)
# else:
#     print('Ошибка')




# num1 = int(input('Введите число, оно переведётся в собачие года\n'))
# if 0<= num1 <= 2:
#    print(num1 * 10.5)
# else:
#    print(21+(num1-2)*4)


# month = input('Введи название любого месяца С МАЛЕНЬКОЙ БУКВЫ\n')
# if month == 'январь':
#   print('В январе 31 день')
# elif month == 'февраль':
#     print('В феврале 28 или 29 дней')
# elif month == 'март':
#     print('В марте 31 день')
# elif month == 'апрель':
#     print('В апреле 30 дней')
# elif month == 'май':
#     print('В мае 31 день')
# elif month == 'июнь':
#     print('В июне 30 дней')
# elif month == 'июль':
#     print('В июле 31 день')
# elif month == 'август':
#     print('В августе 31 день')
# elif month == 'сентябрь':
#     print('В сентябре 30 дней')
# elif month == 'октябрь':
#     print('В октябре 31 день')
# elif month == 'ноябрь':
#     print('В ноябре 30 дней')
# elif month == 'декабрь':
#     print('В декабре 31 день')
# else:
#     print('Такого месяца не существует')

# a = int(input('Введи первую сторону треугольнкиа\n'))
# b = int(input('Введи вторую сторону треугольнкиа\n'))
# c = int(input('Введи третью сторону треугольнкиа\n'))
# if a == b == c:
#     print('Это равносторонний треугольник')
# elif (a == b) or (a == c) or (b == c):
#     print('Это равнобедренный треугольник')
# else:
#     print('Это разносторонний треугольник')


# h = int(input('Каков размер вашего бензобака в литрах?'))
# j = int(input('Сколько горючего в бензобаке? В процентах'))
# k = int(input('Сколько километров проходит автомобиль на одном литре бензина'))
# if j / 100 * h * k >= 200:
#    print('Водитель может ехать до следующей станции')
# else:
   #print('Нужно заправиться на этой станции')

# import random
# l = input('Привет! Как тебя зовут?\n')
# print('Мы загадали число от 1 до 100')
# o = 0
# n = random.randint(1, 100)
# while True:
#
#
#    v = int(input('Введи число от 1 до 100\n'))
#    o = o + 1
#    m = abs(n - v)
#    if m == 1:
#       print('Горячо')
#    elif 2 <= m <= 5:
#       print('Очень тепло')
#    elif 6 <= m <= 10:
#       print('Тепло')
#    elif 11 <= m <= 20:
#       print('Прохладно')
#    elif m > 20:
#       print('Холодно')
#    elif m == 0:
#       print(f'{l}, ты угадал за {o}  попыток')
#       break





# a = int(input('Введите первое число\n'))
# b = int(input('Введите второе число\n'))
# if a > b:
#    print(f'{b} меньшее число')
# elif a < b:
#    print(f'{a} меньшее число')



# name = input('Введите ваше имя\n')
# age = int(input('Введите ваш возраст\n'))
# if age >= 18:
#    print(f'Добрый вечер {name}! Вы совершеннолетний, поздравляем!')
# if age < 18:
#    print(f'Привет,{name}! Приносим извинения, но вы не можете гулять после 22:00')



# time = int(input('Введите целое время на часах\n'))
# # if 7 <= time <= 10:
# #    print('Пора вставать!')
# # elif 23 < time or time < 0:
# #    print('Ошибка')
# # else:
# #    print('Вы проспали!')


# season = input('Введите время года\n').lower()
# if season == 'лето':
#    print('Тополиный пух, жара, июль')
# elif season == 'зима':
#    print('Снеговик, снежки и горка')
# elif season == 'осень':
#    print('Пора в школу!')
# elif season == 'весна':
#    print('Весенняя капель')
# else:
#    print('Ошибка')



# month2 = int(input('Введите номер месяца своего рождения\n'))
# if 6 <= month2 <= 8:
#    print('Вы родились летом')
# elif 3 <= month2 <= 5:
#    print('Подснежник')
# elif 9 <= month2 <= 11:
#    print('Я тоже люблю осенний листопад')
# elif month2 > 12 or month2 <= 0:
#    print('Ошибка')
# else:
#    print('К холодам вам не привыкать')


# num = int(input('Введите целое число\n'))
# if num % 2 == 0:
#     if num > 0:
#        print('Положительное четное')
#     elif num < 0:
#        print('Отрицательное четное')
# elif num % 2 != 0:
#     if num < 0:
#        print('Отрицательное нечетное')
#     elif num > 0:
#        print('Положительное нечетное')
# else:
#     print('Нулевое число')



# num3 = int(input('Введите число от 1 до 999\n'))
# if 1 <= num3 <= 9:
#     print('Цифра')
# elif 10 <= num3 <= 99:
#     print('Двухзначное число')
# elif 100 <= num3 <= 999:
#     print('Трёхзначное число')
# elif num3 > 999 or num3 <= 0:
#     print('Ошибка')


# a = int(input('Введите первую сторону треугольника\n'))
# b = int(input('Введите вторую сторону треугольника\n'))
# c = int(input('Введите третью сторону треугольника\n'))
# if a + b < c or a + c < b or b + c < a:
#     print('Такого треугольника не существует')



# a = int(input('Введите первое число\n'))
# b = int(input('Введите второе число\n'))
# c = int(input('Введите третье число\n'))
# print(a + b + c)

# a = int(input('Введите целое число\n'))
# print(a -1, a, a +1)

# class Square:
#     corner = 90
#     def __init__(self, a):
#         self.a = a
#         print('Square Created!')
#
#     def get_area(self):
#         return self.a ** 2
#
#     def get_perimetr(self):
#         return self.a * 4
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_area(self):
#             return self.a * self.b
#
#     def get_perimetr(self):
#             return (self.a + self.b) * 2
#
# class Rhombus(Square):
#     corner = 45
#     def __init__(self, a):
#         Square.__init__(self, a)
#     def get_area(self):
#         # подсчёт площади неправильный
#         return self.corner * self.a
# romb = Rhombus(5)
# print(romb.get_area())
# square_1 = Square(2)
# print(romb.corner)
# square_2 = Square(5)
# print(square_1.get_area())
# print(square_2.get_area())
# print(square_1.get_perimetr())
# print(square_2.get_perimetr())

class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')

    def drive(self,city):
        print(f'{self.name.title()} is driving to {city.title()}!!!')

    def change_color(self,new_color):
        self.color = new_color
        print(f'Color is changed to {new_color}')
# bmw = Car(name = 'BMW', color = 'Black', year=2000, is_crashed=False)
# print(bmw.name, bmw.color, bmw.year, bmw.is_crashed, bmw.wheels_number)
#
# opel = Car('OPEL', 'White', 2015, False)
# opel.drive('Moscow')
#
# class Middle_earth:
#     def __init__(self, name, power, health, speed):
#         self.power = power
#         self.health = health
#         self.speed = speed
#         self.name = name
#     def specific(self):
#         print(self.name)
#         print('Сила:', self.power)
#         print('Здоровье:', self.health)
#         print('Скорость:', self.speed)
#         print('-------------')
#     def take_damage(self,damage):
#         self.health -= damage
# elves = Middle_earth('Эльфы',15,40,10)
# people = Middle_earth('Люди',12,50,5)
# gnomes = Middle_earth('Гномы', 10,10,2)
# elves.specific()
# people.specific()
# gnomes.specific()
# import time
# while elves.health > 0 or people.health > 0:
#     people.take_damage(elves.power)
#     elves.take_damage(people.power)
#     print(elves.health)
#     print(people.health)
#     time.sleep(2)

class Truck(Car):
    wheels_number = 6
    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
    def drive(self,city):
        print(f'Truck {self.name.title()} is driving to {city.title()} !!!')
    def load_cargo(self, weight):
        print(f'Truck {self.name.title()} loaded cargo, {weight} kg!')
truck1 = Truck('AKS', 'red', 2013, False)
truck1.drive('Moscow')
truck1.load_cargo(1000)
truck1.change_color('yellow')
name1 = 1
print(truck1.wheels_number)



