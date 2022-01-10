# Напишите программу на Python, которая будет возвращать true, если два заданных
# целочисленных значения равны или их сумма или разность равна 5.

def checking_numbers(number_1, number_2):
    return True if number_1 == number_2 or number_1 - number_2 == 5 \
                        or number_1 + number_2 == 5 else False


print(checking_numbers(7, 2))
print(checking_numbers(3, 2))
print(checking_numbers(2, 2))
print(checking_numbers(10, 2))
