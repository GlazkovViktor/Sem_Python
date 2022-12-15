# a=int(input('a= '))
# b=int(input('b= '))
# if a>b:
#     print(a)
# else:
#     print(b)

# сравнить квадрат одного, является ли квадратом
# num1 = int(input('Введите 1-ое числа: '))
# num2 = int(input('Введите 2-ое числа: '))
# if num2 == num1**2 or num1 == num2**2:
#     print('yes')
# else:
#     print('NO')

# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# number3 = int(input('Введите третье число: '))
# number4 = int(input('Введите четвертое число: '))
# number5 = int(input('Введите пятое число: '))

# max = number1
# if number2>max:
#     max = number2
# if number3>max:
#     max = number3
# if number4>max:
#     max = number4
# if number5>max:
#     max = number5
# print(max)
# import random
# my_list = []
# range_list = int(input('Введите кол-во элементов: '))
# for i in range(range_list):
#     my_list.append(random.randint(-100,100))

# print(my_list)
# maxx = my_list[0]
# for item in my_list:
#     if item > maxx:
#         maxx = item
# print(maxx)

# Принимаем программу число N и выводим список от минус N до N
# my_list = []
# N = int(input('Введите N: '))
# k = -N

# for i in range(-N, N+1):
#     my_list.append(i)
# print(*my_list, sep=', ')

#  Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
# N = float(input('Введите дробное число: '))
# N = (N*10) % 10
# if N ==0:
#     print('нет')
# else:
#     print(int(N))

# Домашнее задание Cеминар 1.

#                           Задание 1 Принимаем цифру, отвечаем явялеется ли днем недели

# Day = int(input('Введите цифру: '))
# if 1 <= Day <= 7:
#     print('Являеется')
# else:
#     print('Не является')

#                          Задание 3 Принимаем x и y  и выдает номер плоскости

# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))
# if x > 0 and y > 0:
#     print('1 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x == 0 and y == 0:
#     print('Начало координат')
# if x == 0 and y != 0:
#     print('Ось Y')
# if x != 0 and y == 0:
#     print('Ось X')

#                           Задание 4 по заданому номеру четверти дипазон коодинат


# x = int(input('Введите четверть: '))
# if x == 1:
#     print('x>0 and y>0')
# if x == 2:
#     print('x<0 and y>0')
# if x == 3:
#     print('x<0 and y<0')
# if x == 4:
#     print('x>0 and y<0')

#                          Задание 5 расстяоние между точками в 2Д прос-ве
import math
x1 = int(input('Введите X1: ')) 
y1 = int(input('Введите Y1: '))
x2 = int(input('Введите X2: '))
y2 = int(input('Введите Y2: '))
Dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'Расстояние между точками: {Dist}')
