# Напишите программу на Python для суммирования трех заданных целых чисел.
# Однако, если два значения равны, сумма будет равна нулю.

def sum_3(number_1, number_2, number_3):
    if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
        return 0
    return number_1 + number_2 + number_3


print(sum_3(5, 10, 7))
