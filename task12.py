'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.'''
print('Задумайте 2 натуральных числа не больше 1000')
while True:
    first_number = int(input('Введите сумму этих чисел: '))
    second_number = int(input('Введите произвидение этих чисел: '))
    if first_number > 2000 or second_number > 1000000 or first_number <0 or second_number < 0:
        print('Одно из ваших замуннах чисел превышает 1000, либо число не натуральное')
        print('Задумайте 2 натуральных числа не больше 1000, либо число не натуральное')
    else:
        break
summa = -1
multiplier = -1
for i in range(0,first_number + 1):
    for j in range(0,second_number + 1):
        if i + j == first_number and i * j == second_number:
            summa = i
            multiplier = j
if summa == -1 or multiplier == -1:
    print('Вы допустили ошибку в подсчетах')
elif summa == 0 or multiplier == 0:
    print('Вы задумали 0 и 0')
else:
    print(f'Вы задумали числа: {summa} и {multiplier}')