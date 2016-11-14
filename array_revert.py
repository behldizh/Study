array = []
n = int(input('N: '))
k = int(input('k: '))

for i in range(0, n):
    array.append(int(input('Элемент: ')))


def revert(array, k):
    array1 = array.copy()

    for i in range(0, len(array)):
        tmp = array1[i]
        array1[i] = array[((i+k) % len(array))]
        array[((i+k) % len(array))] = tmp

revert(array, k)

print(array)
