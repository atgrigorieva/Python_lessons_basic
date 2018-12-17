# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def main():
    for i in range(1, 10):
        try:
            os.mkdir('dir_{}'.format(i))
        except FileExistsError:
            print('Директория с названием "dir_{}" уже существует'.format(i))

    for i in range(1,10):
        os.rmdir('dir_{}'.format(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

    current_directory_list = os.listdir(os.getcwd())

    for i in current_directory_list:
        if os.path.isdir(i):
            print(i)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    currentfile = os.path.basename(__file__)
    splinned = os.path.splitext(os.path.basename(__file__))

    # shutil.copy2(currentfile, os.path.join(os.getcwd(), '{}_copy{}'.format(splinned[0], splinned[1])))


# Для normal

def list_of_directory():
    current_directory_list = os.listdir(os.path.dirname(os.path.realpath(__file__)))

    print('Текущая директория {} содержит:'.format(os.getcwd()))
    for i in current_directory_list:
            print('{}. {}'.format(current_directory_list.index(i)+1, i))

def delete_folder():
    folder_name = input('Введите имя папки для удаления: ')
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_name)
    if os.path.isdir(dir_path):
        try:
            os.rmdir(dir_path)
            print('Папка {} успешно удалена'.format(folder_name))
        except OSError:
            add_input = input('Папка, которую вы хотите удалить содержит в себе что-то еще, вы действительно хотите удалить её? [Y/N]')
            if add_input == 'Y':
                shutil.rmtree(dir_path)
                print('Папка {} и её вложения успешно удалены')
            elif add_input == 'N':
                print('OK')
                return
            else:
              print('Ответ не опознан, операция прекращенна')
              return
    else:
        print('Объект с именем {} не найден, либо не является папкой'.format(folder_name))

def create_folder():
    folder_name = input('Введите имя папки для создания: ')
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_name)
    try:
        os.mkdir(dir_path)
        print('Папка {} успешно создана'.format(folder_name))
    except FileExistsError:
        print('Папка с именем {} уже существует'.format(folder_name))

def change_directory():
    user_input = input('Введите название папки в которую хотите перейти: ')
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), user_input)
    try:
        os.chdir(path)
        print('Успешено перешли в {}'.format(user_input))
    except FileNotFoundError:
        print('Такой папки не существует')

if __name__ == "__main__":
    main()