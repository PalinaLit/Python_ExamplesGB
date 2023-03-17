# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

print(f'Введите количество элементов в массиве')
n = int(input())

from random import randint
list = [randint(1, 5) for i in range(n)]

print(list)

print(f'Задайте некоторое число X')
x = int(input())

nearest_x = 0

for i in list:
    if abs(i - x) < i - nearest_x: 
        nearest_x = i
        i += 1

print(f'Cамый близкий по величине элемент к заданному числу X -> {nearest_x}')