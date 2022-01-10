# Напишите программу на Python для суммирования двух заданных целых чисел. Однако,
# если сумма составляет от 15 до 20, она вернет 20.

def sum_numbers(number_1, number_2):
    number = number_1 + number_2
    return 20 if 15 <= number < 20 else number


print(sum_numbers(10, 10))
