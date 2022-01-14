# Напишите программу на Python для суммирования первых n натуральных чисел.

def sum_natural(n):
    return sum(i for i in range(1, n + 1))
print(sum_natural(100))
