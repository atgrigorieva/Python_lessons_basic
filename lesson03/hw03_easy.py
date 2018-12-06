# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    numberStr = str(number)

    countNum = 0
    numberStrNew = ''
    point = False
    for num in numberStr:
        if(num == '.'):
            point = True

        if point == True and num != '.':
            countNum = countNum + 1
            if countNum == ndigits:
                if int(numberStr[countNum + 1]) >= 5:

                    while int(numberStrNew[countNum]) == 9:
                        numberStrNew = numberStrNew[:len(numberStrNew) -1]
                        countNum = countNum - 1
                        if numberStrNew[countNum] == '.':
                            break
                    if countNum == 1:
                        numberStrNew = numberStrNew[:len(numberStrNew) - 1]
                        numberStrNew = str(int(numberStrNew) + 1)

                    else:
                        numberStrNew = numberStrNew[:countNum] + str(int(numberStrNew[countNum]) + 1)

                else:
                    numberStrNew = numberStrNew + num
                break
        numberStrNew = numberStrNew + num

    return numberStrNew



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_Part1 = ''
    ticket_numbert_Part2 = ''
    part1Cancel = False
    for i in range(0, len(str(ticket_number))):
        if i == len(str(ticket_number))/2:
            part1Cancel = True
        if part1Cancel != True:
            ticket_number_Part1 = ticket_number_Part1 + str(ticket_number)[i]
        else:
            ticket_numbert_Part2 = ticket_numbert_Part2 + str(ticket_number)[i]


    summPart1 = 0
    summPart2 = 0

    for i in ticket_number_Part1:
        summPart1 = summPart1 + int(i)

    for i in ticket_numbert_Part2:
        summPart2 = summPart2 + int(i)

    if summPart1 == summPart2:
        return 'Счастливый билет'
    else:
        return 'Не счастливый билет'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
