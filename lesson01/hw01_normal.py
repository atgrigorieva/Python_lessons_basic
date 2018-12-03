
__author__ = 'Григорьева Анастасия Тимофеевна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

while True:

    try:
        number = int(input("Введите любое целое число: "))

        maxNumber = 0

        for iNumber in str(number):
            if int(iNumber) > maxNumber:
                maxNumber = int(iNumber)

        print("Наибольшее число в числе ", number, " = ", maxNumber)

        break;
    except ValueError:
        print("Только числа")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input("Введите любую строку: ")

while (a == ''):
    a = input("Введите любую строку: ")

b = input("Введите любую строку: ")

while (b == ''):
    b = input("Введите любую строку: ")

a,b = b,a
print("a = ", a)
print("b = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a,b,c = 0,0,0

while True:

    try:
        a = int(input("Введите любое целое число: "))

        break;
    except ValueError:
        print("Только числа")

while True:

    try:
        b = int(input("Введите любое целое число: "))

        break;
    except ValueError:
        print("Только числа")

while True:

    try:
        c = int(input("Введите любое целое число: "))

        break;
    except ValueError:
        print("Только числа")


D = math.pow(b, 2) - 4 * a * c

if D > 0:
    x1 = ((0 - b) + math.sqrt(D)) / (2 * a)
    x2 = ((0 - b) - math.sqrt(D)) / (2 * a)

    print("Уравнение ax² + bx + c = 0, где a = ", a, " b = ", b, " c = ", c, " имеет 2 решения, x1 = ", x1, " x2 = ", x2)

elif D == 0:
    x = (-1 * b) / (2 * a)

    print("Уравнение ax² + bx + c = 0, где a = ", a, " b = ", b, " c = ", c, " имеет 2 решения, x = ", x)

else:
    print("Уравнение ax² + bx + c = 0, где a = ", a, " b = ", b, " c = ", c, " решений не имеет, так как D < 0")