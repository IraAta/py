#!/usr/bin/env python

# Задаём 6-и значный формат номеру билета
ticket = "{number:06}".format(number=0)

# Задаём глобальные переменные
ticketCount = 0
max = 1000000

# Функция для подсчёта суммы чисел с входящей строки
def sum(num):
    result = 0
    for x in num:
        result += int(x)
    return result

# функция для резделения 6-и значнего числа на 2 части и назначение их глобальным переменным
def separator(ticket):
    global left
    global right
    left = ticket[0:3]
    right = ticket[3:6]

# функция сравнения суммы двух частей числа билета
def compare():
    global ticket
    separator(ticket)
    if sum(left) == sum(right):
        global ticketCount
        ticketCount += 1
    ticket = str("{number:06}".format(number=int(ticket) + 1))

# главная функция программы (точка входа main)
def main():
    while int(ticket) != max:
        compare()
    print("The number of lucky tickets is: %d" % ticketCount)

# определение точки входа
if __name__ == '__main__':
    main()
         

