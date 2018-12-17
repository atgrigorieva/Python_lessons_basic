# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

list_rand = [random.randint(-10, 10) for _ in range(10)]
print(list_rand)


list_rand_new = [el**2 for el in list_rand]
print(list_rand_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_fruits1 = ['apple', 'banana', 'cherry']
list_fruits2 = ['apple', 'banana', 'lemon', 'mango']

fruits1_fruits2 = [fruit for fruit in list_fruits1 if (fruit in list_fruits2) == True]
print(fruits1_fruits2)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list_rand2 = [random.randint(-10, 10) for _ in range(10)]
print(list_rand2)
new_list = [el for el in list_rand2 if el % 3 == 0 and el > 0 and el % 4 != 0]
print(new_list)