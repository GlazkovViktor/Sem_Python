import random
# Задача 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input("Введите вещественное число: ")
# summ = 0
# for i in range(len(n)):
#     if n[i] != '.':
#         summ = summ+ int(n[i])
# print(summ)

# 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.

# n = int(input("Введите N: "))
# my_list = []
# summ = 0
# for i in range(1, n+1):
#     my_list.append(round((1+1/i)**i,2))
# print(my_list)
# for i in range(len(my_list)):
#     summ = summ+my_list[i]
# print(summ)

# задача 3 перемешат список
n = int(input("Введите N: "))
my_list = []
for i in range(n):
    my_list.append(random.randint(0,9))
leng = len(my_list)
print(my_list)
for i in range(leng):
    i_random = random.randint(0, leng-1)
    temp = my_list[i]
    my_list[i] = my_list[i_random]
    my_list[i_random] = temp
print(my_list)


