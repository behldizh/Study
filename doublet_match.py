"""
TODO:
Написать функцию которая возвращает не повторяющееся значение массива.(done)
Если таких элементов больше чем один, вернуть остальные


# Заполнение массива вручную
array = []
n = int(input('N: '))

for i in range(0, n):
    array.append(int(input('Element: ')))

# Заполнение массива с использованием random

from random import random

n = 8
array = [0] * n
for i in range(n):
    array[i] = int(random() * 10)
print(array)

"""

array = [1, 3, 8, 3, 2, 1, 4, 2]
uniq_array = []
n = len(array)
match = 'Есть совпадение '
marker = False


def doublet_match(array, n, match, uniq_array):
    for i in range(n-1):
        print("Проверяем " + str(array[i]))
        for j in range(i+1, n):
            if array[i] == array[j]:
                print(match + str(array[i]))
                break
            elif array.count(array[i]) == 1:
                uniq_element = "Элемент " + str(array[i]) + " уникален"
                uniq_array.append(array[i])
                print(uniq_element)
                break
    print('Вывод набора уникальных элементов: ' + str(uniq_array))

doublet_match(array, n, match, uniq_array)
