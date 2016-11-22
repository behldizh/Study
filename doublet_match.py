"""array = []
n = int(input('N: '))

for i in range(0, n):
    array.append(int(input('Element: ')))

TODO:
Написать функцию которая возвращает не повторяющееся значение массива.
Если таких элементов больше чем один, вернуть остальные

n = 8
array = [0] * n
for i in range(n):
    array[i] = int(random() * 10)
print(array)



"""
#from random import random


array = [1, 3, 8, 3, 2, 1, 4, 2]
n = len(array)
match = 'Есть совпадение '


def doublet_match(array, n, match):
    for i in range(n-1):
        print("Проверяем " + str(array[i]))
        for j in range(i+1, n):
            if array[i] == array[j]:
                print(match + str(array[i]))
                break
            elif array.count(array[i]) == 1:
                uniq_element = "Элемент " + str(array[i]) + " уникален"
                print(uniq_element)
                break

doublet_match(array, n, match)
