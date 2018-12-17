# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def ploshad(self):
        self.perimetr /=2
        self.ploshad =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.ploshad)

    def vysota(self):
        self.ploshad *=2
        self.vysota =  round((self.ploshad / self.CA),2)
        return (self.vysota)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

my_tri = Triangle(2, 2, 5, 8, 7, 4)

print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC, my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.ploshad()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.vysota()))


# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# Собрал все в кучу, слишком просто


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def car_go(self):
        print('Машина {} начала свое движение!'.format(self.name))

    def car_stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def car_turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


my_car = Car(100, 'Red', 'MArusya')

my_car.car_go()
my_car.car_turn('Налево')
my_car.car_stop()

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


import random
import time
import math


class War:
    def __init__(self, name, race, armor, type, health, damage):
        self.name = name
        self.race = race
        self.armor = armor
        self.type = type
        self.health = health
        self.damage = damage


class Warrior(War):
    def __index__(self, name, race, armor, type, health, damage):
        War.__init__(self, name, race, armor, type, health, damage)


class Enemy(War):
    def __index__(self, name, race, armor, type, health, damage):
        War.__init__(self, name, race, armor, type, health, damage)


class Battle():


    def player(**kwargs):
        person = 'Великий {} {} мы приветствуем тебя на нашей битве! Помни, что твой уровень здоровья равен {}%,  сила удара {}'.format(
            kwargs['type_of_warrior'], kwargs['name'], kwargs['health'], kwargs['damage'])
        return person


    def attack(health, damage):
        if health > 0:
            armor = random.randrange(0, 2)
            arg_armor = random.randrange(1, 7)
            if armor == 1:
                health = health - (damage * (arg_armor / 10))
                protection = 'Броня смягчила удар.'
            else:
                health -= damage
                protection = 'Удар сквозь броню.'

        else:
            health <= 0

        return (math.trunc(health), protection)


type_list = {'1': 'Воин', '2': 'Эльф', '3': 'Орк'}
names_of_enemy = {'1': '\'Могучий Слон\'', '2': '\'Меткий Глаз\'', '3': '\'Несокрушимая Стена\''}
damage_man = random.randrange(10, 30)
damage_elf = random.randrange(5, 40)
damage_ork = random.randrange(0, 50)
health_full = 100
health = health_full * 2
health_enemy = health_full

type_of_warrior = input('Выберите кем Вы будете 1 - Воин, 2 - Эльф, 3 - Орк: ')
name = input('Введите свое имя: ')

if type_of_warrior == '1':
    damage = damage_man
    playman = {'type_of_warrior': 'Воин', 'name': name.title(), 'health': health_full, 'damage': damage}
elif type_of_warrior == '2':
    damage = damage_elf
    playman = {'type_of_warrior': 'Эльф', 'name': name.title(), 'health': health_full, 'damage': damage}
elif type_of_warrior == '3':
    damage = damage_ork
    playman = {'type_of_warrior': 'Орк', 'name': name.title(), 'health': health_full, 'damage': damage}
else:
    print('ЭЭЭЭ СТОП! Вы неверно выбрали расу. До свидания.')
    time.sleep(3)
    exit()

time.sleep(2)

enemy = str(random.randrange(1, 4))

if enemy == '1':
    damage_enemy = damage_man
elif enemy == '2':
    damage_enemy = damage_elf
elif enemy == '3':
    damage_enemy = damage_ork

print('Ваш соперник {} {}.'.format(type_list[enemy], names_of_enemy[enemy]))
time.sleep(3)

print(Battle.player(**playman))

time.sleep(2)
while health > 0:
    if health_enemy > 0:
        kick = input('Нанести удар? y/n: ')
        if kick == 'y':
            health_enemy, protection = Battle.attack(health_enemy, damage)
            print('Вы нанесли урон, уровень здоровья вашего противника равен: {}%. {}'.format(health_enemy, protection))
            time.sleep(3)
            health, protection = Battle.attack(health, damage_enemy)
            print('Вам нанесли урон, ваш уровень здоровья равен: {}%. {}'.format(health, protection))
        else:
            print('Слабак, сбежал с поля боя')
            time.sleep(3)
            exit()
    else:
        print('ТАДА!!!! ПОБЕДА!! {} {} вы победили в честной схватке! У Вас осталое еще {}HP.'.format(type_list[enemy],
                                                                                                      names_of_enemy[
                                                                                                          enemy],
                                                                                                      health))
        any = input('Пресс эни кей')
        exit()

else:
    print('THE END. {} {} вы пали геройской смертью'.format(type_list[type_of_warrior], name))

any = input('Пресс эни кей')
exit()