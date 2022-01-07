# Напишите программу на Python для вычисления наибольшего общего делителя (GCD) из
# двух натуральных чисел.

def max_divider(number_1, number_2):
    n = 0
    if number_2 % number_1 == 0:
        return number_1
    for i in range(int(number_1 / 2), 0, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            n = i
            break
    return n


print(max_divider(10, 20))
print(max_divider(12, 17))
print(max_divider(4, 6))
