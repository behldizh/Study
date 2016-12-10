"""
Поменять условие четность, нечетность


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
array = [1, 2, 2, 4, 5, 1, 1, 2, 3, 4]
dictionary = {"initial": array, "unique": []}

def unique_match(array, dictionary):
    for i in range(0, len(array)):
        if array.count(array[i]) <= 1 or array.count(array[i]) % 2 == 1:
            dictionary["unique"].append(array[i])
    print("Уникальные элементы массива: " + str(dictionary["unique"]))

unique_match(array, dictionary)
