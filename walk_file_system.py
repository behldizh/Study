"""
Найти максимальный размер директории или файла на каждом уровне

"""


import os

directory = './blog/'
path = './blog/'


def walk_function(directory):

    max_size = 0
    max_file_size = 0

    for d, dirs, files in os.walk(directory):
        size = os.path.getsize(d)
        if size > max_size:
            max_size = size
        for f in files:
            next_path = os.path.join(d, f)
            size_of_file = os.path.getsize(next_path)
            if max_file_size < size_of_file:
                result = "Файл " + f + " в директории " + d + " имеет максимальный размер, равный: " + str(size_of_file) + " байт"
    print(result)

walk_function(path)



"""
path_f = []

for d, dirs, files in os.walk('./my_files'):

    for f in files:
        # формирование адреса
        path = os.path.join(d, f)
        # получение размера файла относительно адреса
        print("Размер файла " + str(f) + " равен: " + str(os.path.getsize(path)))
        # добавление адреса в список
        path_f.append(path)
"""
