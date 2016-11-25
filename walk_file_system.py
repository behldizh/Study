import os

path = './my_files/'
max_size = 0
max_file_size = 0


def walk_function(max_size, max_file_size, path):
    for d, dirs, files in os.walk('./my_files'):
        size = os.path.getsize(d)
        if size > max_size:
            max_size = size
            print("На данной итерации, максимальный размер у директории: " + d)
        for f in files:
            path = os.path.join(d, f)
            size_of_file = os.path.getsize(path)
            if max_file_size < size_of_file:
                result = "Файл " + f + " в директории " + d + " имеет максимальный размер, равный: " + str(size_of_file) + " байт"
    print(result)

walk_function(max_file_size, max_file_size, path)



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
