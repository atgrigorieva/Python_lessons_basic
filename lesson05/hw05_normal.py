# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import sys
import homework_easy


def help():
    print("""Вы можете:
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку

    Для этого введите соответствующий номер
    """)


def main():
    do = {
        'help': help,  # Помощь
        '1': homework_easy.change_directory,  # Перейти в папку
        '2': homework_easy.list_of_directory,  # Просмотреть содержимое
        '3': homework_easy.delete_folder,  # Удалить папку
        '4': homework_easy.create_folder  # Создать папку
    }

    try:
        key = sys.argv[1]
    except IndexError:
        key = None

    if key:
        if do.get(key):
            do[key]()
        else:
            print('Неверный ключ, напишите "help" для получения справки')




if __name__ == "__main__":
    main()
