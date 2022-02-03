# Напишите программу на Python для вычисления суммы цифр в целом числе.

def sum_numbers(number):
    er = 0
    while True:
        dd = number % 10
        er += dd
        ff = number // 10
        number = ff
        if ff == 0:
            break
    return er

print(sum_numbers((5245)))
