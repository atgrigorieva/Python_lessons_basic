__author__ = 'Григорьева Анастасия Тимофеевна'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

for fruit in range(0, len(fruits)):
    print(str(fruit+1) + '. {:>8}'.format(fruits[fruit]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = []
list2 = []

lenList1 = input('Введите размер 1 списка: ')
lenList2 = input('Введите размер 2 списка: ')

for el in range(int(lenList1)):
    element = input('Введите значение элмента для списка 1: ')
    list1.append(element)

for el in range(int(lenList2)):
    element = input('Введите значение элмента для списка 2: ')
    list2.append(element)

print("Элменты списка 1: ")
print(list1)
print("Элменты списка 2: ")
print(list2)


for el in list1:
    if(el in list2) == True:
        list1.remove(el)

print("Новые элменты списка 1: ")
print(list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list1 = []
lenList1 = input('Введите размер списка: ')
for el in range(int(lenList1)):
    #element = input('Введите значение элмента для списка 1: ')
    #list1.append(element)
    while True:
        try:
            element = int(input('Введите значение элмента для списка: '))
            list1.append(element)
            break;
        except ValueError:
            print("Только числа")

print("Значения списка: ")
print(list1)

list2 = []

for el in list1:
    print(el)
    if el % 2 == 0:
        list2.append(el/4)
    else:
        list2.append(el * 2)
print("Значения списка 2: ")
print(list2)