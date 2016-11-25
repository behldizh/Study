import os

path = './my_files/'
my_list = []
max_size = 0
max_file_size = 0

for directory in os.walk(path):
    my_list.append(directory)

for d, dirs, files in os.walk('./my_files'):
    size = os.path.getsize(d)
    if size > max_size:
        max_size = size
        print("На данной итерации, максимальный размер у директории: " + d)
    for f in files:
        path = os.path.join(d, f)
        size_of_file = os.path.getsize(path)
        if max_file_size < size_of_file:
            result = "Файл " + f + " в директории " + d + " имеет максимальный размер, равный: " + str(size_of_file)

print(result)

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
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            print(path)
        else:
            walk(path)

walk(path)
"""
