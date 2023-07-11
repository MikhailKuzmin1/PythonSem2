'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''
number = int(input('Введите число: '))
i = 0
base = 2
while base**i <= number:
    if base**i <= number:
        print(base**i)
        i += 1
    else:
        i += 1