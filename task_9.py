# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X

# *Пример:*

# 5
#     7 -2 3 5 1
#     6
#     -> 7

N = int(input('Количество чисел в массиве: '))
a = [int(input('Введите число: ')) for i in range(N)]
x = int(input('Искомое число:'))
number = 0
for i in range(len(a)):
    if x - a[i] < x-number and x - a[i] > 0:

        number = i
print('близкий по величине элемент к заданному числу X: ', a[number])
