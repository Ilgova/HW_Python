# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

# *Пример:*

# 5
#     7 -2 3 5 1
#     3
#     -> 1
N = int(input('Количество чисел в массиве: '))
a = [int(input('Введите число: ')) for i in range(N)]
x = int(input('Искомое число:'))
print('Столько раз встречается искомое число: ', a.count(x))