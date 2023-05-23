# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Ввод:пара-ра-рам рам-пам-папам па-ра-па-дам         Вывод:Парам пам-пам

def temp(str):
    str = str.split()
    list = []
    for phrase in str:
        res = 0
        for i in phrase:
            if i in 'аеёиоуыэюя':
                res += 1
        list.append(res)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if temp(str):
    print('Парам пам-пам')
else:
    print('Пам парам')
