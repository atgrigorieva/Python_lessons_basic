# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def makeDir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
        return

    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
        return

count_new_dir = input("Введите кол-во новых директорий для создания: ")

for _ in range(int(count_new_dir)):
    name_new_dir = input("Введите имя новой директории: ")
    makeDir(name_new_dir)

def removeDir(dir_name):
    if os.path.exists(dir_name):
        if os.path.isfile(dir_name):
            print("{} - это файл!".format(dir_name))
        elif os.path.isdir(dir_name):
            files = os.listdir(dir_name)
            if len(files) == 0:
                os.rmdir(dir_name)
            else:
                shutil.rmtree(dir_name)
    else:
        print('Указанный объект не найден')

count_remove_dir = input("Введите кол-во директорий, которые необходимо удалить: ")

for _ in range(int(count_remove_dir )):
    name_remove_dir = input("Введите имя директории для удаления: ")
    removeDir(name_remove_dir)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

list_dir = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
print(list_dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

copy_dir = shutil.copy(os.path.realpath(__file__), os.path.realpath(__file__) + '1')